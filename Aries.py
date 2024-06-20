import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline

# Set up the question-answering model
qa_engine = pipeline("question-answering")

def read_pdf(pdf_stream):
    document = fitz.open(stream=pdf_stream.read(), filetype="pdf")
    content = ""
    for page in document:
        content += page.get_text()
    return content

st.title("PDF Q&A Application")

uploaded_file = st.file_uploader("Upload your PDF document", type=["pdf"])
if uploaded_file:
    document_text = read_pdf(uploaded_file)
    st.write("Extracted Content:")
    st.write(document_text)

    user_query = st.text_input("Ask a question regarding the PDF content:")
    if user_query:
        response = qa_engine(question=user_query, context=document_text)
        st.write("Answer:")
        st.write(response['answer'])
