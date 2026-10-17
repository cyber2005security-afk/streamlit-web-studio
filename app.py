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
    background-color: #1e293b;
    border-right: 1px solid #334155;
}
h1, h2, h3 {
    color: #38bdf8 !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.stButton>button {
    background: linear-gradient(90deg, #1d4ed8 0%, #2563eb 100%);
    color: #ffffff;
    border: 1px solid #3b82f6;
    border-radius: 6px;
    font-weight: bold;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #2563eb 0%, #1d4ed8 100%);
    border-color: #60a5fa;
}
</style>
"""
st.markdown(soc_theme_css, unsafe_allow_html=True)

# إدارة حالة تسجيل الدخول (Session State)
if "logged_in" not in st.session_state:
  st.session_state.logged_in = False
if "username" not in st.session_state:
  st.session_state.username = ""
if "google_email" not in st.session_state:
  st.session_state.google_email = ""

# 2. القائمة الجانبية (Language, Login & Profile)
with st.sidebar:
  st.title("🌐 Language / اللغة")
  lang = st.selectbox("اختر لغة العرض / Choose Language:", ["العربية", "English"])
  st.divider()

  # بوابة تسجيل الدخول
  st.subheader("👤 بوابة المستخدم (Login)")
  if not st.session_state.logged_in:
    input_user = st.text_input("اسم المستخدم (Username):")
    input_pass = st.text_input("كلمة المرور (Password):", type="password")

    if st.button("تسجيل الدخول / Login"):
      if input_user.strip() != "":
        st.session_state.logged_in = True
        st.session_state.username = input_user
        st.rerun()
      else:
        st.warning("⚠️ يرجى إدخال اسم المستخدم.")

    st.markdown("---")
    if st.button("🔴 تسجيل الدخول عبر Google"):
      st.session_state.logged_in = True
      st.session_state.username = "Fadil I. Hussein"
      st.session_state.google_email = "fadil.hussein@gmail.com"
      st.rerun()
  else:
    st.success(f"مرحباً، **{st.session_state.username}**!")
    if st.session_state.google_email:
      st.info(f"📧 Google: {st.session_state.google_email}")
    if st.button("تسجيل الخروج / Logout"):
      st.session_state.logged_in = False
      st.session_state.username = ""
      st.session_state.google_email = ""
      st.rerun()

  st.divider()
  st.title("🛡️ SOC Profile")
  st.subheader("Fadil I. Hussein")
  st.write("🎓 **Cybersecurity Sciences**")
  st.write("🏛️ Al-Qadisiyah University")
  st.divider()
  st.caption("🔒 Operations Center Core")

# حماية التطبيق (التحقق من تسجيل الدخول)
if not st.session_state.logged_in:
  st.warning(
      "⚠️ يرجى تسجيل الدخول أو استخدام المصادقة عبر القائمة الجانبية (Sidebar)"
      " للوصول إلى غرفة العمليات."
  )
  st.stop()

# نصوص الواجهة بناءً على اللغة المختارة
if lang == "العربية":
  t_main_title = "🛡️ غرفة عمليات الأمان السيبراني (SOC)"
  t_subtitle = (
      f"مهندس النظام والمشرف: **Fadil I. Hussein** | المستخدم النشط:"
      f" **{st.session_state.username}**"
  )
  t_desc = (
      "لوحة تحكم سيبرانية متكاملة لإدارة التهديدات، تحليل الحزم، ورصد الحماية."
  )
  tabs_names = [
      "💻 نبض النظام",
      "🤖 تحليل الذكاء الاصطناعي",
      "💻 لغات البرمجة",
      "🎣 فحص التصيد",
      "🌐 بيانات Google OAuth",
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
      f"System Architect & Lead: **Fadil I. Hussein** | Active User:"
      f" **{st.session_state.username}**"
  )
  t_desc = (
      "Comprehensive cyber command center for threat management, packet"
      " analysis, and defense."
  )
  tabs_names = [
      "💻 System Pulse",
      "🤖 AI Security Analysis",
      "💻 Code Studio",
      "🎣 Phishing Analyzer",
      "🌐 Google OAuth Data",
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

# التبويبات الرئيسية الأفقية
tabs = st.tabs(tabs_names)

# ---------------------------------------------------------
# Tab 1: System Info
# ---------------------------------------------------------
with tabs[0]:
  st.subheader("💻 معلومات الخادم وحالة غرفة العمليات")
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
# Tab 2: AI Security Analysis
# ---------------------------------------------------------
with tabs[1]:
  st.subheader(
      "🤖 أداة تحليل السلوك والتهديدات بالذكاء الاصطناعي (AI Threat Detection)"
  )
  st.write(
      "تستخدم هذه الأداة خوارزميات التعلم الآلي لتحليل سلوك الشبكة واكتشاف"
      " الهجمات غير المعروفة تلق
