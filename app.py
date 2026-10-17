import hashlib
import platform
import sys
import time
from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="SOC Operations Center - Fadil I. Hussein",
    page_icon="🛡️",
    layout="wide",
)

cyber_css = """
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #090d16 0%, #111827 100%);
        color: #f3f4f6;
    }
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #1e293b;
    }
    h1, h2, h3 {
        color: #38bdf8 !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #1d4ed8 0%, #2563eb 100%);
        color: #ffffff;
        border-radius: 8px;
        font-weight: bold;
    }
</style>
"""
st.markdown(cyber_css, unsafe_allow_html=True)

if "logged_in" not in st.session_state:
  st.session_state.logged_in = False
if "username" not in st.session_state:
  st.session_state.username = ""
if "role" not in st.session_state:
  st.session_state.role = ""

with st.sidebar:
  st.title("🌐 Language")
  lang = st.selectbox("اختر اللغة:", ["العربية", "English"])
  st.divider()
  st.subheader("👤 تسجيل الدخول")

  if not st.session_state.logged_in:
    u_name = st.text_input("اسم المستخدم:")
    u_pass = st.text_input("كلمة المرور:", type="password")
    u_role = st.selectbox("الصلاحية:", ["SOC Analyst", "Admin"])

    if st.button("دخول"):
      if u_name.strip():
        st.session_state.logged_in = True
        st.session_state.username = u_name
        st.session_state.role = u_role
        st.rerun()
      else:
        st.warning("الرجاء إدخال اسم المستخدم.")
  else:
    st.success(f"مرحباً: {st.session_state.username}")
    if st.button("خروج"):
      st.session_state.logged_in = False
      st.session_state.username = ""
      st.rerun()

  st.divider()
  st.write("Fadil I. Hussein")
  st.write("Cybersecurity Sciences")

if not st.session_state.logged_in:
  st.warning("⚠️ يرجى تسجيل الدخول من القائمة الجانبية للوصول إلى لوحة التحكم.")
  st.stop()

if lang == "العربية":
  st.title("🛡️ غرفة عمليات الأمان السيبراني (SOC)")
  st.markdown(
      f"المشرف: **Fadil I. Hussein** | المستخدم: **{st.session_state.username}**"
  )
  tabs_names = [
      "نبض النظام",
      "الذكاء الاصطناعي",
      "فحص الروابط",
      "المصادقة",
      "لغات البرمجة",
      "صيد الثغرات",
      "برمجيات الفدية",
      "ضغط الشبكة",
      "تحليل الصور",
      "التشفير",
      "كلمات المرور",
      "الأكواد",
  ]
else:
  st.title("🛡️ Security Operations Center (SOC)")
  st.markdown(
      f"Lead: **Fadil I. Hussein** | User: **{st.session_state.username}**"
  )
  tabs_names = [
      "System Pulse",
      "AI Analysis",
      "URL Scanner",
      "Auth Security",
      "Code Studio",
      "Bug Bounty",
      "Ransomware",
      "Network Stress",
      "Image Forensics",
      "Cryptography",
      "Pass Protection",
      "Code Library",
  ]

st.divider()
tabs = st.tabs(tabs_names)

with tabs[0]:
  st.subheader("معلومات الخادم")
  c1, c2, c3 = st.columns(3)
  c1.metric("إصدار بايثون", sys.version.split()[0])
  c2.metric("حالة النظام", "ONLINE [SECURE]")
  c3.metric("مستوى التشفير", "AES-256")

with tabs[1]:
  st.subheader("تحليل السلوك بالذكاء الاصطناعي")
  traffic = st.slider("حركة الشبكة (MB/s):", 10, 
