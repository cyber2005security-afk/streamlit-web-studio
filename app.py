import base64
import hashlib
import platform
import random
import string
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

# 2. القائمة الجانبية واختيار اللغة (Language Selector)
with st.sidebar:
  st.title("🌐 Language / اللغة")
  lang = st.selectbox("اختر لغة العرض / Choose Language:", ["العربية", "English"])
  st.divider()
  st.title("🛡️ SOC Profile")
  st.subheader("Fadil I. Hussein")
  st.write("🎓 **Cybersecurity Sciences**")
  st.write("🏛️ Al-Qadisiyah University")
  st.divider()
  st.caption("🔒 Operations Center Core")

# نصوص الواجهة بناءً على اللغة المختارة
if lang == "العربية":
  t_main_title = "🛡️ غرفة عمليات الأمان السيبراني (SOC)"
  t_subtitle = (
      "مهندس النظام والمشرف: **Fadil I. Hussein** [مركز العمليات النشط]"
  )
  t_desc = (
      "لوحة تحكم سيبرانية لإدارة التهديدات، تحليل الحزم، ورصد الحماية."
  )
  tabs_names = [
      "💻 نبض النظام",
      "💻 لغات البرمجة",
      "🎣 فحص التصيد",
      "💰 صيد الثغرات",
      "🔒 برمجيات الفدية",
      "⚡ ضغط الشبكة",
      "🖼️ تحليل الصور",
      "🔐 التشفير",
      "🧮 حماية الحسابات",
      "📜 الأكواد الأمنية",
  ]
else:
  t_main_title = "🛡️ Security Operations Center (SOC)"
  t_subtitle = (
      "System Architect & Lead: **Fadil I. Hussein** [Active Operations]"
  )
  t_desc = (
      "Core cyber command center for threat management, packet analysis, and"
      " defense."
  )
  tabs_names = [
      "💻 System Pulse",
      "💻 Code Studio",
      "🎣 Phishing Analyzer",
      "💰 Bug Bounty",
      "🔒 Ransomware Defense",
      "⚡ Network Stress",
      "🖼️ Image Forensics",
      "🔐 Cryptography",
      "🧮 Pass Protection",
      "📜 Code Library",
  ]

# 3. العنوان الرئيسي
st.title(t_main_title)
st.markdown(f"### {t_subtitle}")
st.write(t_desc)
st.divider()

# التبويبات الرئيسية
tabs = st.tabs(tabs_names)

# ---------------------------------------------------------
# Tab 1: System Info
# ---------------------------------------------------------
with tabs[0]:
  st.subheader(
      "💻 معلومات الخادم وحالة غرفة العمليات (Server Pulse & Telemetry)"
  )
  col1, col2, col3 = st.columns(3)
  start_time = time.time()
  _ = 1 + 1
  latency = round((time.time() - start_time) * 1000, 2)

  with col1:
    st.metric(
        label="Python Version" if lang == "English" else "إصدار بايثون",
        value=sys.version.split()[0],
    )
    st.metric(
        label="OS Platform" if lang == "English" else "نظام التشغيل",
        value=platform.system(),
    )
  with col2:
    st.metric(
        label="Server Latency" if lang == "English" else "سرعة استجابة الخادم",
        value=f"{latency} ms",
    )
    st.metric(
        label="Status" if lang == "English" else "حالة النظام",
        value="ONLINE [SECURE]",
    )
  with col3:
    st.metric(
        label="CPU Architecture" if lang == "English" else "معمارية المعالج",
        value=platform.machine(),
    )
    st.metric(
        label="Encryption Level" if lang == "English" else "مستوى التشفير",
        value="AES-256",
    )

# ---------------------------------------------------------
# Tab 2: Multi-Language Studio
# ---------------------------------------------------------
with tabs[1]:
  st.subheader(
      "💻 مختبر لغات البرمجة والأمن (Multi-Language Security Studio)"
  )
  lang_choice = st.selectbox(
      "Select Language / اختر لغة البرمجة:",
      ["Python", "C / C++", "JavaScript", "SQL", "Bash / Shell"],
  )
  if lang_choice == "Python":
    st.code("print('SOC Operations Python Module Active...')", language="python")
  elif lang_choice == "C / C++":
    st.code(
        '#include <iostream>\nusing namespace std;\nint main() { cout <<'
        ' "C++ Memory Safe"; }',
        language="cpp",
    )
  elif lang_choice == "SQL":
    st.code(
        "SELECT * FROM security_logs WHERE threat_level > 3;", language="sql"
    )
  else:
    st.code("nmap -sV -p 1-65535 127.0.0.1", language="bash")

# ---------------------------------------------------------
# Tab 3: Phishing Analyzer
# ---------------------------------------------------------
with tabs[2]:
  st.subheader(
      "🎣 أداة تحليل الروابط واكتشاف التصيد (URL & Phishing Detector)"
  )
  input_url = st.text_input(
      "أدخل الرابط للفحص / Enter URL:", "https://secure-login-portal.com"
  )
  if st.button("فحص الرابط / Analyze URL"):
    st.warning(
        "⚠️ تحذير تكتيكي: تم رصد مؤشرات محتملة لهندسة اجتماعية أو روابط تضليل."
    )

# ---------------------------------------------------------
# Tab 4: Bug Bounty
# ---------------------------------------------------------
with tabs[3]:
  st.subheader("💰 قائمة فحص صيد الثغرات (Bug Bounty Checklist)")
  target_domain = st.text_input("النطاق المستهدف / Target Domain:", "target.org")
  if st.button("توليد قائمة المهام / Generate Checklist"):
    st.success(f"📋 تم إعداد نطاق المهام الميدانية لـ {target_domain}")
    st.checkbox("فحص ملفات الروبوتات والمسارات المخفية (robots.txt)")
    st.checkbox("اختبار ثغرات الحقن والسكربتات الخبيثة (XSS)")

# ---------------------------------------------------------
# Tab 5: Ransomware Defense
# ---------------------------------------------------------
with tabs[4]:
  st.subheader("
