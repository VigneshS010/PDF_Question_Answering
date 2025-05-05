PDF Question Answering Application

DESCRIPTION:
This Streamlit application allows users to upload a PDF file and ask questions about its content. The app uses BERT for question answering and BART for summarization. Key features include text extraction from PDFs, question answering with context, summarization of answers, and caching for efficient model loading.

INSTALLATION:
1. Ensure Python 3.7 or later is installed.
2. Install required packages using pip:
   pip install streamlit PyPDF2 transformers torch
3. Clone the repository (if applicable).

USAGE:
1. Run the application with the command:
   streamlit run app.py
2. Upload a PDF file through the interface.
3. Enter your question in the provided text field.
4. View the generated answer in the application.

Example question: "What is the main topic of this document?"

CONTRIBUTING:
Contributions are welcome. To contribute:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes with clear commit messages.
4. Push your branch and open a pull request.
5. Ensure code adheres to existing standards and includes tests if applicable.

LICENSE:
The BERT model is used under the Apache License 2.0. The BART model is used under the MIT License.
