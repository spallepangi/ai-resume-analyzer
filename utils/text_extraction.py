import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(file_obj):
    """
    Extracts text from a PDF file object uploaded via Streamlit.
    
    Args:
        file_obj: The file-like object uploaded through Streamlit.
        
    Returns:
        str: Extracted text from the PDF.
    """
    # Read the file object as bytes
    file_bytes = file_obj.read()

    # Open the PDF from bytes
    pdf_document = fitz.open(stream=file_bytes, filetype="pdf")
    
    text = ""
    for page in pdf_document:
        text += page.get_text()
    
    return text


def extract_text_from_word(file_obj):
    """
    Extracts text from a Word document (.docx).
    
    Args:
        file_obj: The file-like object uploaded through Streamlit.
        
    Returns:
        str: The extracted text from the Word document.
    """
    doc = docx.Document(file_obj)
    return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
