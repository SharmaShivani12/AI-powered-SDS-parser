'''import fitz
import re

def extract_text(path):
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)

def parse_sds(path):
    text = extract_text(path)
    return {
        "product_name": re.search(r"(?i)product name\s*[:\-]?\s*(.+)", text).group(1).strip() if re.search(r"(?i)product name\s*[:\-]?\s*(.+)", text) else "",
        "manufacturer": re.search(r"(?i)manufacturer\s*[:\-]?\s*(.+)", text).group(1).strip() if re.search(r"(?i)manufacturer\s*[:\-]?\s*(.+)", text) else "",
        "emergency_contact": re.search(r"(?i)emergency.*?[:\-]?\s*(.+)", text).group(1).strip() if re.search(r"(?i)emergency.*?[:\-]?\s*(.+)", text) else "",
        "cas_number": re.search(r"\b\d{2,7}-\d{2}-\d\b", text).group(0) if re.search(r"\b\d{2,7}-\d{2}-\d\b", text) else "",
    }
    '''
