
# PDF Answering AI (ArIES)

This project is a web-based application designed to extract text from PDF files and answer questions based on the extracted content using advanced natural language processing techniques. The application is built using Flask for the backend, Streamlit for the frontend, and the Hugging Face Transformers library for the question-answering model.

## Table of Contents

- [Objective](#objective)
- [Model Selection](#model-selection)
- [Installation](#installation)
- [Usage](#usage)
- [PDF Text Extraction](#pdf-text-extraction)
- [Question Answering Pipeline](#question-answering-pipeline)
- [Model Training](#model-training)
- [Key Learnings](#key-learnings)
- [Future Enhancements](#future-enhancements)
- [References](#references)

## Objective

The goal of this project is to create a system that can read PDF documents and provide accurate answers to user queries based on the content extracted from the PDFs. This project combines web development and advanced NLP models to deliver an interactive and intelligent application.

## Model Selection

We use the Hugging Face Transformers library, specifically the BERT (Bidirectional Encoder Representations from Transformers) model, for our question-answering tasks due to its high accuracy, pre-trained capabilities, flexibility, and ease of use.

## Installation

Follow these steps to set up the environment and run the application:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/pdf-answering-ai.git
   cd pdf-answering-ai
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit application:**
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage

1. **Open the Streamlit application:**
   - After running the above command, Streamlit will start a local server. Open the provided URL (e.g., http://localhost:8501) in your web browser.

2. **Upload a PDF file:**
   - Use the file uploader in the Streamlit app to upload a PDF document.

3. **Ask a question:**
   - Enter your question in the provided text box. The application will extract text from the uploaded PDF and use the question-answering model to provide an answer.

## PDF Text Extraction

Text extraction from PDFs is handled using PyMuPDF. The function `extract_text_from_pdf(pdf_path)` reads the PDF and extracts text from each page, concatenating it into a single string for processing.

## Question Answering Pipeline

The Hugging Face Transformers library is used to initialize the question-answering pipeline. The function `answer_question(question, context)` utilizes this pipeline to find answers based on the extracted text from the PDF.

## Model Training

Although this project uses a pre-trained BERT model, the fine-tuning process involves:

1. **Data Collection:** Gathering a dataset with context-question-answer pairs, such as the SQuAD dataset.
2. **Data Pre-processing:** Tokenizing the context and questions and preparing the data in a format compatible with BERT.
3. **Training:** Fine-tuning the pre-trained BERT model on the dataset using the Hugging Face Transformers library.
4. **Evaluation:** Using metrics like Exact Match (EM) and F1 score to assess accuracy.

## Key Learnings

- Understanding transformer-based models like BERT.
- Developing a web application using Flask and Streamlit.
- Methods to extract text from PDF documents using PyMuPDF.
- Integrating machine learning models into a web environment.

## Future Enhancements

- **User Interface Improvements:** Making the interface more intuitive and user-friendly.
- **Performance Optimization:** Enhancing text extraction and model inference speed.
- **Scalability:** Scaling the application to handle multiple users and large documents.
- **Advanced Features:** Adding functionalities like keyword highlighting, summarization, and multi-document support.
- **Fine-tuning:** Fine-tuning the BERT model on domain-specific datasets for improved accuracy in specialized applications.

## References

- "Natural Language Processing with Transformers" by Lewis Tunstall, Leandro von Werra, and Thomas Wolf.
- Real Python article on "Extracting Text from PDFs Using Python".
- Hugging Face Transformers Documentation: [Hugging Face](https://huggingface.co/transformers/)
- PyMuPDF Documentation: [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)

---

Thank you for using the PDF Answering AI! If you have any questions or need further assistance, feel free to reach out.
