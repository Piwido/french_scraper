# Importations nécessaires
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import json
import joblib  # Pour sauvegarder le modèle et le vectoriseur

# Chargement et préparation des données
with open('json/training_set_balanced.json') as f:
    training_set = json.load(f)

documents = [(article["titre"], article["categorie"]) for article in training_set]

X = [doc[0] for doc in documents]
y = [doc[1] for doc in documents]

# Vectorisation et division des données
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Entraînement du modèle
model = MultinomialNB()

model.fit(X_train, y_train)

# Sauvegarde du modèle et du vectoriseur
joblib.dump(model, 'trained_model.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')

# Évaluation facultative du modèle
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)
