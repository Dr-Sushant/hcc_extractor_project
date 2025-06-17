# hcc_extractor.py

def extract_hcc_codes(note):
    """
    Extracts HCC codes based on simple keyword matching.
    Returns a list of HCC codes as strings.
    """
    # Simple keyword-to-HCC mapping (extend this as needed)
    hcc_keywords = {
        "diabetes": "HCC18",
        "copd": "HCC111",
        "chf": "HCC85",  # congestive heart failure
        "ckd": "HCC134",  # chronic kidney disease
        "chronic kidney disease": "HCC134",
        "heart failure": "HCC85"
    }

    note = note.lower()
    found_codes = set()

    for keyword, hcc in hcc_keywords.items():
        if keyword in note:
            found_codes.add(hcc)

    return list(found_codes)

