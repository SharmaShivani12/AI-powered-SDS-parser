import fitz  # PyMuPDF
import re
import json

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)

def parse_sds(path):
    text = extract_text_from_pdf(path)

    def extract_field(pattern, text, group=1, default=None):
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(group).strip() if match else default

    data = {}

    # Product name
    data["product_name"] = extract_field(r"Trade name[:\-]?\s*(.+)", text)

    # Manufacturer
    manufacturer_match = re.search(r"Manufacturer/Supplier:\s*(.*?)\n\s*(.*?)\n", text, re.DOTALL)
    if manufacturer_match:
        lines = manufacturer_match.groups()
        data["manufacturer"] = " ".join([line.strip() for line in lines])
    else:
        data["manufacturer"] = None

    # Address, if needed separately
    address_match = re.search(r"Keimstraße.*?\d{5}", text)
    data["address"] = address_match.group(0).strip() if address_match else None

    # Emergency contact
    data["emergency_contact"] = extract_field(r"Emergency number[:\-]?\s*(\+?[()\d/ -]+)", text)

    # Application
    data["application"] = extract_field(r"Application of the substance / the mixture\s*(.+)", text)

    # CAS Numbers (collect multiple if needed)
    data["cas_number"] = ", ".join(re.findall(r"CAS:\s*(\d{2,7}-\d{2}-\d)", text))

    # Hazard Statements
    hazard_section = re.search(r"· Hazard statements\s*(.*?)· Precautionary statements", text, re.DOTALL)
    if hazard_section:
        data["hazard_statements"] = hazard_section.group(1).replace("\n", " ").strip()
    else:
        data["hazard_statements"] = None

    # Composition
    comp_match = re.search(r"SECTION 3:.*?Dangerous components:\s*(.*?)\s*· Additional information:", text, re.DOTALL)
    if comp_match:
        data["composition"] = comp_match.group(1).strip()
    else:
        data["composition"] = None

    return data
