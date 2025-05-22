def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Task Manager API" in response.json()["message"]


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
