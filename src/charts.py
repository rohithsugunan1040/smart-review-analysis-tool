import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import nltk
from rake_nltk import Rake
import os
import re

from collections import Counter


from  pages.Chat import model

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

st.cache_resource
def keyword_analysis(review):
    if "response" not in st.session_state or st.session_state.new_link:
        # prompt = f"{review}\n\nBased on the above review give the most frequently mentioned keywords which are useful for analysis of product along with their sentiment possitivity precent eg: 55% possitive\nkeyword examples are 'Camera quality','Battery Life' etc not include common keywords like 'good','bad','nice' etc. Keyword should be meaningful.\n\nGive each keyword as 'Keyword-string:' followed by the extracted keyword and in next line 'possitivity:' followed by corresponding positivity percentage."
        prompt = f"{review}\n\nBased on the above review give the most frequently mentioned keywords which are useful for analysis of product along with their sentiment possitivity precent eg: 55% possitive\nkeyword examples are 'Camera quality','Battery Life' etc not include common keywords like 'good','bad','nice' etc. Keyword should be meaningful.\n\nGive each keyword as 'KW:' followed by the extracted keyword and in next line 'possitivity:' followed by corresponding positivity percentage. without any formatting or decoration"
        response = model.generate_content(prompt)
        response =  response.text
        print("RESPONSE\n\n",response)
        st.session_state.response = response
        st.session_state.new_link = False

    # pattern = r"\*\*\s*Keyword:\s*(.+?)\s*\*\*[\s\S]*?Positivity Percentage:\s*(?:Approximately\s*)?(\d+)%"
    # pattern = r"[Kk]eyword[:]*\s*(.*?)\s*(?:\n|\r|\*)[\s\S]*?[Pp]ositivity(?: Percentage)*[:]*\s*(?:Approximately\s*)*(\d+)%"
    # pattern = r"\*\*Keyword:\*\*\s*(.*?)\n\*\*Positivity:\*\*\s*(\d+)%"
    # pattern = r"[kk]eyword-string:\s*(.*?)\s*\n\s*[pP]ossitivity:\s*(\d+)%"
    pattern = r"KW:\s*(.+?)\s*\n\s*possitivity:\s*(\d+)%?"

    # Find all matches
    matches = re.findall(pattern, st.session_state.response)
    sentiments = {match[0]: int(match[1]) for match in matches}

    keywords = list(sentiments.keys())
    print("KEYWORDS\n\n",keywords)

    # Display keywords as inline tags
    keyword_html = "".join([f"<span style='display: inline-block; background-color: #e8eaed; padding: 6px 12px; border-radius: 12px; margin: 4px; font-size: 14px;'>{keyword}</span>" for keyword in keywords])
    st.markdown(f"<div style='display: flex; flex-wrap: wrap; color:black'>{keyword_html}</div>", unsafe_allow_html=True)

    st.markdown("---")

    # Display sentiment bars
    for feature, score in sentiments.items():
        st.write(f"**{feature}**  {score}% positive")
        st.progress(score / 100)