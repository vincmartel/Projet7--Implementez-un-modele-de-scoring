#API Flask qui expose un endpoint (/prediction) pour effectuer des prédictions de probabilité de défaut de paiement et retourne un décision d'accord de prêt.

# Imports
import numpy as np
import pickle
import json
from flask import Flask, jsonify, request
import pandas as pd
import shap

# Création d'une instance de l’application Flask
app = Flask(__name__)

# Import d'un échantillon de 10 prets
sample = pd.read_csv('data_sample.csv')

# Import de la liste des 120 features sélectionnées
with open('liste_features.txt', 'rb') as features:
    liste_importee = pickle.load(features)
    
# Import du scaler entrainé
with open('scaler.pkl', 'rb') as scaler:
    loaded_scaler = pickle.load(scaler)

# Importer le modèle
with open('lgbm_clf.pkl', 'rb') as lgbm:
    loaded_model = pickle.load(lgbm)

# Vérification démarrage API
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'API Flask en cours d\'exécution !'})

# Définition d'une route pour l'API à l'adresse /prediction
@app.route('/prediction', methods=['POST'])
def prediction():
    
    # Récupération de l’identifiant du prêt envoyé depuis une application Streamlit
    data = request.json
    SK_ID_CURR = data['Identifiant du prêt']
    
    # Sélection du pret à partir de l'identifiant reçu de l'application Streamlit
    pret=sample[sample['SK_ID_CURR']==SK_ID_CURR]
    
    # Selection des 120 features sélectionnées du prêt
    pret=pret[liste_importee]

    # Transformation du dataframe pret (1x120) en array
    pret_array=pret.values

    # Standardisation à partir du scaler importé
    pret_array_std=loaded_scaler.transform(pret_array)

    # Prediction de la probabilité d’appartenance du prêt à la classe 1 (c’est-à-dire la probabilité de difficulté de paiement)
    proba=loaded_model.predict_proba(pret_array_std)[0][1]

    # Calculer les valeurs SHAP pour le prêt sélectionné
    explainer = shap.TreeExplainer(loaded_model)
    shap_values = explainer.shap_values(pret_array_std)
    
    # Décision de pret avec seuil de probabilité de défaut à 42%
    y_pred = (proba >= 0.42).astype(int)
    if y_pred == 1:
        classe = "prêt refusé"
    elif y_pred == 0:
        classe = "prêt accordé"
    else:
        classe = "cas d'erreur"

    # Shap value pour la classe 1 et transformation en liste
    #shap_local=shap_values[1][0].tolist()
    
    
    # Envoi de la réponse JSON contenant la probabilité de défaut (pred) et la décision concernant le prêt.
    try:
        return jsonify({'pred': proba,
                        'decision': classe,
                        'shap_local': shap_values[1][0].tolist(),  # Shap value pour la classe 1 et transformation en liste
                        'features': pret.columns.tolist(),
                        'values': pret.values[0].tolist()
                        #'shap_values': shap_values
                        #'feature_names': pret.columns.tolist(),
                        #'feature_values': pret.values[0].tolist()
                       }
                      )
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Si le script est exécuté directement, l’application Flask est lancée en mode débogage sur le port 5000    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
