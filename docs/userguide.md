📖 User Guide: Flask File Text Extractor
This guide will help you understand how to use the Flask File Text Extractor, a web-based tool that extracts text from uploaded files or files available online.

🔹 Features
✅ Upload a file and extract text
✅ Provide a file URL for remote extraction
✅ View extracted text in a popup modal
✅ API endpoint for programmatic extraction

1️⃣ Running the Project Locally
📌 Prerequisites
Python 3.x installed
pip (Python package manager) installed
virtualenv (optional but recommended)
Docker (optional, if running in a container)
📌 Installation Steps
A. Run Locally (Without Docker)
Clone the Repository

bash
Copy
git clone https://github.com/your-repo/flask-text-extractor.git
cd flask-text-extractor
Create and Activate a Virtual Environment

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install Dependencies

bash
Copy
pip install -r requirements.txt
Run the Flask Application

bash
Copy
python app.py
The app will start at http://127.0.0.1:5000/.

2️⃣ Using the Web Application
🔹 A. Extract Text from an Uploaded File
Open http://127.0.0.1:5000.
Click "Choose File", select a document, and click "Upload & Extract".
The extracted text will appear in a popup modal.
Click "View Extracted Data" to see the text again.
🔹 B. Extract Text from a File URL
Open http://127.0.0.1:5000.
Enter the file URL in the text box.
Click "Extract".
The extracted text will appear in a popup modal.
3️⃣ API Usage
🔹 A. Extract Text from a Remote File URL
Use the following API endpoint:

bash
Copy
GET http://127.0.0.1:5000/extract?filepath=<FILE_URL>
Example
bash
Copy
curl "http://127.0.0.1:5000/extract?filepath=https://example.com/sample.pdf"
Response
json
Copy
{
  "filepath": "https://example.com/sample.pdf",
  "text": "Extracted content here..."
}
4️⃣ Running with Docker
Build the Docker Image
bash
Copy
docker build -t flask-text-extractor .
Run the Docker Container
bash
Copy
docker run -p 5000:5000 flask-text-extractor
Open http://127.0.0.1:5000 in your browser.