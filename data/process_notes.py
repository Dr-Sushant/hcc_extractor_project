import os
import pandas as pd
from hcc_extractor import extract_hcc_codes

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def process_clinical_notes(input_csv, output_csv):
    input_path = os.path.join(BASE_DIR, input_csv)
    output_path = os.path.join(BASE_DIR, output_csv)

    print("🔍 Reading from:", input_path)
    
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        print(f"❌ File not found: {input_path}")
        return
    except pd.errors.EmptyDataError:
        print(f"⚠️ File is empty: {input_path}")
        return
    except Exception as e:
        print(f"🔥 Unexpected error reading {input_path}: {e}")
        return

    df['hcc_codes'] = df['notes'].apply(lambda note: ','.join(extract_hcc_codes(note)))
    
    try:
        df.to_csv(output_path, index=False)
        print("✅ Done. Output at:", output_path)
    except Exception as e:
        print(f"❌ Failed to write to {output_path}: {e}")

if __name__ == "__main__":
    process_clinical_notes("data/clinical_notes.csv", "data/clinical_notes_with_hcc.csv")

