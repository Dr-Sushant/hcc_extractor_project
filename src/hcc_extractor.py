import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define HCC keyword dictionary
HCC_KEYWORDS = {
    "diabetes": "HCC18",
    "diabetes mellitus": "HCC18",
    "chronic kidney disease": "HCC134",
    "ckd": "HCC134",
    "copd": "HCC111",
    "congestive heart failure": "HCC85",
    "chf": "HCC85",
    "hypertension": "HCC96",
    "asthma": "HCC112",
    "stroke": "HCC100",
    "depression": "HCC77",
    "coronary artery disease": "HCC96",
    "cad": "HCC96",
    "alzheimer": "HCC51"
}


def is_negated(phrase: str, text: str) -> bool:
    """
    Check for negations like 'no', 'denies', 'without' within 3 words before the phrase.
    """
    pattern = r"(no|denies|without)\s+(\w+\s*){0,3}" + re.escape(phrase)
    return bool(re.search(pattern, text.lower()))


def extract_hcc_codes(clinical_note: str) -> list:
    """
    Extract HCC codes by searching the entire note text (no NER dependency).
    """
    text = clinical_note.lower()
    extracted_codes = set()

    for keyword, hcc_code in HCC_KEYWORDS.items():
        if keyword in text:
            if not is_negated(keyword, text):
                extracted_codes.add(hcc_code)

    return sorted(extracted_codes)


# Run this when script is executed directly
if __name__ == "__main__":
    sample_note = """
    65-year-old male with history of CHF, diabetes mellitus and COPD.
    No signs of CKD or depression. Denies asthma or CAD.
    """
    print("Extracted HCC Codes:", extract_hcc_codes(sample_note))

    print("\nEntities Found:")
    for ent in nlp(sample_note).ents:
        print(f"{ent.text} → {ent.label_}")

import sys
import os

if __name__ == "__main__":
    print("✅ MAIN block entered")
    print("🧾 sys.argv =", sys.argv)

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        print("📄 Received filepath:", filepath)
        print("📂 Current working directory:", os.getcwd())
        print("📁 Files in this folder:", os.listdir())

        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                note = file.read()
                print("Extracted HCC Codes:", extract_hcc_codes(note))
        else:
            print("❌ File not found:", filepath)
    else:
        print("⚠️ No file passed, running fallback note.")
        sample_note = """
        65-year-old male with history of CHF, diabetes mellitus, and COPD.
        No signs of CKD or depression.
        """
        print("Extracted HCC Codes:", extract_hcc_codes(sample_note))

