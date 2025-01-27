def clean_reviews(reviews):
    """
    Preprocesses the review text by removing duplicates and normalizing the text.
    
    Args:
        reviews (list of str): A list of review texts.
        
    Returns:
        list of str: A list of cleaned and normalized review texts.
    """
    # Remove duplicates
    unique_reviews = list(set(reviews))
    
    # Normalize the text (e.g., lowercasing)
    cleaned_reviews = [review.lower().strip() for review in unique_reviews]
    
    return cleaned_reviews