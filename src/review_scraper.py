import requests
from bs4 import BeautifulSoup

def fetch_reviews(product_link):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    try:
        response = requests.get(product_link, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch reviews: {e}")

    soup = BeautifulSoup(response.content, 'html.parser')
    reviews = [review.text.strip() for review in soup.find_all('span', {'data-hook': 'review-body'})]
    
    # Debugging: Print the fetched reviews
    print(f"Fetched {len(reviews)} reviews")
    for review in reviews:
        print(review)
    
    # For testing purposes, return a list of dummy reviews if no reviews are found
    if not reviews:
        print("No reviews were found!!")
        reviews = [
            "I had a bad experience with this product.",
            "It's okay, not the best but not the worst.",
            "Absolutely love it! Highly recommend.",
            "Terrible quality, do not buy."
        ]
    
    return reviews