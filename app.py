import streamlit as st
from src.review_summarizer import summarize_reviews
from src.review_scraper import fetch_reviews
from src.data_processing import clean_reviews
# from src.sentiment_analysis import analyze_sentiment
# temp change

from src.sentiment_analysis_legacy import analyze_sentiment

# temp change end
from src.charts import create_pie_chart
from src.charts import create_bar_chart

def main():
    
   
    st.title("Smart Review Analysis Tool")

    product_link = st.text_input("Enter the product link:")

    if st.button("Analyze Reviews"):
        with st.spinner("Fetching reviews..."):
            reviews = fetch_reviews(product_link)
            if reviews == 0:
                return
        
        with st.spinner("Cleaning reviews..."):
            cleaned_reviews = clean_reviews(reviews)
            
        
        with st.spinner("Analyzing sentiment..."):
            sentiments = analyze_sentiment(cleaned_reviews)
        
        st.success("Analysis complete!")
        
        st.subheader("Sentiment Analysis Results")
        create_pie_chart(sentiments)
        create_bar_chart(cleaned_reviews)
        st.text(summarize_reviews(cleaned_reviews))

if __name__ == "__main__":
    main()