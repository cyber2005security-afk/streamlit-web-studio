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

soc_theme_css = (
    "<style>[data-testid='stAppViewContainer'] { background:"
    " linear-gradient(135deg, #090d16 0%, #111827 100%); color: #f8fafc; }"
    " [data-testid='stSidebar'] { background-color: #0f172a; border-right:"
    " 1px solid #1e293b; } h1, h2, h3 { color: #38bdf8 !important; font-family:"
    " 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; } .stButton>button {"
    " background: linear-gradient(90deg, #1d4ed8 0%, #2563eb 100%); color:"
    " #ffffff; border: 1px solid #3b82f6; border-radius: 6px; font-weight: bold;"
    " } .stButton>button:hover { background: linear-gradient(90deg, #2563eb 0%,"
    " #1d4ed8 100%); border-color: #60a5fa; }</style>"
)
st.markdown(soc_theme_css, unsafe_allow_html=True)

with st.sidebar:
  st.title("🌐 Language / اللغة")
  lang = st.selectbox("اختر لغة العرض / Choose Language
