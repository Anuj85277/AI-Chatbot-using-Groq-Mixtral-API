import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq API setup
API_URL = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# Streamlit page setup
st.set_page_config(page_title="Free Chatbot using Groq Mixtral API 💬", page_icon="💬")
st.markdown("<h1 style='text-align:center;'> Free Chatbot using Groq Mixtral API</h1>", unsafe_allow_html=True)
st.caption(" Powered by **Groq Mixtral** | Built with ❤️ using **Streamlit**")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display previous messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user input
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Placeholder for bot message
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🤖 Thinking...")

        # Request payload
        payload = {
            "model": "llama-3.3-70b-versatile",  # Groq's active model
            "messages": st.session_state["messages"]
        }

        # Make API call
        response = requests.post(API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()
            ai_reply = data["choices"][0]["message"]["content"]
        else:
            ai_reply = f"Error {response.status_code}: {response.text}"

        # Display AI reply
        message_placeholder.markdown(ai_reply)

    # Save assistant reply
    st.session_state["messages"].append({"role": "assistant", "content": ai_reply})
