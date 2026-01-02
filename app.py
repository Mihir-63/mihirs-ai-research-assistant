import streamlit as st
from api.pdf_utils import extract_text_from_pdf
from api.summarizer import chunk_text, summarize_chunks

st.set_page_config(page_title="AI Research Assistant")


st.markdown(
    """
    <div style="
        background-image: url('https://plus.unsplash.com/premium_photo-1664372145510-0c19fbc04acb?q=80&w=1169&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
        padding: 60px;
        text-align: center;
        color: white;
        font-size: 36px;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        border-radius: 12px;
    ">
        AI Research Assistant<br>
        <span style="font-size: 20px; font-weight: normal;">
        Student-friendly summaries of research papers
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")  # spacing


st.title("📚 AI Research Assistant")
st.write("Upload a research paper PDF to get a student-friendly summary.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    pdf_path = "temp.pdf"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Extracting text..."):
        text = extract_text_from_pdf("temp.pdf")

    with st.spinner("Summarizing paper..."):
        chunks = chunk_text(text)
        summary = summarize_chunks(chunks)

    st.subheader("🧠 AI Summary")
    st.write(summary)