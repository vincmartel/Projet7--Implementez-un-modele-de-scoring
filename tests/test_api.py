import json
import pytest
from app import app  # Replace with the actual name of your Flask app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_prediction_response(client):
    # Test qui vérifie si l'API retourne les paramètres 'pred' et 'decision'
    mock_data = {
        'Identifiant du prêt': 100002  # Replace with a valid loan ID
    }

    # Send a POST request to the /prediction endpoint
    response = client.post('/prediction', json=mock_data)
    data = json.loads(response.data.decode('utf-8'))

    # Check if the response contains the expected keys
    assert 'pred' in data
    assert 'decision' in data



def test_prediction_pred_decision(client):
    # Test qui vérifie si l'API retourne une valeur de 'pred' comprise entre 0 et 1, et une valeur de décision égale à 'prêt accordé' ou 'prêt refusé'  
    mock_data = {
        'Identifiant du prêt': 100002  # Replace with a valid loan ID
    }
    
    response = client.post('/prediction', json=mock_data)
    data = json.loads(response.data.decode('utf-8'))
    assert (data['pred']>0 and data['pred']<1)
    assert (data['decision']=='prêt accordé' or data['decision']=='prêt refusé')


if __name__ == '__main__':
    pytest.main()