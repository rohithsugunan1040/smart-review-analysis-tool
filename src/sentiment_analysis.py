import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

# Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def analyze_sentiment(reviews):
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
    for review in reviews:
        inputs = tokenizer(review, return_tensors='pt', truncation=True, padding=True, max_length=512)
        outputs = model(**inputs)
        probs = softmax(outputs.logits, dim=1)
        sentiment = torch.argmax(probs).item()

        if sentiment == 4:  # Positive
            sentiments['positive'] += 1
        elif sentiment == 2:  # Neutral
            sentiments['neutral'] += 1
        else:  # Negative
            sentiments['negative'] += 1
    
    return sentiments


