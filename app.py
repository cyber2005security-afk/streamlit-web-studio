import base64
import hashlib
import platform
import random
import re
import string
import sys
import time
from PIL import Image
import streamlit as st

# 1. إعدادات الصفحة والتصميم
st.set_page_config(
    page_title="SOC Operations Center - Fadil I. Hussein",
    page_icon="🛡️",
    layout="wide",
)

# تخصيص CSS
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
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.stButton>button {
    background-color: #1d4ed8;
    color: #ffffff;
    border: 1px solid #3b82f6;
    border-radius: 6px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #2563eb;
    border-color: #60a5fa;
}
</style>
"""
st.markdown(soc_theme_css, unsafe_allow_html=True)

# 2. القائمة الجانبية واختيار اللغة
with st.sidebar:
  st.title("🌐 Language / اللغة")
  lang = st.selectbox("اختر لغة العرض / Choose Language:", ["العربية", "English"])
  st.divider()
  st.title("🛡️ SOC Profile")
  st.subheader("Fadil I. Hussein")
  st.write("🎓 **Cybersecurity Sciences**")
  st.write("🏛️ Al-Qadisiyah University")
  st.divider()
  st.caption("🔒 Operations Center Core v7.5")

# نصوص الواجهة
if lang == "العربية":
  t_main_title = "🛡️ غرفة عمليات الأمان السيبراني (SOC)"
  t_subtitle = "مهندس النظام والمشرف: **Fadil I. Hussein** [مركز العمليات النشط]"
  
