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

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from io import BytesIO
import matplotlib.pyplot as plt




def generate_sentiment_chart():
    """Generate a pie chart of sentiment scores and return as BytesIO buffer."""
    fig, ax = plt.subplots()
    sentiments = st.session_state.sentiments
    labels = sentiments.keys()
    sizes = sentiments.values()
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis('equal')
    
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    plt.close()
    return img_buffer


def generate_pdf():
    """Generate a PDF report with sentiment scores, keyword analysis, and summary."""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()
    
    # Title
    elements.append(Paragraph("<b>Smart Review Analysis Report</b>", styles["Title"]))
    elements.append(Spacer(1, 12))
    
    # Product Information
    product_name = st.session_state.get("product_name", "N/A")
    elements.append(Paragraph(f"<b>Product Name:</b> {product_name}", styles["Normal"]))
    elements.append(Spacer(1, 12))
    
    # Sentiment Score Table
    if st.session_state.sentiments:
        data = [["Sentiment", "Percentage"]] + [[k, f"{v}%"] for k, v in st.session_state.pie_data.items()]
        table = Table(data, colWidths=[150, 100])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(table)
        elements.append(Spacer(1, 12))
    
    # Keyword Analysis
    # if "top_keywords" in st.session_state and st.session_state.top_keywords:
    #     elements.append(Paragraph("<b>Top Keywords:</b>", styles["Normal"]))
    #     keyword_data = [[kw] for kw in st.session_state.top_keywords]
    #     keyword_table = Table(keyword_data)
    #     keyword_table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    #     elements.append(keyword_table)
    #     elements.append(Spacer(1, 12))
    # else:
    #     elements.append(Paragraph("<b>Top Keywords:</b> No keywords extracted.", styles["Normal"]))
    #     elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Top Keywords:</b>", styles["Normal"]))
    keyword_data = [[kw] for kw in st.session_state.top_keywords]
    keyword_table = Table(keyword_data)
    keyword_table.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(keyword_table)
    elements.append(Spacer(1, 12))
    
    # Review Summary
    if "summary" in st.session_state:
        elements.append(Paragraph("<b>Review Summary:</b>", styles["Normal"]))
        elements.append(Paragraph(st.session_state.summary, styles["Normal"]))
        elements.append(Spacer(1, 12))
    
    # Sentiment Chart
    img_buffer = generate_sentiment_chart()
    img = Image(img_buffer, width=300, height=200)
    elements.append(img)
    
    # Conclusion
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Conclusion:</b> The product has received mostly positive reviews with minor concerns.", styles["Normal"]))
    
    # Build the PDF
    doc.build(elements)
    buffer.seek(0)
    return buffer

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
        st.session_state.pie_data = None
        st.session_state.top_keywords = None

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

        # if st.session_state.show_chat:
        #     chat_sidebar()

    if st.session_state.reviews:
        if st.button("Download Report"):
            pdf_data = generate_pdf()
            st.download_button(label="Download PDF", data=pdf_data, file_name="review_report.pdf", mime="application/pdf")

if __name__ == "__main__":
    main()