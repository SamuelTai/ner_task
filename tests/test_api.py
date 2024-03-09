from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_extract_dates_from_text():
    response = client.post(
        "/extract_dates/",
        json={
            "text": "The policy provides cover from 31st June 2019"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "dates" in data
    assert "message" in data
