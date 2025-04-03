import streamlit as st
import google.generativeai as genai
import re


# genai.configure(api_key="AIzaSyA8PFDBQxqRVGhpAyYQs11dC9YT4STV7Z0")
genai.configure(api_key="AIzaSyBZpVsAZpepbFKzLb-g5Ymxuxu3YozaBb8")
# model = genai.GenerativeModel('gemini-1.5-pro-latest')
model = genai.GenerativeModel('gemini-2.0-flash-lite')

def get_response(query,review):
    prompt = f"Based on this review answer the following question. Answer doesnot exceed more than 60 words. If the question is a not related to the review like 'hi' 'how are you' etc then give reply mentioning that you can only give answer to question related to the review.\nThe review is \n{review} and the question is \n{query}"
    response = model.generate_content(prompt)
    answer =  response.text
    return answer



def chat_page():
    st.title("💬 Chat Assistant")

    def boldify(text):
        """Convert **text** to bold for Streamlit Markdown."""
        return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    def clear_text():
        st.session_state.user_input = st.session_state.chat_input
        st.session_state.chat_input = ""

        if 'last_message' not in st.session_state:
            st.session_state.last_message = ""

        user_input = st.session_state.user_input
        if user_input != st.session_state.last_message:
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.last_message = user_input
        
        # Simulated bot response
        bot_response = get_response(user_input, st.session_state.cleaned_reviews)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.session_state.enter_clicked = True

    # Custom CSS for chat formatting
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
                <div class="bot-message">{boldify(msg["content"])} </div>
            </div>
            """, unsafe_allow_html=True)

    # User input field
    st.text_input("Type your message:", key="chat_input", on_change=clear_text)
    user_input = st.session_state.user_input
    
    if st.button("Send") and user_input:
        if not st.session_state.get("enter_clicked", False):
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Simulated bot response
            bot_response = get_response(user_input, st.session_state.cleaned_reviews)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
        st.rerun()

# Run the chat page function
if __name__ == "__main__":
    chat_page()
