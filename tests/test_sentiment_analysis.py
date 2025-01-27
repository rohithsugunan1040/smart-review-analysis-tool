def test_analyze_sentiment():
    from src.sentiment_analysis import analyze_sentiment

    reviews = [
        "I love this product! It's amazing.",
        "This is okay, not great but not bad.",
        "I hate this! It broke after one use."
    ]

    expected_output = {
        'positive': 1,
        'neutral': 1,
        'negative': 1
    }

    assert analyze_sentiment(reviews) == expected_output

def test_analyze_sentiment_empty():
    from src.sentiment_analysis import analyze_sentiment

    reviews = []

    expected_output = {
        'positive': 0,
        'neutral': 0,
        'negative': 0
    }

    assert analyze_sentiment(reviews) == expected_output

def test_analyze_sentiment_mixed():
    from src.sentiment_analysis import analyze_sentiment

    reviews = [
        "Absolutely fantastic!",
        "Not what I expected.",
        "Worst purchase ever.",
        "It's okay, I guess.",
        "I would buy this again."
    ]

    expected_output = {
        'positive': 2,
        'neutral': 1,
        'negative': 2
    }

    assert analyze_sentiment(reviews) == expected_output