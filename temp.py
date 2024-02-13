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

    
## Retirer les noms de rubrique : titres de moins de 5 mots 
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
    # Mise à jour du fichier articles.json
    with open('json/articles.json', 'w') as f:
        json.dump(articles, f, indent=4)
    print(f"{count} articles retirés.")


# Test de la détections des caractères spéciaux 
def test_special_characters(articles):
    count = 0 
    for article in articles:
        if any('à' for char in article["titre"]):
            count += 1
    print(f"{count} articles contiennent des caractères spéciaux.")

training_set = load_data("training")
categories_count = count_categories(training_set)

articles = load_data()
remove_small_titles(articles)
