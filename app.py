import streamlit as st
from api.pdf_utils import extract_text_from_pdf
from api.summarizer import chunk_text, summarize_chunks

st.set_page_config(page_title="Mihir's AI Research Assistant")

st.title("📚 Mihir's AI Research Assistant")
st.write("Upload a research paper PDF to get a student-friendly summary.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with open("python_files/.venv/temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf("temp.pdf")

    with st.spinner("Summarizing paper..."):
        chunks = chunk_text(text)
        summary = summarize_chunks(chunks)

    st.subheader("🧠 AI Summary")
    st.write(summary)