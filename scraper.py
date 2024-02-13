#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse  # Assurez-vous d'importer urlparse depuis urllib.parse
import json
import hashlib
import datetime
import re 
import sys


# Récupère le contenu de la page
def get_soup (url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Erreur de requête HTTP pour l'url : {url}")
        exit()

#Récupère les articles d'une page spécifique
# Format de retour : [[titre, sous-titre, date, site], ...]
def get_articles_le_figaro(soup):
    articles_brut = soup.find_all("h2", class_="fig-ranking-profile-headline")
    articles = []
    for article in articles_brut:
        title = article.text
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Le Figaro"])
    return articles

def get_articles_le_monde(soup):
    articles_brut = soup.find_all("p", class_="article__title")
    articles = []
    for article in articles_brut:
        title = article.text
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Le Monde"])
    return articles

def get_articles_le_parisien(soup):
    articles_brut = soup.find_all("a", class_="lp-f-subtitle-04")
    articles = []
    for article in articles_brut:
        title = article.text
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Le Parisien"])
    return articles

def get_articles_liberation(soup):
    articles_brut = soup.find_all("h2", class_="Headline-sc-16el3pa-0")
    articles = []
    for article in articles_brut:
        title = article.text
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Libération"])
    return articles

def get_articles_les_echos(soup):
    articles_brut = soup.find_all("h3", class_="sc-14kwckt-6")
    articles = []
    for article in articles_brut:
        title = article.text
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Les Echos"])
    return articles

def get_articles_mediapart(soup):
    articles_brut = soup.find_all("div", class_="teaser__container")
    articles = []
    title = ""
    subtitle = ""
    for article in articles_brut:
        if article.find("h3", class_="teaser__title" ) is not None:
            title = article.find("h3", class_="teaser__title" ).text.strip()
        if article.find("div", class_="teaser__body" ) is not None:
            subtitle = article.find("div", class_="teaser__body" ).text.strip()
        articles.append([title, subtitle, str(datetime.date.today()), "Mediapart"])
    for article in articles:
        article[0] = article[0].replace("\n", "")
        article[1] = article[1].replace("\n", "")
    unique_articles = []
    seen_titles = set()  # Ensemble pour stocker les titres déjà vus
    for article in articles:
        title = article[0]
        if title not in seen_titles:
            unique_articles.append(article)
            seen_titles.add(title)
    return unique_articles

def get_articles_l_express(soup):
    articles_brut = soup.find_all("h2", class_="thumbnail__title")
    articles = []
    for article in articles_brut:
        title = article.text
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "L'Express"])
    # Retrait des pubs en bas de page
    return articles[:-6]

def get_articles_marianne(soup):
    articles_brut = soup.find_all("a", class_="thumbnail__link")
    articles = []
    for article in articles_brut:
        title = article.text
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Marianne"])
    return articles

def get_articles_la_croix(soup):
    articles_brut = soup.find_all("a", class_="block-item__title")
    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "La Croix"])
    for article in articles:
        article[0] = article[0].replace("\n", "")
        article[1] = article[1].replace("\n", "")
    return articles

def get_articles_20_minutes(soup):
    articles_brut = soup.find_all("h3", class_="font-weight-bold@xs")
    articles_brut.extend(soup.find_all("h2", class_="font-weight-bold@xs" ))
    articles_brut.extend(soup.find_all("h3", class_="font-weight-semi-bold@xs" ))
    articles_brut.extend(soup.find_all("h4", class_="font-weight-semi-bold@xs" ))
    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "20 Minutes"])
    return articles

def get_articles_courrier_international(soup):
    articles_brut = soup.find_all("p", class_="title")
    articles_brut.extend(soup.find_all("h1", class_="title" ))
    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Courrier International"])
    return articles

def get_articles_bfmtv(soup):
    articles_brut = soup.find_all("h1", class_="title_une_item")
    articles_brut.extend(soup.find_all("h3", class_="content_item_title" ))
    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "BFMTV"])
    return articles

def get_articles_le_nouvel_obs(soup):
    articles_brut = soup.find_all("h2", class_="home_une_title")
    articles_brut.extend(soup.find_all("div", class_="h5-like" ))
    articles_brut.extend(soup.find_all("p", class_="h5-like" ))
    articles_brut.extend(soup.find_all("h2", class_="h5-like" ))
    articles_brut.extend(soup.find_all("h3", class_="h5-like" ))
    articles_brut.extend(soup.find_all("h3", class_="h6-like" ))
    articles_brut.extend(soup.find_all("h2", class_="h6-like" ))
    articles_brut.extend(soup.find_all("p", class_="h6-like" ))
    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Le Nouvel Obs"])
    return articles

def get_articles_huffington_post(soup):
    articles_brut = soup.find_all("p", class_="newsUne-title")
    articles_brut.extend(soup.find_all("div", class_="blockReading-statement" ))
    articles_brut.extend(soup.find_all("div", class_="horizontalCardTxt-title" ))
    articles_brut.extend(soup.find_all("h2", class_="card-title" ))
    articles_brut.extend(soup.find_all("p", class_="newsFeaturedArticle-chapo" ))
    articles_brut.extend(soup.find_all("a", class_="newsUne-item" ))
    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Huffington Post"])
    return articles

def get_articles_valeurs_actuelles(soup):
    articles_brut = soup.find_all("h2", class_="card-post__title")
    articles_brut.extend(soup.find_all("h3", class_="b-actu__item__title" ))
    articles_brut.extend(soup.find_all("a", class_="b-interview__txt" ))
    articles_brut.extend(soup.find_all("p", class_="b-letter__txt" ))

    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Valeurs Actuelles"])
    return articles

def get_articles_rtl(soup):
    articles_brut = soup.find_all("h3", class_="article-title")
    articles_brut.extend(soup.find_all("div", class_="flash-actu-card" ))
    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "RTL"])
    return articles

def get_articles_slate(soup):
    articles_brut = soup.find_all("p", class_="card-title")
    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Slate"])
    return articles

def get_artciles_le_telegrame(soup):
    articles_brut = soup.find_all("div", class_="tlg-element__text")
    articles = []
    for article in articles_brut:
        title = article.text.strip()
        subtitle = ""
        articles.append([title, subtitle, str(datetime.date.today()) , "Le Télégramme"])
    return articles

# Retrait des noms de rubrique (titre de moins de 4 mots)
def remove_invalid_articles(articles):
    for article in articles:
        if len(article[0].split()) < 4:
            articles.remove(article)
    return articles

# Fonction de création de hash pour chaque site
def get_hash(articles):
    articles_str = ""
    for article in articles:
        articles_str = article[0] + article[1]
    return hashlib.sha256(articles_str.encode('utf-8')).hexdigest()

def get_articles(sites_dict):
    for site in sites_dict:
        url = site['Url']
        soup = get_soup(url)
        site_name = site['Nom']
        # Stocke les articles nouveaux
        articles = []
        article_function_name = f"get_articles_{site_name.lower().replace(' ', '_')}"
        article_function = getattr(sys.modules[__name__], article_function_name)
        if callable(article_function):
            articles_site=article_function(soup)
            # Si aucun article n'est trouvé, le code de la page a peut-être changé
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
        else :
            print(f"La fonction {article_function_name} n'existe pas")

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
        articles_json.append(article_dict)
    return articles_json


# Filtrage des articles déjà dans le fichier articles.json
def filter_old_articles (articles_json):
    count = 0
    with open('json/articles.json') as f:
        articles = json.load(f)
    new_articles = []
    for article in articles_json:
        if article not in articles:
            new_articles.append(article)
            count += 1
    print(f"{count} nouveaux articles récupérés.")
    print(f"Total : {len(articles) + count} articles.")
    return new_articles, count


# Ajout des nouveaux articles dans le fichier articles.json
def add_new_articles (new_articles_json):
    with open('json/articles.json') as f:
        articles = json.load(f)
    total = len(articles)
    articles.extend(new_articles_json)
    with open('json/articles.json', 'w') as f:
        json.dump(articles, f, indent=4)
    return total



def main ():
    # Import le dictionnaire des sites
    with open('json/sites.json') as f:
        sites_dict = json.load(f)

    articles = get_articles(sites_dict)
    articles_json = create_article_dict(articles)
    new_articles_json, new_number = filter_old_articles(articles_json)
    total = add_new_articles(new_articles_json)

    # Création d'un log pour suivre les modifications
    with open('log.txt', 'a') as f:
        f.write(f"{str(datetime.datetime.now())} {str(new_number)} articles ajoutés. Total {str(total)} \n")


# Vérifie si le script est exécuté en tant que programme principal
if __name__ == "__main__":
    # Appelle la fonction main() pour démarrer l'exécution du programme
    main()

