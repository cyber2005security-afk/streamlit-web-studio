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
  t_sub = "System Architect & Lead: Fadil I. Hussein"
  tabs_names = [
      "💻 System Pulse",
      "🤖 AI Security",
      "🖥️ Live Code Studio",
      "🦈 Wireshark Tools",
      "⚡ DoS / DDoS Lab",
      "🎭 Social Engineering",
      "🔍 URL Scanner",
      "💰 Bug Bounty",
      "🔒 Ransomware",
      "🖼️ Image Forensics",
      "🔐 Cryptography",
      "🧮 Pass Security",
  ]

st.title(f"🛡️ {t_title}")
st.markdown(f"### {t_sub}")
st.divider()

tabs = st.tabs(tabs_names)

# Tab 0: System Pulse
with tabs[0]:
  st.subheader("💻 معلومات الخادم وحالة غرفة العمليات")
  c1, c2, c3 = st.columns(3)
  start_time = time.time()
  _ = 1 + 1
  latency = round((time.time() - start_time) * 1000, 2)
  c1.metric("إصدار بايثون", sys.version.split()[0])
  c2.metric("حالة النظام", "ONLINE [SECURE]")
  c3.metric("مستوى التشفير", "AES-256")

# Tab 1: AI Threat Detection
with tabs[1]:
  st.subheader("🤖 تحليل السلوك والتهديدات بالذكاء الاصطناعي")
  traffic = st.slider("معدل نقل بيانات الشبكة (MB/s):", 10, 1000, 150)
  fails = st.slider("محاولات الدخول الفاشلة:", 0, 50, 2)
  if st.button("تشغيل فحص الذكاء الاصطناعي"):
    if traffic > 700 or fails > 15:
      st.error("🚨 تنبيه: تم رصد سلوك شبكي شاذ أو هجوم محتمل!")
    else:
      st.success("✅ حالة الأمان مستقرة وسلوك الشبكة طبيعي.")

# Tab 2: Live Executable Code Editor
with tabs[2]:
  st.subheader("🖥️ محرر كود بايثون التفاعلي (Interactive Code Executor)")
  st.write("اكتب كود بايثون وشغّله مباشرة لاستعراض النتائج:")
  default_code = """# كود بايثون لاختبار الأدوات السيبرانية
import math

def check_ip_validity(ip):
    parts = ip.split('.')
    if len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts):
        return True
    return False

test_ip = "192.168.1.1"
print(f"IP Status ({test_ip}):", check_ip_validity(test_ip))
"""
  user_code = st.text_area("محرر الأكواد:", value=default_code, height=220)
  if st.button("▶️ تشغيل الكود (Run Code)"):
    output_buffer = io.StringIO()
    try:
      with contextlib.redirect_stdout(output_buffer):
        exec(user_code, {})
      st.subheader("🖥️ مخرجات التنفيذ (Output):")
      st.code(output_buffer.getvalue(), language="text")
    except Exception as e:
      st.error(f"❌ حدث خطأ في التنفيذ:\n{e}")

# Tab 3: Wireshark Packet Analysis Tool
with tabs[3]:
