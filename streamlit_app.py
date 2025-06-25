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

# About box
st.markdown("""
<div class="box">
    <h3>🧠 HCC Risk Code Extractor</h3>
    <p>Paste clinical notes below to extract <b>Hierarchical Condition Categories (HCC)</b> using NLP.</p>
    <small>Built by <b>Dr. Sushant Tapase</b> — MBBS | M.Tech BMDS | Clinical NLP in action</small>
</div>
""", unsafe_allow_html=True)

# Session state
if "note" not in st.session_state:
    st.session_state.note = ""
if "extract_now" not in st.session_state:
    st.session_state.extract_now = False

    # How This Works
with st.expander("📘 How This Works"):
    st.markdown("""
    **HCC Extractor Overview**

    This tool uses **Natural Language Processing (NLP)** to scan clinical notes and identify key conditions that map to **Hierarchical Condition Categories (HCC)**.

    - 🔍 **Named Entity Recognition (NER):** Clinical terms are identified using spaCy's language model.
    - 🧠 **Keyword Mapping:** Matches terms like *diabetes*, *COPD*, *CHF*, etc. to their respective HCC codes.
    - ❌ **Negation Detection:** Terms like “no diabetes” are filtered out using simple rule-based logic.
    - 📤 **CSV Export:** Download HCC codes to use in clinical audits or population health analysis.

    **Use Case Example:**  
    This demo is useful in medical coding, chart review, or insurance risk adjustment settings where **accurate diagnosis capture** is critical.

    ---
    🔧 Built with:
    - Python · spaCy · Streamlit · Regex
    - Custom rule-based logic and open-source medical models
    """)


# Sample note
sample_text = """65-year-old male with history of CHF, diabetes mellitus, and COPD. 
No signs of CKD or depression. CAD is stable."""

col1, col2 = st.columns([1, 2])
with col1:
    if st.button("📋 Try Sample Note"):
        st.session_state.note = sample_text
        st.session_state.extract_now = True

with col2:
    st.session_state.note = st.text_area("✍️ Clinical Note", value=st.session_state.note, height=200, label_visibility="collapsed")

# Extract HCC codes
if st.button("🔍 Extract HCC Codes") or st.session_state.extract_now:
    if st.session_state.note.strip():
        codes = extract_hcc_codes(st.session_state.note)
        if codes:
            st.success(f"✅ Extracted HCC Codes: {', '.join(codes)}")
            df = pd.DataFrame({"HCC Code": codes})
            st.download_button("⬇️ Download HCC Codes CSV", df.to_csv(index=False), file_name="hcc_codes.csv", mime="text/csv")
        else:
            st.info("⚠️ No HCC codes found.")
    else:
        st.warning("Please enter a clinical note.")
    st.session_state.extract_now = False

# Credits & Licensing
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