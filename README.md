# AI-Powered SDS Parser

This is a full-stack tool built to extract key information from Safety Data Sheets (SDS) automatically. The idea is to save time by removing the need to manually read and enter chemical data from lengthy documents.

## What It Does

- Lets you upload SDS PDF files through a web interface
- Parses each PDF to extract important fields like product name, manufacturer, and CAS number
- Stores the results in a database for easy access and further use

## Tech Stack

- **Backend:** Django + Django REST Framework
- **Parsing:** Local PDF-to-text with `PyMuPDF`, then processed by a locally running language model
- **Frontend:** Vue.js app (`sds-frontend/`) for uploading files and displaying results

## How It Works

When a PDF is uploaded, the backend reads the text, sends it to a local AI model (like LLaMA3) running via Ollama, and extracts useful fields in structured JSON. This data is then saved directly into the Django database and can be viewed or extended as needed.

---

This project helps streamline chemical data entry and improves accuracy when dealing with complex SDS documents.
