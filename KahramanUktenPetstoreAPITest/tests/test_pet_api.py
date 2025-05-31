import requests

BASE_URL = "https://petstore.swagger.io/v2"
PET_ID = 999999  # Sabit ID

def create_pet():
    data = {
        "id": PET_ID,
        "name": "TestPet",
        "photoUrls": ["https://example.com/photo.jpg"]
    }
    requests.post(f"{BASE_URL}/pet", json=data)

def delete_pet():
    requests.delete(f"{BASE_URL}/pet/{PET_ID}")

def test_create_pet_positive():
    delete_pet()  # varsa sil
    response = requests.post(f"{BASE_URL}/pet", json={
        "id": PET_ID,
        "name": "TestPet",
        "photoUrls": ["https://example.com/photo.jpg"]
    })
    assert response.status_code == 200

def test_create_pet_negative():
    data = {"photoUrls": ["string"]}
    response = requests.post(f"{BASE_URL}/pet", json=data)
    assert response.status_code == 200  # Swagger gevşek davranıyor

def test_get_pet_by_id_positive():
    create_pet()
    response = requests.get(f"{BASE_URL}/pet/{PET_ID}")
    assert response.status_code == 200
    assert response.json()["id"] == PET_ID

def test_get_pet_by_id_negative():
    response = requests.get(f"{BASE_URL}/pet/-1")
    assert response.status_code == 404

def test_update_pet_positive():
    create_pet()
    data = {
        "id": PET_ID,
        "name": "UpdatedPet",
        "photoUrls": ["https://example.com/photo2.jpg"]
    }
    response = requests.put(f"{BASE_URL}/pet", json=data)
    assert response.status_code == 200

def test_update_pet_negative():
    response = requests.put(f"{BASE_URL}/pet", json={})
    assert response.status_code == 200  # Swagger'da 200 dönüyor

def test_delete_pet_positive():
    create_pet()
    response = requests.delete(f"{BASE_URL}/pet/{PET_ID}")
    assert response.status_code == 200

def test_delete_pet_negative():
    response = requests.delete(f"{BASE_URL}/pet/-1")
    assert response.status_code == 404
