import gradio as gr
from hcc_extractor import extract_hcc_codes

def extract_codes_from_note(note):
    if note.strip():
        codes = extract_hcc_codes(note)
        if codes:
            return f"✅ Extracted HCC Codes: {', '.join(codes)}"
        else:
            return "⚠️ No HCC codes found."
    else:
        return "⚠️ Please enter a clinical note."

iface = gr.Interface(
    fn=extract_codes_from_note,
    inputs=gr.Textbox(lines=10, label="✍️ Clinical Note"),
    outputs="text",
    title="🧠 HCC Risk Code Extractor",
    description="Paste a clinical note and extract HCC risk codes using simple rule-based NLP."
)

if __name__ == "__main__":
    iface.launch()
