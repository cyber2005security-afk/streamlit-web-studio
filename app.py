import hashlib
import platform
import sys
import time
import io
import contextlib
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
    " 1px solid #1e293b; } h1, h2, h3 { color: #38bdf8 !important; }</style>"
)
st.markdown(soc_theme_css, unsafe_allow_html=True)

with st.sidebar:
    st.title("Language / اللغة")
    lang = st.selectbox("اختر اللغة:", ["العربية", "English"])
    st.divider()
    st.title("🛡️ SOC Profile")
    st.subheader("Fadil I. Hussein")
    st.write("🎓 Cybersecurity Sciences")
    st.write("🏛️ Al-Qadisiyah University")

if lang == "العربية":
    t_title = "غرفة عمليات الأمان السيبراني (SOC)"
    t_sub = "مهندس النظام والمشرف: Fadil I. Hussein"
    tabs_names = [
        "💻 نبض النظام",
        "🤖 الذكاء الاصطناعي",
        "🖥️ محرر الأكواد (Live Code)",
        "🦈 أدوات Wireshark",
        "⚡ أدوات DoS / DDoS",
        "🎭 الهندسة الاجتماعية",
        "🔍 فحص الروابط",
        "💰 صيد الثغرات",
        "🔒 برمجيات الفدية",
        "🖼️ تحليل الصور",
        "🔐 التشفير",
        "🧮 حماية الحسابات",
    ]
else:
    t_title = "Security Operations Center (SOC)"
    t_sub = "System Architect & Lead:
