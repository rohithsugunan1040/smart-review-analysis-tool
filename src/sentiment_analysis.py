from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(reviews):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
    
    for review in reviews:
        score = analyzer.polarity_scores(review)
        print(f"Review: {review}\nScore: {score}\n")  # Debugging: Print the review and its sentiment score
        if score['compound'] >= 0.05:
            sentiments['positive'] += 1
        elif score['compound'] <= -0.05:
            sentiments['negative'] += 1
        else:
            sentiments['neutral'] += 1
    
    return sentiments