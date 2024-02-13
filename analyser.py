import json
from collections import Counter
import datetime

# Import des fichiers json
with open('json/articles.json') as f:
    articles = json.load(f)
with open('json/mots.json') as f:
    mots = json.load(f)

# Import des stopwords
stopwords_list = []

for word in mots:
    if word['category'] == 'stopword':
        stopwords_list.append(word['word'])

# Création d'une liste contenant tous les mots des titres et sous-titres
all_words = []
for article in articles:
    all_words.extend(article['titre'].split())
    all_words.extend(article['sous-titre'].split())

# Création d'un training set avec tous les titres d'articles et leur catégorie
training_set = []

# Tri des articles par catégorie
def sort_articles(articles, words_list):
    categories_count = {}
    total = len(articles)
    # Test pour éviter de classer un article plusieurs fois dans la même catégorie
    test = 0
    for article in articles : 
        test = 0
        for word in words_list:
            if ((word['word'].lower() in article['titre'].lower()) or (word['word'].lower() in article['sous-titre'].lower())) and test == 0:
                if word['category'] in categories_count:
                    categories_count[word['category']] += 1
                    if word['category'] != 'stopword':
                        test += 1
                    if word['category'] == 'politque':
                        print(word['word'])
                else:
                    categories_count[word['category']] = 1
                    if word['category'] != 'stopword':
                        test += 1
            
    # Trier les entrées par ordre décroissant de valeur
    sorted_categories = dict(sorted(categories_count.items(), key=lambda item: item[1], reverse=True))
    print(f"Répartition des articles par catégorie : {sorted_categories}")
    unclassed_articles = total - sum(categories_count.values()) + categories_count['stopword']
    print(f"Nombre d'articles non classés : {unclassed_articles}/{total}, pourcentage : {round(unclassed_articles / total * 100, 2)}%")
    return categories_count

# Similaire à sort_articles mais retourne une liste d'articles classés
def get_training_set(articles, words_list):
    categories_count = {}
    total = len(articles)
    training_set = []
    # Test pour éviter de classer un article plusieurs fois dans la même catégorie
    test = 0
    for article in articles : 
        test = 0
        for word in words_list:
            if ((word['word'] in article['titre']) or (word['word'] in article['sous-titre'])) and test == 0:
                if word['category'] in categories_count:
                    categories_count[word['category']] += 1
                    if word['category'] != 'stopword':
                        test += 1
                        training_set.append({"titre": article['titre'] + " " + article['sous-titre'], "categorie": word['category']})
                else:
                    categories_count[word['category']] = 1
                    if word['category'] != 'stopword':
                        test += 1
                        training_set.append({"titre": article['titre'] + " " + article['sous-titre'], "categorie": word['category']})
    # Trier les entrées par ordre décroissant de valeur
    sorted_categories = dict(sorted(categories_count.items(), key=lambda item: item[1], reverse=True))
    print(f"Répartition des articles par catégorie : \n{sorted_categories}")
    unclassed_articles = total - sum(categories_count.values()) + categories_count['stopword']
    print(f"Nombre d'articles non classés : {unclassed_articles}/{total}, pourcentage : {round(unclassed_articles / total * 100, 2)}%")
    # Exporte le training set dans un fichier json
    with open('json/training_set.json', 'w') as f:
        json.dump(training_set, f, indent=4)

# Log des résultats de l'analyse
def log_results(categories_count, articles, date=None):
    total = len(articles)
    if date == None:
        date = 'All time'
    with open('json/sites.json') as f:
        sources = json.load(f)

    with open('stats/log_analyser.txt', 'a') as f:
        f.write("##################################################\n")
        f.write(f"{str(datetime.datetime.now())} {str(total)} articles analysés.\n")
        f.write(f"Statistiques pour la période du {date} \n")
        unclassed_articles = total - sum(categories_count.values()) + categories_count['stopword']
        f.write(f"Nombre d'articles non classés : {unclassed_articles}, pourcentage : {round(unclassed_articles / total * 100, 2)}%\n")
        for category, count in categories_count.items():
            percentage = round(count / total * 100, 2)
            f.write(f"Nombre d'articles {category} : {count}, pourcentage : {percentage}%\n")
        # Récupération des sources
        f.write("Sources : ")
        for source in sources : 
            f.write(f"{source['Nom']}, ")
        f.write("\n")



# Création d'une liste d'articles d'une même date
def sort_articles_by_date(articles, date=None, date2=None):
    if date is None:
        print("Date non spécifiée, date du jour sélectionnée.")
        # Date d'aujourd'hui au format 'YYYY-MM-DD'
        date = str(datetime.date.today())
    # Recherche pour tout les articles enregistrés depuis le début
    elif date=="All time":
        print("Analyse de la répartition des articles par date.")
        dates = []
        for article in articles:
            if article['date'] not in dates:
                dates.append(article['date'])
        dates.sort()
        print(f"Répartition des articles par date : {len(dates)} dates différentes.")
        for date in dates:
            date_articles = [article for article in articles if article['date'] == date]
            print(f"Articles du {date} : {len(date_articles)}")
    # Recherche pour une date spécifique
    else:
        # Recherche pour une période 
        if date2 is not None:
            print(f"Sélection des articles du {date} au {date2}.")   
            articles_by_date = []
            for article in articles:
                if article['date'] >= date and article['date'] <= date2:
                    articles_by_date.append(article)
            return articles_by_date
        # Recherche pour une date 
        else:
            print(f"Sélection des articles du {date}.")   
            articles_by_date = []
            for article in articles:
                if article['date'] == date:
                    articles_by_date.append(article)
            return articles_by_date

date = '2024-02-12'
articles_by_date = sort_articles_by_date(articles, date)
log_results(sort_articles(articles_by_date, mots), articles_by_date, date)
#Recherche des mots les plus fréquents
counts = Counter(all_words)
counts.subtract(stopwords_list)


# Retrait des stopwords
filtered_words = []
list_of_words = counts.most_common(100)
for word in list_of_words:
    if word[0] not in stopwords_list :
        filtered_words.append(word)
for word in filtered_words:
    if word[0]=='—':
        filtered_words.remove(word)


