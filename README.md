# Projet7: Implémentez un modèle de scoring

**API Flask pour la décision d'attribution de prêt**

Cette API Flask utilise un modèle de machine learning entrainé (LGBM Classifier) pour prédire la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé.

**Contenu du Dépôt**

- app.py: Le code de l’API Flask. Vous pouvez l’exécuter localement avec python app.py
- requirements.txt: La liste des dépendances et packages Python nécessaires pour exécuter l’API. Vous pouvez installer ces dépendances avec pip install -r requirements.txt

- liste_features.txt: La liste des features à conserver pour le modèle.
- scaler.pkl: Le scaler entraîné. Il est utilisé pour normaliser les caractéristiques d’entrée avant de faire des prédictions.
- lgbm_clf.pkl: Le modèle LGBM Classifier entraîné. Ce fichier est utilisé pour effectuer les prédictions.

- test_api.py: Les tests Pytest exécutés pendant le build.
- data_sample.csv: Un échantillon de demande de prêt pour tester l’API. 
- app-streamlit.py: l’interface Streamlit de test de l'API pour simuler un scoring et une décision d'attribution de prêt 

**Utilisation**

1)  Clonez ce dépôt sur votre machine locale.
2)  Installez les dépendances en exécutant pip install -r requirements.txt.
3)  Exécutez l’API Flask avec python app.py.
4)  Utilisez l’interface app-streamlit.py pour simuler un scoring client

**Déploiement vers Azure**

Nous utilisons GitHub Actions pour automatiser le processus de build et déploiement. Si les tests sont OK, l’API est déployée vers Azure.

URL de l'API: **https://scoringcredit.azurewebsites.net**
