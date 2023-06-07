from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from scipy.special import softmax
import streamlit as st
import torch

# Streamlit initialization
@st.cache_resource()
def get_model():
    tokenizer = AutoTokenizer.from_pretrained(f"cardiffnlp/twitter-roberta-base-sentiment")
    model = AutoModelForSequenceClassification.from_pretrained(f"liamarguedas/SentimentReview")     
    return tokenizer, model # Get model and tokenizer

# Assign model and tokenizer
tokenizer, model = get_model()

# Create pipeline
PipeReturn = pipeline("sentiment-analysis", model = model, tokenizer = tokenizer)

# Function to return value from pipeline
def predict(text: str):
    try: 
        sentiment = PipeReturn(text)[0]
        for key, value in sentiment.items():
            if sentiment[key] == 'LABEL_0':
                return 'Negative'
            elif sentiment[key] == 'LABEL_2':  
                return 'Positive'
        return 'Neutro'
    except RuntimeError:
        return "Unclassified"

# Get user input and request
user_input, button = str(st.text_area('Enter review to analyze')), st.button("Analyze sentiment")

# Sent predictions to the user
if user_input and button:
    st.write(predict(user_input))