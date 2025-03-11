# from transformers import pipeline
import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key="AIzaSyA8PFDBQxqRVGhpAyYQs11dC9YT4STV7Z0")

model = genai.GenerativeModel('gemini-1.5-pro-latest')

def summarize_reviews(reviews):
    # Initialize Gemini model


# # Example: Product reviews to summarize
    # reviews = """
    # The sound quality is amazing. I love the battery life, lasts all day. The design feels premium.
    # However, the connectivity drops sometimes. Overall, great value for money!
    # """

    # Prompt Gemini for summarization
    prompt = f"Summarize the following customer reviews into a short, clear summary:\n\n{reviews}"
    response = model.generate_content(prompt)

    prompt = f"Give some sugessions to improve the quality of product based on the review:\n\n{reviews}"
    print(model.generate_content(prompt).text)

    # Get the summarized text
    summary = response.text
    return summary
