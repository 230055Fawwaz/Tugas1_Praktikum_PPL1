import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        # Reset state
        import app as app_module
        app_module.todos.clear()
        app_module.next_id = 1
        yield client


def test_health_check(client):
    res = client.get("/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "success"


def test_get_todos_empty(client):
    res = client.get("/todos")
    assert res.status_code == 200
    assert res.get_json()["data"] == []


def test_create_todo(client):
    res = client.post("/todos", json={"title": "Belajar Flask", "description": "Bikin API"})
    assert res.status_code == 201
    data = res.get_json()
    assert data["data"]["title"] == "Belajar Flask"
    assert data["data"]["completed"] == False


def test_create_todo_missing_title(client):
    res = client.post("/todos", json={"description": "no title"})
    assert res.status_code == 400


def test_get_todo_by_id(client):
    client.post("/todos", json={"title": "Test"})
    res = client.get("/todos/1")
    assert res.status_code == 200
    assert res.get_json()["data"]["id"] == 1


def test_get_todo_not_found(client):
    res = client.get("/todos/999")
    assert res.status_code == 404


def test_update_todo(client):
    client.post("/todos", json={"title": "Old Title"})
    res = client.put("/todos/1", json={"title": "New Title", "completed": True})
    assert res.status_code == 200
    data = res.get_json()
    assert data["data"]["title"] == "New Title"
    assert data["data"]["completed"] == True


def test_delete_todo(client):
    client.post("/todos", json={"title": "Delete me"})
    res = client.delete("/todos/1")
    assert res.status_code == 200
    # Verify gone
    res2 = client.get("/todos/1")
    assert res2.status_code == 404
