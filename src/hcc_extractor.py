import re

# Dictionary of example HCC codes and their patterns
HCC_PATTERNS = {
    'HCC1': r'\bcongestive heart failure\b|\bCHF\b',
    'HCC2': r'\bchronic obstructive pulmonary disease\b|\bCOPD\b',
    'HCC3': r'\bdiabetes mellitus\b|\bdiabetes\b',
    'HCC4': r'\brenal failure\b|\bchronic kidney disease\b|\bCKD\b',
}

def extract_hcc_codes(clinical_note: str) -> list:
    """
    Extracts HCC codes from a clinical note using simple regex pattern matching.

    Args:
        clinical_note (str): The unstructured clinical note text.

    Returns:
        list: List of matched HCC code strings (e.g., ['HCC1', 'HCC3'])
    """
    clinical_note = clinical_note.lower()
    found_codes = []

    for hcc_code, pattern in HCC_PATTERNS.items():
        if re.search(pattern, clinical_note):
            found_codes.append(hcc_code)

    return found_codes


# Demo block: this runs only when you run the file directly
if __name__ == "__main__":
    sample_note = """
    Patient is a 65-year-old male with history of CHF and diabetes mellitus.
    He has no signs of CKD but shows mild COPD on spirometry.
    """
    codes = extract_hcc_codes(sample_note)
    print("Extracted HCC Codes:", codes)
