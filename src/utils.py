def format_review(review):
    """Format a single review for consistency."""
    return review.strip().lower()

def extract_keywords(text):
    """Extract keywords from the given text."""
    # Placeholder for keyword extraction logic
    return text.split()

def calculate_average_rating(ratings):
    """Calculate the average rating from a list of ratings."""
    if not ratings:
        return 0
    return sum(ratings) / len(ratings)
