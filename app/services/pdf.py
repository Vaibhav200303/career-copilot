from pypdf import PdfReader
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(file_path:str)->str:
    reader=PdfReader(file_path)
    if reader.is_encrypted:
        raise ValueError("Encrypted PDFs are not supported")
    pages_text=[]
    for page in reader.pages:
        text=page.extract_text()
        if text:
            pages_text.append(text)
    extracted_text="\n".join(pages_text).strip()

    if extracted_text:
        return extracted_text
    images=convert_from_path(file_path)
    ocr_text=[]
    for image in images:
        text=pytesseract.image_to_string(image)
        if text:
            ocr_text.append(text)
    return "\n".join(ocr_text).strip()