import os
import pandas as pd
from hcc_extractor import extract_hcc_codes

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def process_clinical_notes(input_csv, output_csv):
    input_path = os.path.join(BASE_DIR, input_csv)
    output_path = os.path.join(BASE_DIR, output_csv)

    print("🔍 Reading from:", input_path)
    df = pd.read_csv(input_path)
    df['hcc_codes'] = df['notes'].apply(lambda note: ','.join(extract_hcc_codes(note)))
    df.to_csv(output_path, index=False)
    print("✅ Done. Output at:", output_path)

if __name__ == "__main__":
    process_clinical_notes("data/clinical_notes.csv", "data/clinical_notes_with_hcc.csv")
import os
import pandas as pd
from hcc_extractor import extract_hcc_codes

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def process_clinical_notes(input_csv, output_csv):
    input_path = os.path.join(BASE_DIR, input_csv)
    output_path = os.path.join(BASE_DIR, output_csv)

    print("🔍 Reading from:", input_path)
    df = pd.read_csv(input_path)
    df['hcc_codes'] = df['notes'].apply(lambda note: ','.join(extract_hcc_codes(note)))
    df.to_csv(output_path, index=False)
    print("✅ Done. Output at:", output_path)

if __name__ == "__main__":
    process_clinical_notes("data/clinical_notes.csv", "data/clinical_notes_with_hcc.csv")
