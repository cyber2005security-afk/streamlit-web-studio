import hashlib
import platform
import re
import sys
import time
from PIL import Image
import streamlit as st

# إعدادات الصفحة بتصميم واسع
st.set_page_config(
    page_title="SOC Operations Center - Fadil I. Hussein",
    page_icon="🛡️",
    layout="wide",
)

# تصميم واجهة عالي الجمالية (Dark Cyber Theme)
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
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    .stButton>button {
        background: linear-gradient(90deg, #1d4ed8 0%, #2563eb 100%);
        color: #ffffff;
        border: 1px solid #3b82f6;
        border-radius: 8px;
        font-weight: bold;
        box-shadow: 0 4px 12px rgba(29, 78, 216, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
        box-shadow: 0 6px 16px rgba(37, 99, 235, 0.5);
        border-color: #60a5fa;
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #1e293b;
        color: #f3f4f6;
        border: 1px solid #334155;
        border-radius: 6px;
    }
</style>
"""
st.markdown(cyber_css, unsafe_allow_html=True)

# إدارة جلسة تسجيل الدخول (Session State)
if "logged_in" not in st.session_state:
  st.session_state.logged_in = False
if "username" not in st.session_state:
  st.session_state.username = ""
if "role" not in st.session_state:
  st.session_state.role = ""

# القائمة الجانبية (نظام الدخول ومعلومات المستخدم)
with st.sidebar:
  st.title("🌐 Language / اللغة")
  lang = st.selectbox("اختر لغة العرض:", ["العربية", "English"])
  st.divider()

  st.subheader("👤 بوابة المستخدم (Login)")
  if not st.session_state.logged_in:
    input_user = st.text_input("اسم المستخدم (Username):")
    input_pass = st.text_input("كلمة المرور (Password):", type="password")
    user_role = st.selectbox(
        "الصلاحية / Role:", ["محلل أمني (SOC Analyst)", "مدير نظام (Admin)"]
    )

    if st.button("تسجيل الدخول / Login"):
      if input_user.strip() != "":
        st.session_state.logged_in = True
        st.session_state.
