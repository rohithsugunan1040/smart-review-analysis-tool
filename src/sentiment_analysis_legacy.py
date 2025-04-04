import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon
nltk.download('vader_lexicon')

def analyze_sentiment(reviews):
    sia = SentimentIntensityAnalyzer()
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
    for review in reviews:
        result = sia.polarity_scores(review)
        # Debugging: Print the review and its sentiment result
        # print(f"Review: {review}\nResult: {result}\n")
        if result['compound'] >= 0.05:
            sentiments['positive'] += 1
        elif result['compound'] <= -0.05:
            sentiments['negative'] += 1
        else:
            sentiments['neutral'] += 1
    print("\n\nSENTIMENTSS")
    print(sentiments)
    return sentiments