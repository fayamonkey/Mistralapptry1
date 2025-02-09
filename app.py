import streamlit as st
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import zipfile
import os

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            text += pytesseract.image_to_string(image)
    return text

# Streamlit app
st.title("PDF to Markdown Converter")

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    if st.button("Process"):
        markdown_files = []
        with st.spinner('Processing...'):
            for uploaded_file in uploaded_files:
                text = extract_text_from_pdf(uploaded_file)
                markdown_content = f"# Extracted Text from {uploaded_file.name}\n\n{text}"
                markdown_files.append((uploaded_file.name.replace('.pdf', '.md'), markdown_content))

            # Create a ZIP file
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
                for file_name, content in markdown_files:
                    zip_file.writestr(file_name, content)

            zip_buffer.seek(0)
            st.download_button(
                label="Download Markdown files as ZIP",
                data=zip_buffer,
                file_name="extracted_texts.zip",
                mime="application/zip"
            )
