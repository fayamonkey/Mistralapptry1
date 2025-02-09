# PDF to Markdown Converter

This Streamlit app allows you to upload one or multiple PDF files, extract text from them (including OCR for images within the PDFs), and download the extracted text as Markdown files in a ZIP archive.

## How to Use

1. Upload one or more PDF files using the file uploader.
2. Click the "Process" button to start extracting text.
3. Once processing is complete, click the "Download Markdown files as ZIP" button to download the extracted text as Markdown files in a ZIP archive.

## Requirements

- Streamlit
- PyMuPDF
- pytesseract
- Pillow

## Setup

1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the app using `streamlit run app.py`.
