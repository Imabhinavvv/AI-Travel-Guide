import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from google.api_core.retry import Retry

# Load API key
file_path = "/Python_Challenges/gemini_key.txt"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        gemini_key = f.read().strip()
else:
    st.error("API Key file not found. Please check the file path.")
    st.stop()

# Set environment variable for DNS resolver
os.environ["GRPC_DNS_RESOLVER"] = "native"

# Streamlit App Configuration
st.set_page_config(page_title="AI Traveller", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main-title {
        text-align: center;
        color: #ffffff;
        background: linear-gradient(to right, #2c3e50, #4ca1af);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .stSidebar {
        background: #2c3e50;
        color: white;
        padding: 15px;
        border-radius: 10px;
    }
    .stButton button {
        width: 100%;
        background-color: #4ca1af;
        color: white;
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<div class='main-title'><h1>🌍 AI Traveller - Your Travel Companion 🧳</h1>" 
            "<p>Plan your journey smartly with AI-powered recommendations!</p></div>", 
            unsafe_allow_html=True)

# Initialize LLM if API key is available
llm = None
if gemini_key:
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=gemini_key,
            temperature=0.7,
            retry=Retry(initial=1.0, maximum=60.0, multiplier=2.0, deadline=900.0)
        )
    except Exception as e:
        st.error(f"Invalid API Key or authentication error: {e}")

# User Input - Travel Details
st.sidebar.header("✈️ Enter Your Travel Details")
source = st.sidebar.text_input("From Location:", placeholder="Enter your starting point...")
destination = st.sidebar.text_input("To Location:", placeholder="Enter your destination point...")
travel_mode = st.sidebar.selectbox("Travel Mode:", ["All", "Train", "Bus", "Flight", "Cab", "Bike"], index=0)
travel_preference = st.sidebar.selectbox("Travel Preference:", ["Budget", "Fastest", "Most Comfortable"], index=0)
sort_by = st.sidebar.selectbox("Sort Results By:", ["Price", "Duration", "Departure Time"], index=0)
language = st.sidebar.selectbox("Language:", ["English", "Hindi", "Tamil", "Telugu", "Kannada", "Marathi"], index=0)

# Search Button
if st.sidebar.button("🔍 Search Travel Options") and llm:
    if source and destination:
        prompt = f"""
        Provide travel options from {source} to {destination} using {travel_mode}.
        Prioritize {travel_preference} travel options.
        Sort results by {sort_by}.
        Respond in {language}.
        Include estimated costs and duration in bullet points.
        """

        with st.spinner("🚀 Fetching the best travel options... Please wait ✨"):
            try:
                response = llm.invoke([{ "role": "user", "content": prompt }])
                st.success("🎉 Here are your best travel options:")
                st.markdown(response.content)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter both source and destination locations.")
