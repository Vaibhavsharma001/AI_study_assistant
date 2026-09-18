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

# Page configuration
st.set_page_config(
    page_title = "AI Study Assistant",
    page_icon = "📚",
    layout = "wide"
)

st.title("📚 AI Study Assistant")
st.subheader("Learn smarter with AI — explanations, notes, MCQs and quizzes.")

# Sidebar
st.sidebar.header("⚙️ Study Settings")

topic = st.sidebar.text_input(
      "Enter your topic",
      placeholder="e.g. Python OOP"
)

difficulty = st.sidebar.selectbox(
    "Diffficlty",
    ["Beginner", "Intermediate", "Advanced"]
)

# Main tabs

tab1,tab2,tab3,tab4 = st.tabs(
    ["📖 Explain", "📝 Notes", "❓ MCQs", "🎯 Quiz"]
)

def generate_response(prompt):
    """send prompt to gemini and return the resopnse."""
    
    try:
        response = client.models.generate_content(
            model = "gemini-3.7-flash",
            contents = prompt
        )
        
        return response.text
    
    except Exception as e:
        return f"Error:{e}"
    
    
with tab1:
    st.header("📖 Topic Explanation")

    if not topic:
        st.info("Enter a topic from the sidebar.")

    else:
        if st.button("Explain Topic", key="explain"):

            prompt = f"""
You are an expert teacher.

Explain the following topic to a student.

Topic: {topic}
Difficulty: {difficulty}

Follow this structure:

1. Simple definition
2. Why it is important
3. Main concepts
4. Easy examples
5. Real-world example
6. Common mistakes
7. Short summary

Use simple language and make the explanation suitable
for a college student.
"""

            with st.spinner("Preparing explanation..."):
                result = generate_response(prompt)

            st.markdown(result)