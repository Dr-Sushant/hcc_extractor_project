# 🩺 Clinical ICD-10 Extractor

A lightweight clinical NLP application that extracts **ICD-10 diagnosis codes** from free-text clinical notes and maps them to corresponding **HCC (Hierarchical Condition Category) risk categories**.

🚀 **Live Demo**

https://huggingface.co/spaces/Dr-Sushant/hcc-extractor

---

# 👨‍⚕️ About the Author

**Dr. Sushant Tapase**

MBBS | Clinical Research | MBA (Healthcare & Hospital Management) | M.Tech Biomedical Data Science

This project demonstrates practical applications of clinical NLP, healthcare coding, and rule-based information extraction from unstructured medical text.

---

# 💡 Project Objective

Healthcare documentation is largely unstructured.

This project demonstrates how clinical notes can be automatically analyzed to identify diagnosis concepts and map them to ICD-10 codes and HCC risk categories using a lightweight rule-based NLP pipeline.

The application accepts either:

* Free-text clinical notes
* Direct ICD-10 code input

and returns structured coding information.

---

# 🌟 Features

✅ Clinical note processing

✅ ICD-10 diagnosis code extraction

✅ HCC risk category mapping

✅ Multiple condition detection

✅ Direct ICD-10 code input support

✅ Interactive Streamlit interface

✅ Hugging Face deployment

---

# 🔬 Sample Workflow

Clinical Note

⬇️

Condition Detection

⬇️

ICD-10 Mapping

⬇️

HCC Mapping

⬇️

Structured Output

---

# 🧪 Demo Clinical Notes

## Example 1 – Diabetes

Patient has type 2 diabetes mellitus and requires regular monitoring.

**Expected Detection**

ICD-10: E11.9

HCC: 19

---

## Example 2 – Chronic Kidney Disease

Patient diagnosed with chronic kidney disease stage 3.

**Expected Detection**

ICD-10: N18.3

HCC: 138

---

## Example 3 – HIV

HIV-positive patient with declining CD4 count.

**Expected Detection**

ICD-10: B20

HCC: 1

---

## Example 4 – Leukemia

Acute myeloid leukemia diagnosed following bone marrow biopsy.

**Expected Detection**

ICD-10: C92.00

HCC: 8

---

## Example 5 – Multiple Conditions

Patient has type 2 diabetes mellitus and chronic kidney disease stage 3.

**Expected Detection**

ICD-10: E11.9 → HCC: 19

ICD-10: N18.3 → HCC: 138

---

## Example 6 – ICD-10 Direct Input

E11.9, N18.3

**Expected Detection**

Diabetes

Chronic Kidney Disease

---

# 🛠️ Technology Stack

* Python
* Pandas
* Regular Expressions (Regex)
* Streamlit
* Clinical Coding Logic
* ICD-10 Mapping
* HCC Risk Mapping

---

# 📁 Repository Structure

```text
hcc-extractor/
│
├── app.py
├── hcc_extractor.py
├── icd_hcc_cleaned.csv
├── requirements.txt
├── README.md
│
├── data/
│   └── sample_input.txt
│
└── sample_note.txt
```

---

# 🎯 Potential Applications

* Clinical NLP Demonstrations
* Medical Coding Education
* ICD-10 Training
* Healthcare Analytics
* Risk Adjustment Workflows
* Clinical Documentation Improvement (CDI)
* Healthcare AI Prototyping

---

# ⚠️ Disclaimer

This project is intended for educational and demonstration purposes only.

It is not certified for clinical decision support, diagnosis, reimbursement, regulatory reporting, or production healthcare use.

---

# 📄 License

MIT License
