import streamlit as st 
from openai import OpenAI
from dotenv import load_dotenv 
import os 

# Page configuration
st.set_page_config(
    page_title = "AI Study Assistant",
    page_icon = "📚",
    layout = "wide"
)


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


if not api_key:
    st.error("API_KEY is missing. Please add it to your .env file.")
    st.stop()
    
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
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
    "Diffficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

# Main tabs

tab1,tab2,tab3,tab4 = st.tabs(
    ["📖 Explain", "📝 Notes", "❓ MCQs", "🎯 Quiz"]
)

def generate_response(prompt):
    """send prompt to groq and return the resopnse."""
    
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
          messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content
    
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
            
with tab2:
    st.header("📝 Generate Study Notes")
    
    if not topic:
        st.info("Enter a topic from the sidebar.")
        
    else:
        
        if st.button("Generates Notes" , key= "notes"):
            
            
            prompt = f"""
            
            Create detailed but easy-to-revise study notes.

Topic: {topic}
Difficulty: {difficulty}

Requirements:

- Use clear headings
- Use bullet points
- Explain important definitions
- Include important formulas if applicable
- Include examples
- Mention important exam points
- Keep the notes organized
- Add a final quick revision section
"""
            
            with st.spinner("Creating notes..."):
                result = generate_response(prompt)
                
            st.markdown(result)
            
            
            
# ---------------------------------------------------
# MCQ TAB
# ---------------------------------------------------

with tab3:

    st.header("❓ Multiple Choice Questions")

    if not topic:
        st.info("Enter a topic from the sidebar.")

    else:

        number_of_questions = st.slider(
            "Number of questions",
            min_value=3,
            max_value=10,
            value=5
        )

        if st.button("Generate MCQs", key="mcq"):

            prompt = f"""
Create {number_of_questions} multiple-choice questions.

Topic: {topic}
Difficulty: {difficulty}

For every question provide:

Question:
A)
B)
C)
D)

Correct Answer:
Explanation:

Make sure the correct answer is clearly identified.
Questions should test understanding, not only memorization.
"""

            with st.spinner("Generating questions..."):

                result = generate_response(prompt)

            st.markdown(result)

            
            