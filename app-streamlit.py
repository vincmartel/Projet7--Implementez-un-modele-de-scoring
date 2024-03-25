import streamlit as st
import requests

# Titre de l'application
#st.title("Test de l'API de prédiction de défaut client")
st.title("Décision d'attribution de crédit")

# Affichage du logo "prêt à dépenser"
st.image('logo.jpg')

# Liste déroulante - sélection d'un identifiant de prêt dans la liste de test
prets_test = [12345678,100002, 100003, 100004, 100006, 100007, 100008, 100009, 100010, 100011, 100012]
SK_ID_CURR = st.selectbox("Identifiant du prêt", prets_test)

# Bouton pour effectuer la prédiction
if st.button("Résultat"):
    # Appel à l'API Flask
    api_url = "http://127.0.0.1:5000/prediction"
    payload = {"Identifiant du prêt": SK_ID_CURR}
    
    try:
        # Envoi de la requête à l'API et récupération de la réponse
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            # Traitement de la réponse de l'API
            result = response.json()
            if result['decision'] == "prêt refusé":
                st.error(f"Probabilité de défaut : {round(100*result['pred'])}% (La limite acceptable est 42%)")
                st.error(f"Décision :  {result['decision']}")
            elif result['decision'] == "prêt accordé":
                st.success(f"Probabilité de défaut : {round(100*result['pred'])} % (La limite acceptable est 42%)")
                st.success(f"Décision : {result['decision']}")
                
        else:
            st.error("Erreur lors de l'appel à l'API")
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur : {e}")