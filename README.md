# Cover Letter Generator

A simple Python script that customizes a cover letter based on a job and company description. It uses a template `.docx` file and generates a tailored cover letter using a language model (e.g., from Groq's API).

---

## 🚀 How It Works

The script reads:
- A resume file (DOCX)
- A cover letter template (DOCX)
- Job description (`jobDescription.txt`)
- Company description (`companyDescription.txt`)

It then uses an AI model to fill in the template, creating a customized cover letter ready to be saved as a new `.docx` file.

---

## 🔧 Setup

1. **Install dependencies**  
   

   ```bash
   pip install requests
   pip install python-docx
   ```

2. **Create a `config.py` file**  
   Add the following variables to a `config.py` file in your project root:

   ```python
   GROQ_API_KEY = "your_groq_api_key"
   GROQ_MODEL = "your_model_name"
   GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"

   RESUME_PATH = "/path/to/your/resume.docx"
   COVER_LETTER_TEMPLATE_PATH = "/path/to/your/template.docx"
   COVER_LETTER_PATH = "/path/to/save/generated_cover_letter.docx"

   JOB_DESCRIPTION_PATH = "jobDescription.txt"
   COMPANY_DESCRIPTION_PATH = "companyDescription.txt"
   ```

---

## ✅ Output

A fully customized cover letter will be saved at the path defined in `COVER_LETTER_PATH`.

---

## 📌 Notes

- Make sure the job and company description files are plain `.txt` files.

- The cover letter template **must include the following placeholders** for the script to work correctly:
  - `<company name>`
  - `<current date>`
  - `<location>`
  - `<content>`

> ⚠️ These placeholders are required. If they are missing or misnamed, the generated cover letter may be incomplete or fail to generate properly. a sample cover letter is included that shows the placeholders

> 📝 A sample cover letter template is included in the project to show how the placeholders should be used.
---

## ⚠️ Disclaimer

This tool is provided as-is for personal use. The user is responsible for reviewing and editing generated content. API usage and data processing are handled entirely through the user's own configuration and keys.

