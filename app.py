import streamlit as st
from src.review_summarizer import summarize_reviews
from src.review_scraper import fetch_reviews
from src.data_processing import clean_reviews
# from src.sentiment_analysis import analyze_sentiment
# temp change

from src.sentiment_analysis_legacy import analyze_sentiment

# temp change end
from src.charts import create_pie_chart
from src.charts import keyword_analysis
from src.chat import get_response

import re


def chat_sidebar():


    def boldify(text):
        """Convert **text** to bold for Streamlit Markdown."""
        return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    def clear_text():
        st.session_state.user_input = st.session_state.chat_input_sidebar
        st.session_state.chat_input_sidebar = ""

        if 'last_message' not in st.session_state:
            st.session_state.last_message = ""

        user_input = st.session_state.user_input
        if user_input != st.session_state.last_message:
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.last_message = user_input
        
        # Simulated bot response
        bot_response = f"{get_response(user_input,st.session_state.cleaned_reviews)}"
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.session_state.enter_clicked = True

    with st.sidebar:
        st.header("💬 Chat")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Custom CSS for chat message alignment and visibility
        st.markdown(
            """
            <style>
                .user-message { 
                    text-align: right; 
                    background-color: #A7E1A7; /* Soft green */
                    color: black;
                    padding: 10px; 
                    border-radius: 10px;
                    display: inline-block;
                    max-width: 80%;
                    border: 1px solid #4CAF50;
                }
                .bot-message {
                    text-align: left;
                    background-color: #F1F1F1; /* Soft gray */
                    color: black;
                    padding: 10px; 
                    border-radius: 10px;
                    display: inline-block;
                    max-width: 80%;
                    border: 1px solid #888;
                }
                .message-container {
                    display: flex;
                    width: 100%;
                    margin: 5px 0;
                }
                .user-container {
                    justify-content: flex-end;
                }
                .bot-container {
                    justify-content: flex-start;
                }
            </style>
            """, 
            unsafe_allow_html=True
        )

        # Display chat messages
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"""
                <div class="message-container user-container">
                    <div class="user-message">{msg["content"]}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="message-container bot-container">
                    <div class="bot-message">{boldify(msg["content"])}</div>
                </div>
                """, unsafe_allow_html=True)

        # User input field
        st.text_input("Type your message:", key="chat_input_sidebar",on_change=clear_text)
        user_input = st.session_state.user_input
        
        st.session_state.button_clicked = False

        if st.button("Send", key="chat_send_sidebar") and user_input:
            if not st.session_state.enter_clicked:
                st.session_state.messages.append({"role": "user", "content": user_input})
               
                # Simulated bot response
                bot_response = f"{get_response(user_input,st.session_state.cleaned_reviews)}"
                st.session_state.messages.append({"role": "assistant", "content": bot_response})

            # Clear input field correctly
            

            st.rerun()


def main():
    st.title("Smart Review Analysis Tool")

    product_link = st.text_input("Enter the product link:")

    if "reviews" not in st.session_state:
        st.session_state.reviews = None
        st.session_state.product_name = None
        st.session_state.cleaned_reviews = None
        st.session_state.sentiments = None
        st.session_state.summary = None
        st.session_state.show_chat = False  # To handle chat visibility

    if st.button("Analyze Reviews"):
        st.session_state.new_link = True
        with st.spinner("Fetching reviews..."):
            reviews,product_name = fetch_reviews(product_link)
            if reviews == 0:
                return
            st.session_state.reviews = reviews
            st.session_state.product_name = product_name
        
        with st.spinner("Cleaning reviews..."):
            st.session_state.cleaned_reviews = clean_reviews(st.session_state.reviews)
        
        with st.spinner("Analyzing sentiment..."):
            st.session_state.sentiments = analyze_sentiment(st.session_state.cleaned_reviews)
        
        with st.spinner("Summarizing reviews..."):
            st.session_state.summary = summarize_reviews(st.session_state.cleaned_reviews)

        st.session_state.show_chat = False  # Reset chat visibility after analysis
        st.success("Analysis complete!")

    # Display results only if reviews exist
    if st.session_state.reviews:
        st.header(st.session_state.product_name)
        st.subheader("Sentiment Analysis Results")
        create_pie_chart(st.session_state.sentiments)
        st.text("")
        st.subheader("Common keywords")
       
        keyword_analysis(st.session_state.reviews)
        st.text("")
        st.subheader("Review Summary")
        st.text("")
        st.write(st.session_state.summary)

        if "show_chat" not in st.session_state:
            st.session_state.show_chat = False

        if st.session_state.show_chat:
            chat_sidebar()


if __name__ == "__main__":
    main()