# Docling
# Docling Text Extractor

This is a Flask-based web application that extracts text from uploaded files or from files available on the internet.

## 🚀 Features
- Upload a file and extract text.
- Provide a file URL for text extraction.
- View extracted text in a popup modal.
- API endpoint for extracting text from a URL.

## 📌 Installation & Running
### A. Run Locally (Without Docker)
1. Clone the repository:
   ```bash
   git clone git@github.com:sthpratik/docling.git
   cd docling
Create a virtual environment:
bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:
bash
Copy
pip install -r requirements.txt
Run the Flask application:
bash
Copy
python app.py
Open http://127.0.0.1:5050 in your browser.
B. Run with Docker
Build the Docker image:
bash
Copy
docker build -t flask-text-extractor .
Run the container:
bash
Copy
docker run -p 5000:5000 docling
Run with docker compose
╰─ docker compose -f docker-compose.deploy.yml up 
Open http://127.0.0.1:5050 in your browser.
🌐 API Usage
Extract text from a remote file URL
bash
Copy
GET http://127.0.0.1:5000/extract?filepath=<FILE_URL>
Example:

bash
Copy
curl "http://127.0.0.1:5000/extract?filepath=https://example.com/sample.pdf"
Response:

json
Copy
{
  "filepath": "https://example.com/sample.pdf",
  "text": "Extracted content here..."
}
📂 Project Structure
php
Copy
docling/
│── app.py                       # Flask app main script
│── requirements.txt             # Python dependencies
│── Dockerfile                   # Docker configuration
│── docker-compose.deploy.yml    # Docker configuration
│── docker-compose.ynl           # Docker configuration

│── templates/
│   ├── index.html               # Frontend UI
│── static/
│   ├── style.css                # Stylesheets
│   ├── theme.css                # Stylesheets
│── uploads/                     # Temporary storage for uploaded files
🛠️ Dependencies
Flask
requests
docling
Docker (optional)