# 🧠 Talk to Your PDF Application

A conversational AI-powered app that allows users to upload any PDF and interact with it in plain English.

Get intelligent answers based on the document's content powered by Hugging Face Transformers!

---

## 📸 Demo Screenshot

![Talk to Your PDF Demo]<img width="956" height="407" alt="demo_screenshot" src="https://github.com/user-attachments/assets/52a84f1a-9505-40e4-a69f-d0f10823756e" />
(demo_screenshot.png)

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

   Create a .env file with your Hugging Face API token:

HUGGINGFACE_API_KEY=your_huggingface_token
Install dependencies

pip install -r requirements.txt
Run the app locally

streamlit run app.py
🧪 Example Usage
Upload a PDF — e.g., Bihar Assembly Elections 2025.pdf

Click “📝 Generate Summary”

Ask:

Get real-time answers from the AI!

🧰 Tech Stack
Streamlit for web interface

PyPDF2 for PDF text extraction
requests for Hugging Face API
Hugging Face Transformers (Inference API):
bart-large-cnn for summarization
roberta-base-squad2 for Q&A

.env for secure API token management

📁 Folder Structure
TALK-WITH-PDF-MAIN/
├── .streamlit/
│   └── config.toml
├── app.py
├── .env                 # Your Hugging Face token
├── requirements.txt
├── .gitignore
├── README.md
📄 License
This project is for educational and demonstration purposes under the MIT License.

📬 Submission
For Blackrose AI Team or recruiter review, this project meets:

Functional PDF upload & QA
Proper folder structure
API-based LLM response
Secure API key handling
Readable, clean UI

🤝 Connect
👤 Satyma Kumar 
