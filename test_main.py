from fastapi.testclient import TestClient
from main import app
import datetime
from dateutil import parser

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    # Assuming the response is text/plain; adjust if it's application/json or another content type
    assert response.text == "Enter /movie/<moviename> to get deatils ----  Enter /time to get time"

def test_get_movie_details():
    # Use a well-known movie title that's likely to exist in the OMDB database
    test_movie_title = "Inception"
    response = client.get(f"/movie/{test_movie_title}")
    data = response.json()
    
    assert response.status_code == 200
    # Check for some expected keys in the response to ensure it's the correct movie data
    # Adjust these keys based on what OMDB actually returns and what you expect
    assert "Title" in data
    assert data["Title"] == test_movie_title
    assert "Year" in data
    assert "Director" in data

def test_read_time():
    response = client.get("/time")
    data = response.json()
    
    assert response.status_code == 200
    assert "current_time" in data
    # Ensure the returned time is a valid datetime string
    try:
        # Parse the datetime string from the response
        parsed_time = parser.parse(data["current_time"])
        # Check if parsed_time is indeed an instance of datetime.datetime
        assert isinstance(parsed_time, datetime.datetime)
    except ValueError:
        # Fail the test if the datetime string is invalid
        assert False, "current_time is not a valid datetime"
