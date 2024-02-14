import json

# Chargement et préparation des données
def load_data(mode="cleaning"):
    if mode == "training":
        with open('json/training_set.json') as f:
            articles = json.load(f)
    if mode == "cleaning":
        with open('json/articles.json') as f:
            articles = json.load(f)
    return articles

# Comptage des catégories
def count_categories(training_set):
    # Comptage du nombre d'articles par catégorie
    categories_count = {}
    for article in training_set:
        categorie = article["categorie"]
        if categorie in categories_count:
            categories_count[categorie] += 1
        else:
            categories_count[categorie] = 1
    print(f"Répartition des catégories d'articles : {categories_count}")
    return categories_count

# Equilibrage des catégories sous-représentées
def balance_categorie_under(training_set, categories_count):
    # Comptage du nombre moyen d'articles par catégorie
    total_categories = 0
    for categorie, count in categories_count.items():
        if categorie != "stopword":
         total_categories += count
    average_count = sum(total_categories) / (len(categories_count)-1)
    print(f"Nombre moyen d'articles par catégorie : {average_count}")

    # Detection des catégories sous-représentées
    new_training_set = []
    removed_articles = []
    for categorie, count in categories_count.items():
        if count < 0.1*average_count:
            print(f"La catégorie '{categorie}' est sous-représentée : nombre d'articles : {count}. Suppression de {count} articles.\n")
            removed_articles.extend([article for article in training_set if article["categorie"] == categorie])
        else: 
            new_training_set.extend([article for article in training_set if article["categorie"] == categorie])
    
    # Sauvegarde temporaire des articles supprimés
    former_removed_articles = []
    with open('json/removed_articles.json', 'w') as f:
        json.load(former_removed_articles, f)
    former_removed_articles.extend(removed_articles)
    with open('json/removed_articles.json', 'w') as f:
        json.dump(removed_articles, f, indent=4)

    # Mise à jour du fichier training_set.json
    with open('json/training_set_balanced.json', 'w') as f:
        json.dump(new_training_set, f, indent=4)
    print(f"{len(removed_articles)} articles retirés.")


#Equilibrage des catégories sur-représentées 
def balance_categories_over(training_set, categories_count):
    # Comptage du nombre d'articles par catégorie
    # Equilibrage de la sur-représentation de la catégorie "politique"
    balance_categories = []
    count = 0
    # Récupération du nombre d'éléments de la second catégorie la plus représentée
    max_count = 0
    for categorie, count in categories_count.items():
        if count > max_count and categorie != "politique":
            max_count = count
    for article in training_set:
        categorie = article["categorie"]
        if categorie == "politique" and count > max_count:
            count += 1
        else:
            balance_categories.append(article)
            if categorie == "politique":
                count += 1
    # Sauvegarde du fichier training_set_balanced.json
    print(f"{count-max_count} articles supprimés de la catégorie 'politique'.")
    json.dump(balance_categories, open('json/training_set_balanced.json', 'w'), indent=4)
    return balance_categories     

    


# Test de la détections des caractères spéciaux 
def test_special_characters(articles):
    count = 0 
    for article in articles:
        if any('à' for char in article["titre"]):
            count += 1
    print(f"{count} articles contiennent des caractères spéciaux.")


def reset_hashes():
    # Import des sites
    with open('json/sites.json') as f:
        sites = json.load(f)
    for site in sites:
        site["Hash"] = ""
    with open('json/sites.json', 'w') as f:
        json.dump(sites, f, indent=4)

# Fusion de deux fichiers d'articles au format JSON
def fusion_archive(filename):
    former_len = 0
    new_len = 0
    with open('json/'+filename) as f:
        archive = json.load(f)
    with open('json/articles.json') as f:
        articles = json.load(f)
    former_len = len(articles)
    for article in archive: 
        if article['titre'] not in [article['titre'] for article in articles]:
            articles.append(article)
    new_len = len(articles)
    with open('json/articles.json', 'w') as f:
        json.dump(articles, f, indent=4)
    print(f"{new_len - former_len} articles ajoutés. Total : {new_len} articles.")



# Ajout d'une section "sous-titre" à chaque site
def add_sous_titre():
    with open('json/sites.json') as f:
        sites = json.load(f)
    for site in sites:
        site["Sous-titre"] = ""
    with open('json/sites.json', 'w') as f:
        json.dump(sites, f, indent=4)

reset_hashes()

def add_site_entry():
    # Charge le fichier JSON des sites
    with open('json/sites.json', 'r') as f:
        sites = json.load(f)
    
    # Récupère les informations pour la nouvelle entrée
    site_name = input("Entrez le nom du site : ")
    site_url = input("Entrez l'URL du site : ")
    
    # Liste pour stocker les titres
    titres = []
    while True:
        titre_type = input("Entrez le type de titre (h1, h3, div), ou 0 pour terminer : ")
        if titre_type == '0':
            break
        titre_class = input("Entrez la classe du titre : ")
        titres.append([titre_type, titre_class])
    
    # Crée le nouvel objet de site
    new_site = {
        "Nom": site_name,
        "URL": site_url,
        "Hash": "",
        "Titres": titres,
        "Sous-titre": ""
    }
    
    sites.append(new_site)
    
    # Mise à jour du fichier JSON
    with open('json/sites.json', 'w') as f:
        json.dump(sites, f, indent=4)

