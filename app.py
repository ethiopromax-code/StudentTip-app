import streamlit as st

st.set_page_config(page_title="Student-Tip", page_icon="📚", layout="centered")

st.markdown("""
    <div style='background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 20px; border-radius: 12px; text-align: center; border: 1px solid #334155;'>
        <h1 style='color: #38bdf8; margin-bottom: 5px; font-size: 24px;'>Student-Tip Platform</h1>
        <p style='color: #94a3b8; margin: 0; font-size: 14px;'>የአስተርዮ አካባቢ ተማሪዎች መረጃ ማግኛ መድረክ</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("### ⛅ የአስተርዮ አካባቢ የአየር ሁኔታ")
st.info("የአየር ሁኔታ፡ 24°C - መለስተኛ ፀሐያማ እና ደመናማ (Partly Cloudy)።")

st.markdown("---")
st.markdown("### 📢 የዕለቱ ዋና ዋና ዜናዎች")

# ዜናዎችን በጊዜያዊነት ለመያዝ
if 'news_list' not in st.session_state:
    st.session_state.news_list = [
        {
            "title": "የአንደኛ ሴሚስተር ፈተና መርሃ-ግብር",
            "content": "ለሁሉም ደረጃ 3 እና 4 ተማሪዎች፦ የፈተና መርሃ-ግብር ከዚህ ሳምንት ጀምሮ ይለቀቃል።"
        }
    ]

# አስተዳዳሪ ዜና የሚለቀቅበት ክፍል
with st.expander("➕ አዲስ ዜና ለመልቀቅ (Admin Post)"):
    admin_pass = st.text_input("የአስተዳዳሪ የይለፍ ቃል (Password)", type="password")
    if admin_pass == "admin123":
        with st.form("news_form"):
            p_title = st.text_input("የዜናው ርዕስ")
            p_content = st.text_area("የዜናው ዝርዝር ጽሁፍ")
            submitted = st.form_submit_button("ለቀቅ (Publish)")
            if submitted and p_title:
                st.session_state.news_list.insert(0, {"title": p_title, "content": p_content})
                st.success("ዜናው ተለቀቀ!")
    elif admin_pass != "":
        st.error("የተሳሳተ የይለፍ ቃል!")

# ዜናዎችን ማሳየት
for news in st.session_state.news_list:
    st.markdown(f"""
        <div style='background: #1e293b; padding: 15px; border-radius: 10px; margin-bottom: 10px; border: 1px solid #334155;'>
            <h4 style='color: #38bdf8; margin-top: 0;'>{news['title']}</h4>
            <p style='color: #cbd5e1;'>{news['content']}</p>
        </div>
    """, unsafe_allow_html=True)
