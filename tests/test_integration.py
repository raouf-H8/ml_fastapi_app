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