import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import nltk
from rake_nltk import Rake
import os

from collections import Counter

try:
    nltk.data.find('corpora/stopwords')
    print("Stopword resource already available")
except LookupError:
    print("Downloading stopword resource")
    nltk.download('stopwords')
nltk.download('punkt')

# Find NLTK data paths
nltk_data_paths = nltk.data.path

# Check each directory for 'punkt_tab'
for path in nltk_data_paths:
    punkt_path = os.path.join(path, 'tokenizers', 'punkt')
    if os.path.exists(punkt_path):
        files = os.listdir(punkt_path)
        if 'punkt_tab.py' in files:
            print(f"'punkt_tab.py' found in: {punkt_path}")
        else:
            print(f"'punkt_tab.py' not found in: {punkt_path}")
            nltk.download('punkt_tab')

def create_pie_chart(sentiments):
    labels = sentiments.keys()
    sizes = sentiments.values()
    colors = ['green', 'grey', 'red']
    explode = (0.1, 0, 0)  
    
    fig1, ax1 = plt.subplots()
    wedges, texts, autotexts = ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                                       shadow=True, startangle=90, textprops=dict(color="w"))
    
    # Improve the appearance of the chart
    for text in texts:
        text.set_color('black')
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)
    
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn=' as a circle.
    plt.setp(autotexts, size=10, weight="bold")
    ax1.set_title('Sentiment Analysis Results', color='black', fontsize=14)
    
    st.pyplot(fig1)


def create_bar_chart(cleaned_reviews):
    r = Rake(min_length=2, max_length=3)
    all_keywords = []
    for review in cleaned_reviews:
        r.extract_keywords_from_text(review)
        all_keywords.extend(r.get_ranked_phrases())
    
    keyword_counts = Counter(all_keywords)


    keywords = []
    counts = []
    for keyword,count in keyword_counts.items():
        if count > 4:
            keywords.append(keyword)
            counts.append(count)


    df = pd.DataFrame({
        'keyword' : keywords,
        'count' : counts
    })

    fig = px.bar(df,x='keyword',y='count',labels={
        'keyword':'keywords','count':'keyword count'
    },title='Most occured Keywords')

    st.plotly_chart(fig)

