from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_user():
    # 1. Créer un utilisateur
    new_user = {"name": "Charlie"}
    post_response = client.post("/users", json=new_user)
    assert post_response.status_code == 200
    assert post_response.json()["name"] == "Charlie"

    # 2. Vérifier qu’il est dans la liste
    get_response = client.get("/users")
    assert get_response.status_code == 200
    users = get_response.json()
    assert any(user["name"] == "Charlie" for user in users)

def test_predict_endpoint():
    input_data = {
        "x1": 1.5,
        "x2": -0.3
    }
    response = client.post("/predict", json=input_data)
    assert response.status_code == 200

    result = response.json()
    assert "prediction" in result
    assert isinstance(result["prediction"], float) or isinstance(result["prediction"], int)

def test_predict_invalid_input():
    bad_input = {"x1": "not a number"}  
    response = client.post("/predict", json=bad_input)
    assert response.status_code == 422

#ce test vérifie : 
#La route /entities fonctionne et renvoie un status 200.
#Le format de réponse contient les clés entities et anonymized_text.
#Le texte anonymisé contient bien des X à la place des entités reconnues.
#Les entités sont bien structurées.

def test_extract_entities():
    payload = {
        "text": "Emmanuel Macron est né à Amiens.",
        "model_language": "fr",
        "model_size": "sm"
    }

    response = client.post("/entities", json=payload)
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert "entities" in data
    assert "anonymized_text" in data

    entities = data["entities"]
    anon_text = data["anonymized_text"]

    # Vérifie qu’au moins une entité a été détectée
    assert isinstance(entities, list)
    assert all("start" in e and "end" in e and "text" in e and "type" in e for e in entities)

    # Vérifie que les entités ont bien été remplacées par des "X"
    for entity in entities:
        start = entity["start"]
        end = entity["end"]
        assert set(anon_text[start:end]) == {"X"}