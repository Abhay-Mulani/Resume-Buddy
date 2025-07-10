from flask import Flask, render_template, request, Response
import PyPDF2
import os
import json
from resumeparser import ResumeParser

app = Flask(__name__)

# Load Gemini API key from config.yaml
gemini_key = os.getenv("GEMINI_API_KEY")

parser = ResumeParser(gemini_key)

# Function to extract text from PDF
def read_pdf(file_stream):
    try:
        reader = PyPDF2.PdfReader(file_stream)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    except Exception as e:
        return f"❌ PDF Read Error: {e}"

# Home page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# File upload and Gemini parsing route
@app.route("/process", methods=["POST"])
def parse_resume():
    file = request.files.get("pdf_doc")  # This should match input name="pdf_doc"
    if not file:
        return render_template("index.html", data={"Error": "No file uploaded."})

    resume_text = read_pdf(file.stream)
    if not resume_text or resume_text.startswith("❌"):
        return render_template("index.html", data={"Error": "Failed to extract text from PDF."})

    parsed_output = parser.extract_text(resume_text)

    # Try parsing to JSON; fallback to plain text
    try:
        parsed_dict = json.loads(parsed_output)
        return render_template("index.html", data=parsed_dict)
    except Exception:
        return render_template("index.html", data={"Result": parsed_output})

# Start Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
