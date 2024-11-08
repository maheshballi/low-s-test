# src/pdf_processing.py
import fitz  # PyMuPDF for reading PDF
import re

def extract_text_from_pdf(pdf_path):
    """
    Extracts raw text from each page of a PDF.
    :param pdf_path: Path to the PDF file.
    :return: Extracted text as a single string.
    """
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf.load_page(page_num)
            text += page.get_text("text")
    return text

def clean_text(text):
    """
    Cleans extracted text by removing unwanted symbols, extra spaces, and greetings.
    :param text: Raw text from PDF.
    :return: Cleaned text.
    """
    # Remove greetings, unnecessary text, and extra whitespaces
    text = re.sub(r"(Moderator:|Ladies and gentlemen,|Thank you very much\.)", "", text)
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space
    return text
