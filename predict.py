import joblib

# Chargement du modèle et du vectoriseur
model = joblib.load('trained_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

# Fonction pour effectuer une prédiction
def predict(titre):
    new_example_vectorized = vectorizer.transform([titre])
    prediction = model.predict(new_example_vectorized)
    return prediction[0]

# Exemple d'utilisation de la fonction de prédiction
titre = "La pollution des océans."
print("Prediction:", predict(titre))
