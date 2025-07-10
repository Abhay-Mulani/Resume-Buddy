
# 📄 Resume Buddy

**Resume Buddy** is a smart resume parsing web application powered by Google Gemini API and NLP tools. Upload your resume (PDF) and get a structured breakdown including your name, contact, skills, education, work experience, and more — all parsed and displayed in a beautiful UI.

---

## 🚀 Features

- Upload resume in `.pdf` format  
- Extracts:
  - Full Name
  - Email & Phone
  - Skills
  - Education History
  - Work Experience
- Uses Google Gemini API (free-tier supported)
- Clean and elegant UI using TailwindCSS
- Displays parsed data on a separate, well-styled result page

---

## 🧠 Tech Stack

- **Frontend**: HTML + TailwindCSS
- **Backend**: Flask (Python)
- **AI/NLP**: Google Gemini API, PyPDF2, JSON
- **Other**: YAML config, Bootstrap-style Tailwind styling

---

## 📂 Project Structure

```
Resume-Buddy/
├── static/
├── templates/
│   └── index.html
├── resumeparser.py
├── app.py
├── config.yaml
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/Abhay-Mulani/Resume-Buddy
   cd resume-buddy
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Gemini API key in `config.yaml`**
   ```yaml
   gemini_api_key: "YOUR_GEMINI_API_KEY"
   ```

5. **Run the app**
   ```bash
   python app.py
   ```

6. **Go to browser**
   ```
   http://localhost:8000
   ```

---

## 📌 Notes

- Ensure your Gemini API key supports the `text` generation capability.
- Built with Gemini Free Tier compatible model.
- Supports most clean and structured resumes.

---

## 🙌 Author

**Abhay Mulani**

---

## 📃 License

This project is licensed under the MIT License.
