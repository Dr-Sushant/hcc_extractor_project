import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import pandas as pd
from hcc_extractor import extract_hcc_codes

# Page config
st.set_page_config(page_title="🧠 HCC Risk Code Extractor", layout="centered")

# CSS styling
st.markdown("""
    <style>
        .stTextArea textarea { border-radius: 12px; }
        .stButton button { border-radius: 8px; }
        .stDownloadButton button { border-radius: 8px; background-color: #2c7be5; color: white; }
        .box {
            padding: 1rem;
            background-color: #f0f2f6;
            border-radius: 12px;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Info
st.sidebar.title("ℹ️ About This App")
st.sidebar.markdown("""
This tool extracts **Hierarchical Condition Category (HCC)** codes from clinical text using simple NLP logic.

Built with ❤️ by **Dr. Sushant Tapase**  
🧠 M.Tech Biomedical Data Science  
🔗 [GitHub Project](https://github.com/your-username/hcc_code_extractor)
""")

# About box
st.markdown("""
<div class="box">
    <h3>🧠 HCC Risk Code Extractor</h3>
    <p>Paste or upload clinical notes to extract <b>Hierarchical Condition Categories (HCC)</b> using NLP.</p>
    <small>Built by <b>Dr. Sushant Tapase</b> — MBBS | M.Tech BMDS | Clinical NLP in action</small>
</div>
""", unsafe_allow_html=True)

# How to Use box
st.markdown("""
<div class="box">
    <h4>📖 How to Use</h4>
    <ol>
        <li>Paste a clinical note or upload a file (TXT/CSV).</li>
        <li>Click <b>“Extract HCC Codes”</b> to view matched phrases.</li>
        <li>Use the 📋 button to try a sample note.</li>
        <li>Download the result CSV file.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Sample text
sample_text = """65-year-old male with history of CHF, diabetes mellitus, and COPD. 
No signs of CKD or depression. CAD is stable."""

# Session state
if "note" not in st.session_state:
    st.session_state.note = ""
if "extract_now" not in st.session_state:
    st.session_state.extract_now = False

# Upload section
st.subheader("📂 Upload Clinical Notes")
uploaded_file = st.file_uploader("Upload a TXT or CSV file", type=["txt", "csv"])

note_df = pd.DataFrame()

if uploaded_file:
    if uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
        note_df = pd.DataFrame([{"Note": text}])
    elif uploaded_file.type == "text/csv":
        note_df = pd.read_csv(uploaded_file)
        if "Note" not in note_df.columns:
            st.error("CSV must have a column named 'Note'")
            note_df = pd.DataFrame()

# Paste box and sample button
st.subheader("📝 Or Paste a Note")
col1, col2 = st.columns([1, 2])
with col1:
    if st.button("📋 Try Sample Note"):
        st.session_state.note = sample_text
        st.session_state.extract_now = True

with col2:
    st.session_state.note = st.text_area("✍️ Clinical Note", value=st.session_state.note, height=200, label_visibility="collapsed")

# Extract HCC codes logic
st.subheader("🔍 Extract HCC Codes")
if st.button("🚀 Run Extraction") or st.session_state.extract_now:
    combined_notes = []

    # If file upload present
    if not note_df.empty:
        combined_notes = note_df["Note"].tolist()

    # If user also pasted one note
    if st.session_state.note.strip():
        combined_notes.append(st.session_state.note)

    if not combined_notes:
        st.warning("Please paste a note or upload a file first.")
    else:
        all_results = []
        for idx, note in enumerate(combined_notes):
            matches = extract_hcc_codes(note)  # expected: list of (matched_phrase, hcc_code)
            for phrase, hcc_code, icd_code in matches:
                all_results.append({
                    "Note Index": idx,
                    "Matched Phrase": phrase,
                    "HCC Code": hcc_code,
                    "ICD-10 Code": icd_code
                })

        if all_results:
            df = pd.DataFrame(all_results)
            st.dataframe(df)

            # Download button
            st.download_button("⬇️ Download CSV", df.to_csv(index=False), file_name="hcc_results.csv", mime="text/csv")
        else:
            st.info("⚠️ No HCC codes found.")
            st.session_state.extract_now = False

# License section
with st.expander("⚖️ Usage Disclaimer & License"):
    st.markdown("""
    This project is provided **for educational and demonstration purposes only**.  
    You may **view and share** this app **with attribution**, but:

    - ❌ Modification  
    - ❌ Reuse in other tools or apps  
    - ❌ Commercial or clinical use  

    ...is **strictly prohibited** under the license terms.

    ---
    © 2025 Dr. Sushant Tapase  
    Licensed under **[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)**  
    See `LICENSE` file for details.
    """)


