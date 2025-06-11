import os
import streamlit as st
import google.generativeai as genai
from apikey import gemini_api_key  # Make sure this contains your Gemini API key

# Set up Gemini API key
genai.configure(api_key=gemini_api_key)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Streamlit UI
st.title('Medium Article Generator (Gemini)')
topic = st.text_input('Input your topic of interest')

if topic:
    with st.spinner("Generating article..."):
        response = model.generate_content(f"Write a Medium-style article about: {topic}")
        st.write(response.text)
