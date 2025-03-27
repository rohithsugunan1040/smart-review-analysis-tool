import google.generativeai as genai
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(parent_dir)

import creds

genai.configure(api_key=creds.api_key)
# model = genai.GenerativeModel('gemini-1.5-pro-latest')
model = genai.GenerativeModel('gemini-2.0-flash-lite')

def get_response(query,review):
    prompt = f"Based on this review answer the following question. Answer doesnot exceed more than 60 words\nThe review is \n{review} and the question is \n{query}"
    response = model.generate_content(prompt)
    answer =  response.text
    return answer