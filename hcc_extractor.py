"""
hcc_extractor.py

A simple clinical NLP script to extract Hierarchical Condition Category (HCC) codes
from unstructured clinical text using keyword matching.

Author: Dr. Sushant Tapase
License: CC BY-NC-ND 4.0 — See LICENSE.md
"""

def extract_hcc_codes(note):
    """
    Extracts HCC codes from clinical text using basic keyword matching.

    Args:
        note (str): The unstructured clinical note (plain text).

    Returns:
        list: A list of matching HCC codes (e.g., ['HCC18', 'HCC85'])
    """

    # Mapping of clinical terms to HCC codes (expandable)
    hcc_keywords = {
        "diabetes": "HCC18",
        "copd": "HCC111",
        "chf": "HCC85",  # Congestive Heart Failure
        "ckd": "HCC134",  # Chronic Kidney Disease
        "chronic kidney disease": "HCC134",
        "heart failure": "HCC85"
    }

    note = note.lower()  # Normalize input text
    found_codes = set()

    for keyword, hcc in hcc_keywords.items():
        if keyword in note:
            found_codes.add(hcc)

    return list(found_codes)


# Optional demo block for direct script execution
if __name__ == "__main__":
    sample_note = """
    70-year-old male with a history of diabetes, CKD, and CHF.
    Mild COPD noted on spirometry.
    """
    codes = extract_hcc_codes(sample_note)
    print("Extracted HCC Codes:", codes)
