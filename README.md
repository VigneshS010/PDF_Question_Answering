PDF QUESTION ANSWERING APPLICATION

This application allows users to upload a PDF document and ask questions about its content. It uses natural language processing models to extract text, generate answers, and provide concise summaries. Built with Streamlit for the user interface, it leverages PyPDF2 for text extraction and Hugging Face Transformers (BERT for question answering and BART for summarization) for processing.

INSTALLATION

1. Ensure Python 3.7 or later is installed on your system.
2. Install required packages using pip:
   pip install streamlit PyPDF2 torch transformers
3. Additional setup is not required as the models are automatically downloaded from Hugging Face Hub on first run.

USAGE

1. Run the application with the following command:
   streamlit run app.py
2. In the browser window that opens:
   - Use the file uploader to upload a PDF document.
   - Enter a question in the provided text input field.
   - The application will process the document and display the answer.
3. Example question for a research paper PDF: "What is the main contribution of this study?"

CONTRIBUTING

Contributions are welcome. Follow these steps to contribute:
1. Fork the repository.
2. Create a feature branch for your changes.
3. Commit your changes with clear commit messages.
4. Push the branch to your forked repository.
5. Open a pull request with a detailed description of your changes.
6. Ensure code follows existing style and includes necessary tests.

LICENSE

The application code is licensed under MIT License. Note that the underlying models (deepset/bert-base-cased-squad2 and facebook/bart-large-cnn) are subject to their respective licenses from Hugging Face Model Hub.
