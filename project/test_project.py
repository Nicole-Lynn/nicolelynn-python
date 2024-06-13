from project import available_genres, get_genre_by_index, get_genre_by_name
import requests
import pytest


def test_available_genres(monkeypatch):
    # Mock the API response
    mock_response = {
        "genres": [
            {"id": 1, "name": "Action"},
            {"id": 2, "name": "Adventure"},
            {"id": 3, "name": "Animation"}
        ]
    }

     # Define a mock Response object
    class MockResponse:
        def json(self):
            return mock_response

    # Define a mock function for requests.get
    def mock_get(url):
        return MockResponse()

    # Replace the requests.get function with the mock function
    monkeypatch.setattr(requests, "get", mock_get)

    # Call the available_genres function
    genres = available_genres()

    # Assert the result
    assert genres == ['Action', 'Adventure', 'Animation']



def test_get_genre_by_index():
    assert get_genre_by_index("3") == "Confirmed! You chose 3 the genre, ANIMATION."
    assert get_genre_by_index("9") == "Confirmed! You chose 9 the genre, FANTASY."
    with pytest.raises(Exception):
        get_genre_by_index("20")


def test_get_genre_by_name():
    assert get_genre_by_name("romance") == "Confirmed! You chose the genre, ROMANCE."
    assert get_genre_by_name("tv movie") == "Confirmed! You chose the genre, TV MOVIE."

