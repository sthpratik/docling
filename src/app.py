from flask import Flask, render_template, request, jsonify
import os
from docling.document_converter import DocumentConverter
import requests

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Read environment variables
PORT = os.getenv("PORT", 5050)  # 

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Extract text using Docling
    extracted_text = extract_text(filepath)

    return jsonify({"filename": file.filename, "text": extracted_text})


@app.route("/extract", methods=["GET"])
def extract_from_path():
    """Extracts text from a given URL file path"""
    file_url = request.args.get("filepath")
    
    if not file_url:
        return jsonify({"error": "File URL is required"}), 400
    
    try:
        response = requests.get(file_url, stream=True)
        if response.status_code != 200:
            return jsonify({"error": "Failed to download file"}), 400
        
        # Save the file temporarily
        temp_filename = os.path.join(UPLOAD_FOLDER, os.path.basename(file_url))
        with open(temp_filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        # Extract text
        extracted_text = extract_text(temp_filename)

        # Optional: Remove temp file after extraction
        os.remove(temp_filename)

        return jsonify({"filepath": file_url, "text": extracted_text})
    
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch file: {str(e)}"}), 400

@app.route("/extract_from_form", methods=["POST"])
def extract_from_form():
    """Handles form-based file path input and returns extracted text"""
    file_path = request.form.get("filepath")

    if not file_path:
        return render_template("index.html", error="File path is required")

    if not os.path.exists(file_path):
        return render_template("index.html", error="File not found")

    extracted_text = extract_text(file_path)

    return render_template("index.html", text=extracted_text)

def extract_text(filepath):
    # source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
    converter = DocumentConverter()
    result = converter.convert(filepath)
    print(result.document.export_to_markdown())
    return result.document.export_to_markdown()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(PORT))  # Change 8080 to any free port

