# HCC Extractor Project

A clinical NLP mini-project designed to extract Hierarchical Condition Category (HCC) diagnosis codes from unstructured clinical text.

## 💡 Objective

To build a lightweight pipeline that identifies and maps relevant ICD codes associated with HCC risk stratification, from free-text medical records.

## 🛠️ Tools & Libraries

- Python 3
- spaCy / NLTK
- Regex
- Pandas
- CSV / JSON for output

## 🧪 Sample Workflow

- **Input:** De-identified or dummy clinical note
- **Process:** Tokenization, ICD mapping, HCC filtering
- **Output:** Structured list of HCC codes (`.csv` or `.json`)

## 📌 Project Status

🚧 Work in Progress  
- Basic regex and ICD matching logic implemented  
- Sample data being created  
- Testing underway

## 📂 Directory Structure

```bash
hcc_extractor_project/
├── README.md
├── main.py or hcc_extractor.ipynb
├── sample_note.txt
├── output.csv
└── requirements.txt (optional)

