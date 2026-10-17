import hashlib
import platform
import re
import sys
import time
from PIL import Image
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="SOC Operations Center - Fadil I. Hussein",
    page_icon="🛡️",
    layout="wide",
)

# تصميم الواجهة
soc_theme_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0f172a;
    color: #f8fafc;
}
[data-testid="stSidebar"] {
    background-color: #1e293b;
    border-right: 1px solid #334155;
}
h1, h2, h3 {
    color: #38bdf8 !important;
}
.stButton>button {
    background-color: #1d4ed8;
    color: #ffffff;
    border-radius: 6px;
    font-weight: bold;
}
</style>
"""
st.markdown(soc_theme_css, unsafe_allow_html=True)

# القائمة الجانبية
with st.sidebar:
  st.title("🌐 Language / اللغة")
  lang = st.selectbox("اختر اللغة:", ["العربية", "English"])
  st.divider()
  st.subheader("Fadil I. Hussein")
  st.write("🎓 **Cybersecurity Sciences**")
  st.write("🏛️ Al-Qadisiyah University")

# العناوين بحسب اللغة
if lang == "العربية":
  st.title("🛡️ غرفة عمليات الأمان السيبراني (SOC)")
  st.markdown(
      "مهندس النظام والمشرف: **Fadil I. Hussein** [مركز العمليات النشط]"
  )
  tabs_names = [
      " نبض النظام",
      " ذكاء الاصطناعي",
      " فحص الروابط",
      " أمان المصادقة",
      " لغات البرمجة",
      " صيد الثغرات",
      " برمجيات الفدية",
      " ضغط الشبكة",
      " تحليل الصور",
      " التشفير",
      " كلمات المرور",
      " الأكواد",
  ]
else:
  st.title("🛡️ Security Operations Center (SOC)")
  st.markdown("System Architect & Lead: **Fadil I. Hussein**")
  tabs_names = [
      " System Pulse",
      " AI Analysis",
      " URL Scanner",
      " Auth Security",
      " Code Studio",
      " Bug Bounty",
      " Ransomware",
      " Network Stress",
      " Image Forensics",
      " Cryptography",
      " Pass Protection",
      " Code Library",
  ]

st.divider()
tabs = st.tabs(tabs_names)

# Tab 1: System Info
with tabs[0]:
  st.subheader("معلومات الخادم وحالة النظام")
  
