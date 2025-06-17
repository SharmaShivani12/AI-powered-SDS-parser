# AI-Powered SDS Parser

This is a full-stack tool built to extract key information from Safety Data Sheets (SDS) automatically. The idea is to save time by removing the need to manually read and enter chemical data from lengthy documents.

## What It Does

- Lets you upload SDS PDF files through a web interface
- Parses each PDF to extract important fields like product name, manufacturer, and CAS number
- Stores the results in a database for easy access and further use

## Tech Stack

- **Backend:** Django + Django REST Framework
- **Parsing:** Local PDF-to-text with `PyMuPDF`, then processed by a locally running language model (- Uses a local LLM (e.g., LLaMA3) for PDF understanding
- Stores parsed data into a Django database)
- **Frontend:** Vue.js app (`sds-frontend/`) for uploading files and displaying results

## How It Works

When a PDF is uploaded, the backend reads the text, sends it to a local AI model (like LLAMA) running via Ollama, and extracts useful fields in structured JSON. This data is then saved directly into the Django database and can be viewed or extended as needed.
- **Backend:** Django + DRF  
  - Endpoint: `POST /api/upload/` accepts PDF uploads
  - Parses text using `PyMuPDF`, sends to local LLM
  - Saves structured data to the `SDSRecord` model
  - SQLite DB the default provided by Django.

- **AI Engine:** Local LLM (via Ollama API)
  - Receives prompt with raw PDF text
  - Responds with JSON containing extracted fields

- **Frontend:** Vue.js (`sds-frontend/`)
  - Handles PDF upload
  - Displays parsed SDS records

While running the app you will need to start the three terminals one for LLM , one for Django (backend)
and one for Vue(frontend).
![image](https://github.com/user-attachments/assets/5ef5c6c8-33d7-4265-a27a-b59974361d98)
![image](https://github.com/user-attachments/assets/61079c44-5f60-4577-a66a-7d04b8d86b63)


