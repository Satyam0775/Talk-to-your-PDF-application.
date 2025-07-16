import streamlit as st
import PyPDF2
import requests
import os
from dotenv import load_dotenv

# 🔐 Load environment variables
load_dotenv()
HF_API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# 📄 Extract PDF Text
def extract_text_from_pdf(uploaded_file):
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        return f"⚠️ Error reading PDF: {str(e)}"

# 📑 Summarize PDF using BART
def summarize_pdf_text(text):
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {
        "inputs": text[:3000],
        "parameters": {
            "max_length": 400,
            "do_sample": False
        }
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
        headers=headers,
        json=payload
    )

    try:
        result = response.json()
        if isinstance(result, list) and "summary_text" in result[0]:
            return result[0]["summary_text"]
        elif isinstance(result, dict) and "error" in result:
            return f"⚠️ Hugging Face API Error: {result['error']}"
        return "⚠️ Couldn't generate summary."
    except Exception as e:
        return f"⚠️ Error during summarization: {str(e)}"

# 🤖 Question Answering using Roberta-SQuAD2
def ask_question(context_text, question):
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {
        "inputs": {
            "question": question,
            "context": context_text[:3000]
        }
    }

    response = requests.post(
        "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2",
        headers=headers,
        json=payload
    )

    try:
        result = response.json()
        if "answer" in result and result["answer"].strip():
            return result["answer"].strip()
        elif "error" in result:
            return f"⚠️ QA Error: {result['error']}"
        else:
            return "🤔 I couldn't find a clear answer in the document."
    except Exception as e:
        return f"⚠️ Unexpected Error: {str(e)}"

# 🌐 Streamlit UI
st.set_page_config(page_title="Talk to Your PDF", page_icon="📄")
st.markdown("<h1 style='text-align: center;'>🧠 Talk to Your PDF</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload any PDF and ask questions — get real-time answers from AI!</p>", unsafe_allow_html=True)
st.divider()

# 📤 File Upload
uploaded_file = st.file_uploader("📁 Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("📖 Extracting text..."):
        full_pdf_text = extract_text_from_pdf(uploaded_file)

    # 📄 Get Summary Button
    if st.button("📝 Generate Summary"):
        with st.spinner("Summarizing..."):
            summary = summarize_pdf_text(full_pdf_text)
        st.subheader("📄 Summary of the Document")
        st.write(summary)
    else:
        summary = summarize_pdf_text(full_pdf_text)

    # 💬 Ask Your Question
    user_question = st.text_input("❓ Ask a question about the PDF")

    if user_question:
        with st.spinner("🤖 Thinking..."):
            answer = ask_question(summary, user_question)
        st.subheader("📘 Answer")
        st.write(answer)
else:
    st.info("Please upload a PDF file to begin.")
