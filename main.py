# python script pour appeler 2 autres script, 1er script qui demarre une api flask et un 2eme script qui lance une application streamlit

import subprocess

# Chemin vers vos scripts
script1_path = "api-flask.py"
script2_path = "app-streamlit.py"

# Exécution du premier script
#subprocess.run(["python", script1_path]
subprocess.run(["python", "-m", "api-flask.py"])

# Exécution du deuxième script
subprocess.run(["python", "-m", "streamlit", "run", "app-streamlit.py"])
