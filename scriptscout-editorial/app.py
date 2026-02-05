import os
from flask import Flask, render_template, request, jsonify
import PyPDF2
import docx
from google import genai
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()

# Initialize the Gemini 2.5 Flash Client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

def extract_text(file):
    """
    Parses PDF or DOCX files and returns raw text.
    """
    if file.filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        return "".join([p.extract_text() or "" for p in reader.pages])
    elif file.filename.endswith('.docx'):
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    return ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/audit', methods=['POST'])
def audit():
    file = request.files.get('manuscript')
    if not file:
        return jsonify({"error": "No manuscript uploaded"}), 400

    try:
        # 1. Extraction and Pre-processing
        raw_text = extract_text(file)
        
        # 2. Text Cleaning to prevent Python 3.10 f-string backslash errors
        # We replace problematic characters that could break the string injection
        clean_text = raw_text.replace('"', "'").replace('\n', ' ')

        # 3. IRJMS Strict Editorial System Prompt
        prompt = f"""
        Act as a Managing Editor for the International Research Journal of Multidisciplinary Scope (IRJMS).
        You are performing an automated editorial compliance check. 
        
        MANUSCRIPT TEXT:
        {clean_text}

        STRICT COMPLIANCE RULES:
        1. Abstract: Must be a SINGLE paragraph in block format. No indentations. No structured sub-headers. Word count MUST be between 200-250 words.
        2. Keywords: Provide exactly 4 to 6 keywords.
        3. Title Page: Verify the short title is within 54 characters (including spaces).
        4. Headings: Use ONLY major headings: Introduction, Methodology, Results, Discussion, Conclusion. NO section numbers (e.g., 1.1) and NO third-level headlines.
        5. Typography: Replace all "&" with "and" throughout the text.
        6. Abbreviations: Ensure full forms are used during the first mention.
        7. Post-Conclusion Sections: The manuscript MUST have these specific sections in order:
           - Acknowledgement
           - Funding
           - Conflict of Interest
           - Declaration of Generative AI and AI Assisted Technologies in the Writing Process
           - Author Contributions
           - Ethics approval
           - Data availability
           - Abbreviation
           - REFERENCES
        8. Citations: Use parentheses for citations, e.g., (1), (2), sequentially starting from 1.
        9. Reference Style (Vancouver): Check against this format: "Westerik N, et al. Title. Journal. Year; Vol:Pages. DOI."
        10. Figures & Tables: Ensure legends are present and they are mentioned in Results/Discussion. Multipanel labels must be UPPER-CASE BOLD (A, B, C).

        OUTPUT:
        Provide a 'Point-by-Point' compliance report. 
        For every violation, quote the text and provide the correction.
        FINAL VERDICT: Accept, Minor Revisions, Major Revisions, or Reject.
        """

        # 4. Gemini 2.5 Flash Generation
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        return jsonify({"report": response.text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred during processing. Ensure the file is not corrupted."}), 500

if __name__ == '__main__':
    # Running on port 5002 to distinguish from the ATS project
    app.run(debug=True, port=5002)