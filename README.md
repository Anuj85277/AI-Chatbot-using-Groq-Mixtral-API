# 🤖 AI Chatbot using Groq Mixtral API

A simple and free-to-use **AI Chatbot** built with **Streamlit** and powered by **Groq’s Mixtral API**.  
This project provides an interactive UI where users can chat with an AI assistant — all in real time!

---

## 🚀 Features
- 💬 Interactive chat interface using **Streamlit**
- ⚡ Powered by **Groq Mixtral API** (free key)
- 🌈 Attractive and modern UI
- 🧠 Intelligent responses using the latest LLMs
- 🔒 Secure key handling via `.env` file

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Model:** Groq Mixtral API  
- **Environment Management:** Python `venv`

---

## 📂 Project Structure

AI-Chatbot-using-Groq-Mixtral-API/
│
├── app.py # Main Streamlit app
├── requirements.txt # Required dependencies
├── .env # Contains your API key (not uploaded to GitHub)
├── .gitignore # Ignored files (env, .env, etc.)
├── README.md # Project documentation
└── env/ # Virtual environment (excluded from Git)

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/AI-Chatbot-using-Groq-Mixtral-API.git
cd AI-Chatbot-using-Groq-Mixtral-API
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv env
env\Scripts\activate    # On Windows
# source env/bin/activate  # On Mac/Linux
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Add Your API Key
Create a .env file in the root directory and add your Groq API key:

ini
Copy code
GROQ_API_KEY=your_api_key_here
5️⃣ Run the App
bash
Copy code
streamlit run app.py
