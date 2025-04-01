import streamlit as st
import PyPDF2
from transformers import pipeline

def extract_text_from_pdf(pdf_file):
    text = ''
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return None
    

@st.cache_resource  # Cache the model for efficiency
def load_qa_pipeline():
    return pipeline("question-answering", model="deepset/bert-base-cased-squad2")

@st.cache_resource #cache summarizer
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

def answer_question(question, context, qa_pipeline, summarizer):
    max_length = 512
    stride = 100
    chunks = []
    for i in range(0, len(context), max_length - stride):
        chunks.append(context[i:i + max_length])

    answers = []
    for chunk in chunks:
        try:
            result = qa_pipeline(question=question, context=chunk)
            if result['answer'].strip():
                answers.append(result['answer'].strip())
        except Exception as e:
            st.warning(f"Error processing chunk: {e}")

    if answers:
        final_answer = " ".join(answers)
        try:
            summarized_answer = summarizer(final_answer, max_length=50, min_length=10, do_sample=False)[0]['summary_text']
            return summarized_answer
        except Exception as e:
            st.warning(f"Error during summarization: {e}")
            return final_answer
    else:
        return "Could not find an answer."
    

def main():
    st.title('PDF Question Answering')

    file = st.file_uploader('Upload a PDF file', type='pdf')
    question = st.text_input('Enter you question: ')

    if file and question:
        text = extract_text_from_pdf(file)
        if text:
            qa_pipeline = load_qa_pipeline()
            summarizer = load_summarizer()
            answer = answer_question(question, text, qa_pipeline, summarizer)
            st.subheader('Answer:')
            st.write(answer)

if __name__ == "__main__":
    main()