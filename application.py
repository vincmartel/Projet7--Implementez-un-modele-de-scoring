# python script pour appeler 2 autres script, 1er script qui demarre une api flask et un 2eme script qui lance une application streamlit

# Chemin vers vos scripts
#script1_path = "api-flask.py"
#script2_path = "app-streamlit.py"

# Exécution du premier script
#subprocess.run(["python", script1_path]
#subprocess.run(["python", "-m", "api-flask.py"])
#subprocess.run(["python", "-m", "api-flask.py"])
#subprocess.run(["python", "api-flask.py"])

# Exécution du deuxième script
#subprocess.run(["python", "-m", "streamlit", "run", "app-streamlit.py"])
#subprocess.run(["python", "streamlit", "run", "app-streamlit.py"])

# Obtenez les variables d'environnement actuelles
#env = os.environ.copy()

# Modifiez la variable d'environnement PORT pour l'API Flask
#env["PORT"] = "8000"

# Exécutez api-flask.py avec Python en utilisant la nouvelle variable d'environnement
#subprocess.Popen(["python", "api-flask.py"], env=env)

# Exécutez app-streamlit.py avec Streamlit
#subprocess.Popen(["streamlit", "run", "app-streamlit.py"])

import subprocess
import os
import time


# Exécution du premier script
#subprocess.run(["python", script1_path]
#subprocess.run(["python", "-m", "api-flask.py"])

# Exécution du deuxième script
#subprocess.run(["python", "-m", "streamlit", "run", "app-streamlit.py"])




# Chemin relatif vers les scripts api-flask.py et app-streamlit.py
scripts_directory = "./"

# Obtenez les variables d'environnement actuelles
env = os.environ.copy()

# Modifiez la variable d'environnement PORT pour l'API Flask
env["PORT"] = "5000"

# Lancez l'API Flask
#api_process = subprocess.Popen(["python", f"{scripts_directory}/api-flask.py"], env=env)
api_process = subprocess.Popen(["python", f"{scripts_directory}/api-flask.py"], env=env)
print("L'API Flask est en cours de démarrage...")

# Attendez quelques secondes pour que l'API soit prête
time.sleep(5)

# Vérifiez si l'API Flask a démarré correctement
if api_process.poll() is None:
    print(f"L'API Flask a démarré avec succès sur le port {env['PORT']}.")
else:
    print("Erreur lors du démarrage de l'API Flask.")

# Lancez l'application Streamlit
#streamlit_process = subprocess.Popen(["streamlit", "run", f"{scripts_directory}/app-streamlit.py", "--server.port", "8501"], env=env)
#subprocess.run(["python", "streamlit", "run", "app-streamlit.py"])
#subprocess.run(["streamlit", "run", "app-streamlit.py"])
#subprocess.Popen(["streamlit", "run", "app-streamlit.py"])
#subprocess.run(["streamlit", "run", f"{scripts_directory}/app-streamlit.py"])
#streamlit run app-streamlit.py
#python -m streamlit run app-streamlit.py
#subprocess.Popen(["streamlit", "run", "app-streamlit.py"])
subprocess.run(["python", "-m", "streamlit", "run", "app-streamlit.py"])
print("L'application Streamlit est en cours de démarrage...")

# Attendez quelques secondes pour que l'application soit prête
time.sleep(5)

# Vérifiez si l'application Streamlit a démarré correctement
if streamlit_process.poll() is None:
    print("L'application Streamlit a démarré avec succès sur le port 8501.")
else:
    print("Erreur lors du démarrage de l'application Streamlit.")