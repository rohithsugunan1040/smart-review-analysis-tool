import google.generativeai as genai
from .. creds import api_key as key

# genai.configure(api_key="AIzaSyA8PFDBQxqRVGhpAyYQs11dC9YT4STV7Z0")
genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-1.5-pro-latest')
model = genai.GenerativeModel('gemini-2.0-flash-lite')

def get_response(query,review):
    prompt = f"Based on this review answer the following question. Answer doesnot exceed more than 60 words\nThe review is \n{review} and the question is \n{query}"
    response = model.generate_content(prompt)
    answer =  response.text
    return answer