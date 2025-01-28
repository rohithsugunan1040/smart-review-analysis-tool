import matplotlib.pyplot as plt
import streamlit as st

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
    
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.setp(autotexts, size=10, weight="bold")
    ax1.set_title('Sentiment Analysis Results', color='black', fontsize=14)
    
    st.pyplot(fig1)
