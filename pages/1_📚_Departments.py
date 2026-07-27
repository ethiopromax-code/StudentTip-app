import streamlit as st

st.markdown("### 📚 የትምህርት ክፍሎች እና የሞጁል ጽሁፎች (Modules & PDFs)")

dept = st.selectbox("የጥናት ዘርፍ ይምረጡ", ["ICT - Hardware & Networking", "Accounting", "Building Electrical Installation"])
level = st.selectbox("ደረጃ (Level) ይምረጡ", ["Level 1", "Level 2", "Level 3", "Level 4"])

st.markdown(f"""
    <div style='background: #1e293b; padding: 15px; border-radius: 10px; border: 1px solid #334155;'>
        <h4>ማቴሪያሎች ለ {dept} - {level}</h4>
        <p>የጥናት መመሪያዎች እና ማስተማሪያ ሰነድ እዚህ አለ።</p>
    </div>
""", unsafe_allow_html=True)

st.download_button(
    label=f"📥 {level} የ PDF ሞጁል አውርድ",
    data=f"ይህ የ Student-Tip የ {dept} - {level} ኦፊሴላዊ የትምህርት ሞጁል ሰነድ ነው።",
    file_name=f"{dept}_{level}_Module.pdf",
    mime="text/plain"
)
