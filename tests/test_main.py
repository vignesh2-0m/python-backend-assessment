import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_repo():
    # Create
    response = client.post("/repos/", json={"owner": "octocat", "name": "Hello-World"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Hello-World"
    repo_id = data["id"]

    # Get
    response = client.get(f"/repos/{repo_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == repo_id
    assert data["owner"] == "octocat"

def test_update_repo():
    # First create a repo
    response = client.post("/repos/", json={"owner": "octocat", "name": "Hello-World-2"})
    repo_id = response.json()["id"]

    # Update stars
    response = client.put(f"/repos/{repo_id}", json={"stars": 100})
    assert response.status_code == 200
    data = response.json()
    assert data["stars"] == 100

def test_delete_repo():
    # Create a repo
    response = client.post("/repos/", json={"owner": "octocat", "name": "To-Delete"})
    repo_id = response.json()["id"]

    # Delete
    response = client.delete(f"/repos/{repo_id}")
    assert response.status_code == 204

    # Confirm deletion
    response = client.get(f"/repos/{repo_id}")
    assert response.status_code == 404
