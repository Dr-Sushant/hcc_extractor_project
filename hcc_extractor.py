import re

def is_negated(phrase: str, text: str) -> bool:
    """
    Checks for negation patterns (e.g., 'no diabetes', 'denies asthma').
    Looks for negation words within 3 words before the phrase.
    """
    pattern = r"(no|denies|without)\s+(\w+\s*){0,3}" + re.escape(phrase)
    return bool(re.search(pattern, text.lower()))

def extract_hcc_codes(clinical_note: str) -> list:
    """
    Extract matched phrases with HCC and ICD-10 codes.
    """
    text = clinical_note.lower()
    matches = []

    # Phrase → (HCC code, ICD-10 code)
    hcc_full_dict = {
        "diabetes mellitus": ("HCC18", "E11.9"),
        "diabetes": ("HCC18", "E11.9"),
        "chronic kidney disease": ("HCC134", "N18.9"),
        "ckd": ("HCC134", "N18.9"),
        "copd": ("HCC111", "J44.9"),
        "congestive heart failure": ("HCC85", "I50.9"),
        "chf": ("HCC85", "I50.9"),
        "hypertension": ("HCC96", "I10"),
        "asthma": ("HCC112", "J45.909"),
        "stroke": ("HCC100", "I63.9"),
        "depression": ("HCC77", "F32.9"),
        "coronary artery disease": ("HCC96", "I25.10"),
        "cad": ("HCC96", "I25.10"),
        "alzheimer": ("HCC51", "G30.9")
    }

    for phrase, (hcc_code, icd_code) in hcc_full_dict.items():
        if phrase in text:
            if not is_negated(phrase, text):
                matches.append((phrase, hcc_code, icd_code))

    return matches


