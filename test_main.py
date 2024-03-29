from fastapi.testclient import TestClient
from main import app
import datetime
from dateutil import parser

client = TestClient(app)

def test_read_time():
    response = client.get("/time")
    data = response.json()
    
    assert response.status_code == 200
    assert "current_time" in data
    # Ensure the returned time is a valid datetime string
    try:
        parsed_time = parser.parse(data["current_time"])
        assert isinstance(parsed_time, datetime.datetime)
    except ValueError:
        assert False, "current_time is not a valid datetime"
