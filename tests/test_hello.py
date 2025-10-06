from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
    
def test_blogs():
    response = client.get("/blogs")
    assert response.status_code == 200
    assert response.json() == {"message": "List of blogs"}
    
def test_abourt():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {"message": "About page"}