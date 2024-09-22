import streamlit as st
from transformers import pipeline

# Title and description of the app
st.title("AI Sentiment Analysis App")
st.write("Enter some text and let the AI analyze the sentiment!")

# Load a pre-trained model for sentiment analysis
sentiment_pipeline = pipeline("sentiment-analysis")

# Text input box for user input
user_input = st.text_area("Enter text here:")

# Run the sentiment analysis when the user submits text
if st.button("Analyze Sentiment"):
    if user_input:
        # Perform sentiment analysis
        results = sentiment_pipeline(user_input)
        # Display the result
        for result in results:
            st.write(f"**Sentiment:** {result['label']}")
            st.write(f"**Confidence:** {round(result['score'], 4)}")
    else:
        st.write("Please enter some text to analyze.")
