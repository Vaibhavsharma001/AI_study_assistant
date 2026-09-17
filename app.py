import streamlit as st 
from google import genai 
from dotenv import load_dotenv 
import os 


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


if not api_key:
    st.error("GEMINI_API_KEY is missing. Please add it to your .env file.")
    st.stop()
    
client = genai.Client(api_key = api_key)

    
st.set_page_config(
    page_title = "AI Study Assistant",
    page_icon = "📚",
    layout = "wide"
)

st.title("📚 AI Study Assistant")
st.subheader("Learn smarter with AI — explanations, notes, MCQs and quizzes.")