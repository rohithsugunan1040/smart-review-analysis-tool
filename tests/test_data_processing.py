def test_clean_reviews():
    from src.data_processing import clean_reviews

    reviews = [
        "Great product!",
        "Great product!",
        "Not bad.",
        "Not bad.",
        "Terrible experience."
    ]
    
    expected_output = [
        "Great product!",
        "Not bad.",
        "Terrible experience."
    ]
    
    assert clean_reviews(reviews) == expected_output

def test_clean_reviews_empty():
    from src.data_processing import clean_reviews

    reviews = []
    
    expected_output = []
    
    assert clean_reviews(reviews) == expected_output

def test_clean_reviews_no_duplicates():
    from src.data_processing import clean_reviews

    reviews = [
        "Amazing!",
        "Loved it!",
        "Would buy again."
    ]
    
    expected_output = [
        "Amazing!",
        "Loved it!",
        "Would buy again."
    ]
    
    assert clean_reviews(reviews) == expected_output