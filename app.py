import streamlit as st

st.set_page_config(page_title="Student-Tip", page_icon="📚", layout="centered")

st.markdown("""
    <div style='background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #334155;'>
        <h1 style='color: #38bdf8; margin-bottom: 5px; font-size: 24px;'>Student-Tip Platform</h1>
        <p style='color: #94a3b8; margin: 0; font-size: 14px;'>የአስተርዮ አከባቢ ተማሪዎች መረጃ ማግኛ መድረክ</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("### ⛅ የአስተርዮ አካባቢ የአየር ሁኔታ")
st.info("የአየር ሁኔታ፡ 24°C - መለስተኛ ፀሐያማ እና ደመናማ (Partly Cloudy)።")

st.markdown("---")
st.markdown("### 📢 የዕለቱ ዋና ዋና ዜናዎች")
st.markdown("""
    <div style='background: #1e293b; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #334155;'>
        <h4 style='color: #38bdf8; margin-top: 0;'>የአንደኛ ሴሚስተር ፈተና መርሃ-ግብር</h4>
        <p style='color: #cbd5e1;'>ለሁሉም ደረጃ 3 እና 4 ተማሪዎች፦ የፈተና መርሃ-ግብር ከዚህ ሳምንት ጀምሮ ይለቀቃል።</p>
    </div>
""", unsafe_allow_html=True)
