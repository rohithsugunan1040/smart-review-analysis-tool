import pytest
from src.review_scraper import fetch_reviews

def test_fetch_reviews(mocker):
    # Mock the requests.get method to simulate a response
    mock_response = mocker.Mock()
    mock_response.content = '<html><body><span data-hook="review-body">Great product!</span></body></html>'
    mocker.patch('requests.get', return_value=mock_response)

    # Call the function with a sample product link
    reviews = fetch_reviews('http://example.com/product')

    # Assert that the reviews are as expected
    assert reviews == ['Great product!']  # Adjust based on actual scraping logic

def test_fetch_reviews_invalid_url(mocker):
    # Mock the requests.get method to simulate a failed response
    mock_response = mocker.Mock()
    mock_response.raise_for_status.side_effect = Exception("Invalid URL")
    mocker.patch('requests.get', return_value=mock_response)

    # Call the function with an invalid product link and assert it handles the error
    with pytest.raises(Exception):
        fetch_reviews('http://invalid-url.com')