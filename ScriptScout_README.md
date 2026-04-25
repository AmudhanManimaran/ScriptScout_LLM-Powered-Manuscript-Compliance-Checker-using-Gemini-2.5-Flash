# ScriptScout — LLM-Powered Manuscript Compliance Checker

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-orange?style=flat-square&logo=google)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

> An automated editorial compliance engine that uses **Gemini 2.5 Flash** to audit academic manuscripts against strict **IRJMS journal formatting rules** — replacing manual editorial screening with a structured LLM-driven point-by-point compliance report.

---

## 🎯 Key Features

- **PDF & DOCX parsing** — extracts and normalizes raw manuscript text
- **10-rule IRJMS compliance engine** — abstract word count, keyword count, heading structure, citation style, Vancouver reference format, figure legends, and more
- **Structured point-by-point report** — every violation quoted with correction
- **Final editorial verdict** — Accept / Minor Revisions / Major Revisions / Reject
- **Flask web interface** — upload manuscript, receive instant audit report
- **Gemini 2.5 Flash** — long-context LLM for full manuscript reasoning

---

## 🏗️ System Architecture

```
User Uploads Manuscript (PDF / DOCX)
            │
            ▼
┌───────────────────────────────┐
│   Text Extraction Layer       │
│   PyPDF2 (PDF) / python-docx  │  ← Parses & normalizes raw text
└───────────────────────────────┘
            │
            ▼
┌───────────────────────────────┐
│   Prompt Engineering Layer    │  ← Injects manuscript + 10 IRJMS
│   (Managing Editor Persona)   │    compliance rules into prompt
└───────────────────────────────┘
            │
            ▼
┌───────────────────────────────┐
│   Gemini 2.5 Flash (LLM)      │  ← Long-context compliance reasoning
│   Compliance Reasoning Engine │    Point-by-point violation detection
└───────────────────────────────┘
            │
            ▼
┌───────────────────────────────┐
│   Structured Audit Report     │  ← Violations quoted + corrected
│   + Final Editorial Verdict   │    Accept / Revisions / Reject
└───────────────────────────────┘
            │
            ▼
      Flask Web Dashboard
```

---

## 📋 IRJMS Compliance Rules Enforced

| # | Rule | Check |
|---|------|-------|
| 1 | Abstract | Single paragraph, block format, 200–250 words |
| 2 | Keywords | Exactly 4–6 keywords |
| 3 | Title Page | Short title ≤ 54 characters |
| 4 | Headings | Major headings only, no section numbers, no third-level |
| 5 | Typography | No "&" — replace with "and" |
| 6 | Abbreviations | Full form on first mention |
| 7 | Post-Conclusion | 9 mandatory sections in exact order |
| 8 | Citations | Sequential parentheses format: (1), (2)... |
| 9 | References | Vancouver style with DOI |
| 10 | Figures & Tables | Legends present, UPPER-CASE BOLD multipanel labels |

---

## 📁 Project Structure

```
ScriptScout/
│
├── scriptscout-editorial/
│   ├── app.py                  # Flask backend + Gemini API integration
│   ├── requirements.txt        # Python dependencies
│   ├── .env.example            # API key template
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css       # Frontend styling
│   │   └── js/
│   │       └── script.js       # Async fetch + UI logic
│   └── templates/
│       └── index.html          # Upload interface
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/AmudhanManimaran/ScriptScout.git
cd ScriptScout/scriptscout-editorial
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
```bash
cp .env.example .env
# Open .env and add your Gemini API key:
# GEMINI_API_KEY=your_api_key_here
```
Get your free Gemini API key at: [aistudio.google.com](https://aistudio.google.com)

### 5. Run the Application
```bash
python app.py
```
Visit `http://localhost:5002` in your browser.

---

## 🚀 Usage

1. Open the web interface at `http://localhost:5002`
2. Upload your manuscript as **PDF** or **DOCX**
3. Click **"Check Compliance"**
4. Receive a structured point-by-point audit report
5. Review violations with exact quotes and corrections
6. Final verdict: Accept / Minor Revisions / Major Revisions / Reject

---

## 🧠 Technical Details

### Prompt Engineering Strategy
The system uses a **Managing Editor persona prompt** that:
- Injects the full manuscript text into a structured context window
- Defines 10 strict IRJMS rules as explicit constraints
- Requires point-by-point output format with direct text quotation
- Forces a final categorical verdict

### Text Normalization
Before LLM injection, the pipeline:
- Strips backslash-prone characters to prevent f-string injection errors
- Normalizes newlines for consistent tokenization
- Handles both PDF (PyPDF2) and DOCX (python-docx) schemas

### LLM Selection
**Gemini 2.5 Flash** was chosen for:
- Long-context window — handles full academic manuscripts
- Fast inference for real-time editorial feedback
- Strong instruction-following for structured output generation

---

## 📦 Requirements

```
flask>=2.0.0
PyPDF2>=3.0.0
python-docx>=0.8.11
google-genai>=0.3.0
python-dotenv>=1.0.0
```

---

## ⚠️ Environment Variables

Create a `.env` file in the `scriptscout-editorial/` directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**Never commit your API key to GitHub.** The `.gitignore` excludes `.env` automatically.

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Amudhan Manimaran**
- 🌐 Portfolio: [amudhanmanimaran.github.io/Portfolio](https://amudhanmanimaran.github.io/Portfolio/)
- 💼 LinkedIn: [linkedin.com/in/amudhan-manimaran-3621bb32a](https://www.linkedin.com/in/amudhan-manimaran-3621bb32a)
- 🐙 GitHub: [github.com/AmudhanManimaran](https://github.com/AmudhanManimaran)
