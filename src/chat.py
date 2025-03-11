import google.generativeai as genai
genai.configure(api_key="AIzaSyA8PFDBQxqRVGhpAyYQs11dC9YT4STV7Z0")
model = genai.GenerativeModel('gemini-1.5-pro-latest')

def get_response(query,review):
    prompt = f"Based on this review answer the following question. Answer doesnot exceed more than 60 words\nThe review is \n{review} and the question is \n{query}"
    response = model.generate_content(prompt)
    answer =  response.text
    return answer