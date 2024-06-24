# from fastapi.testclient import TestClient
# from src.main import app  # 假设您的主应用在src/main.py中定义

# client = TestClient(app)

# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}

# def test_create_user():
#     user_data = {"name": "Test User", "email": "test@example.com", "password": "testpassword"}
#     response = client.post("/users/", json=user_data)
#     assert response.status_code == 201
#     assert "id" in response.json()
#     assert response.json()["name"] == user_data["name"]
#     assert response.json()["email"] == user_data["email"]

# def test_read_user():
#     response = client.get("/users/1")
#     assert response.status_code == 200
#     assert "id" in response.json()
#     assert "name" in response.json()
#     assert "email" in response.json()

# def test_update_user():
#     update_data = {"name": "Updated User", "email": "updated@example.com"}
#     response = client.put("/users/1", json=update_data)
#     assert response.status_code == 200
#     assert response.json()["name"] == update_data["name"]
#     assert response.json()["email"] == update_data["email"]

# def test_delete_user():
#     response = client.delete("/users/1")
#     assert response.status_code == 204

# def test_read_nonexistent_user():
#     response = client.get("/users/999")
#     assert response.status_code == 404
#     assert response.json() == {"detail": "User not found"}