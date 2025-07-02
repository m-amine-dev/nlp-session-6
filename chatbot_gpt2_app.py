import streamlit as st
from transformers import pipeline

# Title
st.title("🗨️ LLM Chatbot using Hugging Face & Streamlit")

# Initialize QA pipeline (LLM) from Hugging Face
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# Chat input
user_input = st.text_input("You:", "")

if user_input:
    # Generate response
    response = generator(user_input, max_length=100, num_return_sequences=1)[0]["generated_text"]
    
    # Show response
    st.markdown(f"**Bot:** {response}")

