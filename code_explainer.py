import streamlit as st
import openai
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI Code Explainer", page_icon="🧠", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .big-font {
        font-size: 20px !important;
        font-weight: bold;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #4F8BF9;
        border-radius: 50px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 50px;
    }
    .stTextArea textarea {
        border-radius: 15px;
    }
    .stSelectbox>div>div>select {
        border-radius: 50px;
    }
    .css-145kmo2 {
        font-size: 20px;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1 style='text-align: center; color: #4F8BF9;'>🧠 AI-Powered Code Explainer and Optimizer</h1>", unsafe_allow_html=True)

# API Key handling
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    st.error("OpenAI API key not found. Please set it in your environment variables or .env file.")
    st.stop()

# Functions
def explain_code(code, language):
    prompt = f"Explain the following {language} code in simple terms:\n\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that explains code."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def suggest_optimizations(code, language):
    prompt = f"Suggest optimizations for the following {language} code:\n\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that suggests code optimizations."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Main Interface
st.markdown("---")
st.markdown("<p class='big-font'>Let's analyze your code!</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    language = st.selectbox("Select programming language", ["Python", "JavaScript", "Java", "C++"])
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    analyze_button = st.button("Analyze Code")

code = st.text_area(f"Enter your {language} code here:", height=200)

if analyze_button:
    if code:
        st.markdown("---")
        st.markdown("<p class='big-font'>Your Code:</p>", unsafe_allow_html=True)
        st.code(code, language=language.lower())
        
        with st.spinner("AI is analyzing your code..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)
            
            explanation = explain_code(code, language)
            optimizations = suggest_optimizations(code, language)

        st.markdown("---")
        st.markdown("<p class='big-font'>Analysis Results:</p>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["Code Explanation", "Optimization Suggestions"])
        
        with tab1:
            st.markdown("<p style='color: #4F8BF9;'>Here's what your code does:</p>", unsafe_allow_html=True)
            st.write(explanation)
        
        with tab2:
            st.markdown("<p style='color: #4F8BF9;'>Here are some optimization suggestions:</p>", unsafe_allow_html=True)
            st.write(optimizations)
        
    else:
        st.warning("Please enter some code to analyze.")

# Sidebar
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/1024px-ChatGPT_logo.svg.png", width=100)
st.sidebar.title("About")
st.sidebar.info(
    "This app uses AI to explain code and suggest optimizations. "
    "It demonstrates the potential of AI in making programming more "
    "accessible and efficient for developers of all levels."
)
st.sidebar.markdown("---")
st.sidebar.success("Created with ❤️ by Muchiri Kahwai")
st.sidebar.markdown("---")
st.sidebar.markdown("Connect with me:")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/muchirik/)")
st.sidebar.markdown("[GitHub](https://github.com/kr-muchiri)")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>© 2024 AI Code Explainer. All rights reserved.</p>", unsafe_allow_html=True)