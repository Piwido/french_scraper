import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse  # Assurez-vous d'importer urlparse depuis urllib.parse
import json
import hashlib
import datetime
import re 
import sys

## TODO: if article.find([...]) is not None:


# TODO: ajouter en-tête utilisateur
# Récupère le contenu de la page
def get_soup (url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Erreur de requête HTTP pour l'url : {url}")
        print(f"Code de statut : {response.status_code}")
        exit()


# Suppression des doubles dans une liste d'articles
def remove_duplicates(articles):
    unique_articles = []
    seen_titles = set()  
    for article in articles:
        title = article["titre"]
        if title not in seen_titles:
            unique_articles.append(article)
            seen_titles.add(title)
    return unique_articles
# Retirer les noms de rubrique : titres de moins de 5 mots 
def remove_small_titles(articles):
    count = 0
    new_articles = []
    deleted_articles = []
    for article in articles:
        if (len(article["titre"].split()) > 4) or (len(article["sous-titre"].split()) > 4):
            new_articles.append(article)
        else:
            count += 1
            deleted_articles.append(article)
    # Sauvegarde temporaire des articles supprimés
    with open('json/deleted_articles.json', 'w') as f:
        json.dump(deleted_articles, f, indent=4)
    print(f"{count} articles retirés.")
    return new_articles


# Retrait des "\n" dans les titres et sous-titres
def remove_newline(articles):
    for article in articles:
        article['titre'] = article['titre'].replace("\n", "")
        article['sous-titre'] = article['sous-titre'].replace("\n", "")
    return articles

def clean_articles(articles):
    articles = remove_newline(articles)
    articles = remove_duplicates(articles)
    articles = remove_small_titles(articles)
    return articles
#Récupère les articles d'une page spécifique
# Format de retour : [[titre, sous-titre, date, site], ...]
def get_articles_bfmtv(soup):
    articles_brut = soup.find_all("h1", class_="title_une_item")
    articles_brut.extend(soup.find_all("h3", class_="content_item_title" ))
    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "BFMTV"])
    return articles

def get_articles_site(site, soup):
    ## Récupération des blocs de titres d'articles avec code html
    tags = site['Titres']
    articles_brut = []
    for tag in tags:
        if soup.find_all(tag[0], class_=tag[1]) is not None: 
            articles_brut.extend(soup.find_all(tag[0], class_=tag[1]))
    ## Récupération des titres et sous-titres
    articles = []
    title = ""
    subtitle = ""
    for article in articles_brut:
        title = article.text.strip()
        if (len(site['Sous-titre']) > 0):
            if article.find(site['Sous-titre'][0], class_=site['Sous-titre'][1]).text.strip() is not None:
                subtitle = article.find(site['Sous-titre'][0], class_=site['Sous-titre'][1]).text.strip()
        articles.append([title, subtitle, str(datetime.date.today()), site["Nom"]])
    return articles


# Fonction de création de hash pour chaque site
def get_hash(articles):
    articles_str = ""
    for article in articles:
        articles_str = article[0] + article[1]
    return hashlib.sha256(articles_str.encode('utf-8')).hexdigest()

def get_articles(sites_dict):
    articles = []
    for site in sites_dict:
        url = site['Url']
        soup = get_soup(url)
        site_name = site['Nom']
        # Stocke les articles nouveaux
        articles_site=get_articles_site(site, soup)
        # Si aucun article n'est trouvé, le code de la page a peut-être changé
        if len(articles_site) == 0:
            if site_name == "BFMtv":
                articles_site = get_articles_bfmtv(soup)  
            if len(articles_site) == 0:
                print(f"Aucun article récupéré sur {site_name}. Vérifiez le code de la page.")
                continue
        hash_site = get_hash(articles_site)
        if hash_site != site['Hash']:
            print(f"{site_name} a changé : Récupération des nouveaux articles")
            articles.extend(articles_site)
            # Mise à jour du hash
            site['Hash'] = hash_site
        else:
            print(f"{site_name} n'a pas changé")
        # Met à jour le fichier sites.json
    with open('json/sites.json', 'w') as f:
        json.dump(sites_dict, f, indent=4)
    return articles

### Export to json
# Création d'un dictionnaire pour chaque nouvel article
def create_article_dict(articles):
    articles_json = []
    for article in articles:
        article_dict = {
            "titre": article[0],
            "sous-titre": article[1],
            "date" : article[2],
            "source": article[3]
        }
        # Que tf1 détécté
        articles_json.append(article_dict)
    return articles_json


# Que TF1 détécté
# Filtrage des articles déjà dans le fichier articles.json
def filter_old_articles (articles_json):
    count = 0
    with open('json/articles.json') as f:
        articles = json.load(f)
    new_articles = []

    for article in articles_json:
    # TODO: ne pas prendre en compte l'heure
    # TODO: Sites des nouveaux articles et nombre d'articles   
        if article['titre'] not in [a['titre'] for a in articles]:
            new_articles.append(article)
            
            count += 1
    print(f"{count} nouveaux articles récupérés.")
    # S'il y a des nouveaux articles, affiche la source et le nombre d'articles
    if count > 0:
        print(f"Source des nouveaux articles : {journal_count(new_articles)}")
    total  = len(articles) + count
    print(f"Total : {total} articles.")
    return new_articles, count, total


# Ajout des nouveaux articles dans le fichier articles.json
def add_new_articles (new_articles_json):
    with open('json/articles.json') as f:
        articles = json.load(f)
    total = len(articles)
    articles.extend(new_articles_json)
    count = 0
    for article in articles :
        if (article['source'] == "bfmtv" or article['source'] == "BFMTV"):
            count += 1
    print(f"Nombre d'articles bfmtv : {count}")
    with open('json/articles.json', 'w') as f:
        json.dump(articles, f, indent=4)
    return total

def journal_count (articles):
    journal_count = {}
    for article in articles:
        if article["source"] in journal_count:
            journal_count[article["source"]] += 1
        else:
            journal_count[article["source"]] = 1
    return journal_count

def main ():
    # Import le dictionnaire des sites
    with open('json/sites.json') as f:
        sites_dict = json.load(f)
    

    articles = get_articles(sites_dict)
    articles_json = create_article_dict(articles)
    articles_json = clean_articles(articles_json)
    new_articles_json, new_number, total= filter_old_articles(articles_json)
    add_new_articles(new_articles_json)


    # Création d'un log pour suivre les modifications
    with open('log.txt', 'a') as f:
        f.write(f"{str(datetime.datetime.now())} {str(new_number)} articles ajoutés. Total {str(total)} \n")


# Vérifie si le script est exécuté en tant que programme principal
if __name__ == "__main__":
    # Appelle la fonction main() pour démarrer l'exécution du programme
    main()

