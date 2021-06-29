from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_index() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '"A Simple and Basic MDL Scraper API"'  # this is weird


def test_sample_drama() -> None:
    response = client.get("/id/58953-mouse")  # real id
    assert response.status_code == 200
    assert response.json()["data"]["title"] == "Mouse"


def test_unknown_drama() -> None:
    response = client.get("/id/alkdjaklsdjklasd")
    assert response.status_code == 404
    assert response.json() == {
        "error": True,
        "code": 404,
        "description": "404 Not Found",
    }


def test_sample_people() -> None:
    response = client.get("/people/4444-kim-jong-min")
    assert response.status_code == 200
    assert response.json()["data"]["name"] == "Kim Jong Min"


def test_unknown_people() -> None:
    response = client.get("/people/asdasdadadasdadasdasdaswerwer")
    assert response.status_code == 404
    assert response.json() == {
        "error": True,
        "code": 404,
        "description": "404 Not Found",
    }


def test_unknown_endpoint() -> None:
    response = client.get("/unknown")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
