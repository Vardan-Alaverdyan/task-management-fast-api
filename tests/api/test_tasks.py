import pytest


def test_create_task(client):
    task_data = {
        "title": "Test Task",
        "description": "Test Description",
        "priority": 1
    }
    response = client.post("/api/v1/tasks/", json=task_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["description"] == task_data["description"]
    assert data["status"] == "pending"


def test_list_tasks(client):
    # Create a task first
    task_data = {
        "title": "Test Task",
        "description": "Test Description",
        "priority": 1
    }
    client.post("/api/v1/tasks/", json=task_data)
    
    # List tasks
    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["title"] == task_data["title"]


def test_get_task(client):
    # Create a task first
    task_data = {
        "title": "Test Task",
        "description": "Test Description",
        "priority": 1
    }
    create_response = client.post("/api/v1/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Get the task
    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == task_data["title"]


def test_update_task(client):
    # Create a task first
    task_data = {
        "title": "Test Task",
        "description": "Test Description",
        "priority": 1
    }
    create_response = client.post("/api/v1/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Update the task
    update_data = {
        "title": "Updated Task",
        "status": "in_progress"
    }
    response = client.put(f"/api/v1/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_data["title"]
    assert data["status"] == update_data["status"]


def test_delete_task(client):
    # Create a task first
    task_data = {
        "title": "Test Task",
        "description": "Test Description",
        "priority": 1
    }
    create_response = client.post("/api/v1/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Delete the task
    response = client.delete(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200
    
    # Verify task is deleted
    get_response = client.get(f"/api/v1/tasks/{task_id}")
    assert get_response.status_code == 404


def test_process_task(client):
    # Create a task first
    task_data = {
        "title": "Test Task",
        "description": "Test Description",
        "priority": 1
    }
    create_response = client.post("/api/v1/tasks/", json=task_data)
    task_id = create_response.json()["id"]
    
    # Start processing
    response = client.post(f"/api/v1/tasks/{task_id}/process")
    assert response.status_code == 200
    data = response.json()
    assert "processing started" in data["message"]
