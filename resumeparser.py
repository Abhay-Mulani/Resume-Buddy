import google.generativeai as genai
import json

class ResumeParser:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash"  # ✅ Works on free tier
        )

    def extract_text(self, resume_text):
        prompt = f"""
You are a resume parser. From the text below, extract:

- Full Name
- Email
- Phone
- Skills
- Education
- Work Experience

Return your answer as a **valid JSON object**.

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return json.dumps({"Error": f"Gemini API Error: {e}"})
