# 📖 Docling Text Extractor

This is a **Flask-based web application** that extracts text from uploaded files or from files available on the internet.

## 🚀 Features
- 📂 Upload a file and extract text.
- 🌍 Provide a file URL for text extraction.
- 📝 View extracted text in a popup modal.
- 🔗 API endpoint for extracting text from a URL.

---

## 📌 Installation & Running

### A. Run Locally (Without Docker)
1. **Clone the repository:**
```bash
   git clone git@github.com:sthpratik/docling.git
   cd docling
```
## Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  ️# On Windows use: venv\Scripts\activate
```

## Install dependencies:
```bash
pip install -r requirements.txt
```

## Run the Flask application:
```bash
python src/app.py
```

## Open in your browser:
```bash
http://127.0.0.1:5050
```

B. Run with Docker

## Build the Docker image:
   ```bash
docker build -t docling .
```

## Run the container:
   ```bash
docker run -p 5050:5000 docling
```

## Open in your browser:
   ```bash
http://127.0.0.1:5050
```
C. Run with Docker Compose

## Use Docker Compose to deploy:
   ```bash
docker compose -f docker-compose.deploy.yml up
```

## Open in your browser:
   ```bash
http://127.0.0.1:5050
```

🌐 API Usage

## Extract text from a remote file URL

Endpoint:
```bash
GET http://127.0.0.1:5050/extract?filepath=<FILE_URL>
```

## Example
```bash
curl "http://127.0.0.1:5050/extract?filepath=https://example.com/sample.pdf"
```

## Response
```json
{
  "filepath": "https://example.com/sample.pdf",
  "text": "Extracted content here..."
}
```

📂 Project Structure
   ```plaintext
docling/
│── app.py                       # Flask app main script
│── requirements.txt             # Python dependencies
│── Dockerfile                   # Docker configuration
│── docker-compose.deploy.yml    # Docker Compose config (deployment)
│── docker-compose.yml           # Docker Compose config (local)
│── templates/
│   ├── index.html               # Frontend UI
│── static/
│   ├── style.css                # Stylesheets
│   ├── theme.css                # Stylesheets
│── uploads/                     # Temporary storage for uploaded files
```

🛠️ Dependencies
Flask - Web framework
requests - To fetch files from URLs
Docling - IBM’s document processing library
Docker (optional) - For containerized deployment
