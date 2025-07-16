# Talk-to-your-PDF-application.

# 🧠 Talk to Your PDF

A simple, AI-powered app that lets you interact with your PDF documents using natural language.

This tool enables students, researchers, professionals, and anyone working with long documents to **upload a PDF, ask questions**, and receive **AI-generated answers**—all through an elegant, minimal interface.

---

## 🚀 Features

- 📤 Upload and read any PDF file
- ❓ Ask natural-language questions
- 🤖 Get answers using **Hugging Face Inference API**
- 🎨 Dark mode UI with red theme
- 🔐 Uses `.env` file to securely load your Hugging Face token
- 🧠 Powered by `facebook/bart-large-cnn` for summarization and response

---

## 📸 Preview

![App Screenshot](https://via.placeholder.com/800x400.png?text=Screenshot+Placeholder)

---

## 🔧 Technologies Used

- `Streamlit` – UI & app framework  
- `PyPDF2` – PDF text extraction  
- `Hugging Face Transformers` – API for NLP model  
- `dotenv` – Secure API key handling  
- `requests` – HTTP calls to Hugging Face

---

## 📦 Installation & Running Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/talk-to-your-pdf.git
   cd talk-to-your-pdf
