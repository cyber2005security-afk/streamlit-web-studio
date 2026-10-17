import hashlib
import platform
import sys
import time
from PIL import Image
import streamlit as st

# 1. إعدادات الصفحة والتصميم الاحترافي لغرفة العمليات (SOC Theme)
st.set_page_config(
    page_title="SOC Operations Center - Fadil I. Hussein",
    page_icon="🛡️",
    layout="wide",
)

# تخصيص CSS لغرفة عمليات احترافية
soc_theme_css = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #090d16 0%, #111827 100%);
    color: #f8fafc;
}
[data-testid="stSidebar"] {
    background-color: #0f172a;
    border-right: 1px solid #1e293b;
}
h1, h2, h3 {
    color: #38bdf8 !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.stButton>button {
    background: linear-gradient(90deg,
