# 🧠 Talk to Your PDF Application

A conversational AI-powered app that allows users to upload any PDF and interact with it in plain English.

Get intelligent answers based on the document's content — powered by Hugging Face Transformers!

---

## 📸 Demo Screenshot

![Talk to Your PDF Demo](demo_screenshot.png)

---

## 🚀 Features

- 📁 Upload PDF files (up to 200MB)
- 📝 AI-generated summary of the entire PDF
- ❓ Ask questions in plain English about the document
- 🤖 Powered by:
  - `facebook/bart-large-cnn` for summarization
  - `deepset/roberta-base-squad2` for question answering
- 💬 Streamlit UI with user-friendly interface
- 🔐 API Key securely loaded via `.env`

---

## 🛠️ Installation

1. **Clone this repo**  
   ```bash
   git clone https://github.com/Satyam0775/Talk-to-your-PDF-application.git
   cd Talk-to-your-PDF-application
