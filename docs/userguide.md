📖 User Guide: Docling Text Extractor

This guide will help you understand how to use the Flask File Text Extractor, a web-based tool that extracts text from uploaded files or files available online.

## 🔹 Features
- ✅ Upload a file and extract text
- ✅ Provide a file URL for remote extraction 
- ✅ View extracted text in a popup modal
- ✅ API endpoint for programmatic extraction

## 1️⃣ Running the Project Locally

### 📌 Prerequisites
- Python 3.x installed
- pip (Python package manager) installed
- virtualenv (optional but recommended)
- Docker (optional, if running in a container)

### 📌 Installation Steps

#### A. Run Locally (Without Docker)

1. Clone the Repository:
```bash
git clone https://github.com/yourusername/docling.git
cd docling
```

Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install Dependencies
```

```bash
pip install -r requirements.txt
Run the Flask Application
```

```bash
python app.py
The app will start at http://127.0.0.1:5050/.
```

2️⃣ Using the Web Application

### 🔹 A. Extract Text from an Uploaded File
1. Open `http://127.0.0.1:5050`
2. Click \"Choose File\", select a document, and click \"Upload & Extract\"
3. The extracted text will appear in a popup modal
4. Click \"View Extracted Data\" to see the text again

### 🔹 B. Extract Text from a File URL
1. Open `http://127.0.0.1:5050`
2. Enter the file URL in the text box
3. Click \"Extract\"
4. The extracted text will appear in a popup modal

## 3️⃣ API Usage

### 🔹 A. Extract Text from a Remote File URL
```bash
GET http://127.0.0.1:5050/extract?filepath=<FILE_URL>


Use the following API endpoint:
```bash
GET http://127.0.0.1:5000/extract?filepath=<FILE_URL>
```

Example

```bash
curl "http://127.0.0.1:5000/extract?filepath=https://example.com/sample.pdf"
```

Response
```json
{
  "filepath": "https://example.com/sample.pdf",
  "text": "Extracted content here..."
}
```

4️⃣ Running with Docker
Build the Docker Image
```bash
docker build -t docling .
```

Run the Docker Container
```bash
docker run -p 5050:5050 docling
Open http://127.0.0.1:5050 in your browser.
```