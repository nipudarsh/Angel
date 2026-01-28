"""Integration tests for the health endpoint."""
from fastapi.testclient import TestClient

from angel_web.app import create_app


def test_health_endpoint() -> None:
    app = create_app()
    client = TestClient(app)
    response = client.get("/api/system/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
