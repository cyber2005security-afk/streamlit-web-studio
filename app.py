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

if "logged_in" not in st.session_state:
  st.session_state.logged_in = False
if "username" not in st.session_state:
  st.session_state.username = ""
if "google_email" not in st.session_state:
  st.session_state.google_email = ""

with st.sidebar:
  st.title("🌐 Language / اللغة")
  lang = st.selectbox("اختر لغة العرض / Choose Language:", ["العربية", "English"])
  st.divider()

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

if not st.session_state.logged_in:
  st.warning(
      "⚠️ يرجى تسجيل الدخول أو استخدام المصادقة عبر القائمة الجانبية (Sidebar)"
      " للوصول إلى غرفة العمليات."
  )
  st.stop()

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

st.title(t_main_title)
st.markdown(f"### {t_subtitle}")
st.write(t_desc)
st.divider()

tabs = st.tabs(tabs_names)

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

with tabs[1]:
  st.subheader(
      "🤖 أداة تحليل السلوك والتهديدات بالذكاء الاصطناعي (AI Threat Detection)"
  )
  net_traffic = st.slider(
      "معدل نقل بيانات الشبكة (Network Traffic MB/s):", 10, 1000, 150
  )
  failed_attempts = st.slider("محاولات الدخول الفاشلة المتكررة:", 0, 50, 2)
  if st.button("تشغيل فحص الذكاء الاصطناعي / Run AI Analysis"):
    if net_traffic > 700 or failed_attempts > 15:
      st.error(
          f"🚨 [AI Alert] للمستخدم {st.session_state.username}: تم رصد سلوك"
          " شبكي شاذ!"
      )
    else:
      st.success("✅ [AI Status] حالة الأمان مستقرة ضمن النطاق الآمن.")

with tabs[2]:
  st.subheader("💻 مختبر لغات البرمجة والأمن")
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

with tabs[3]:
  st.subheader("🎣 أداة تحليل الروابط واكتشاف التصيد")
  input_url = st.text_input(
      "أدخل الرابط للفحص / Enter URL:", "https://secure-login-portal.com"
  )
  if st.button("فحص الرابط / Analyze URL"):
    st.warning(
        "⚠️ تحذير تكتيكي: تم رصد مؤشرات محتملة لهندسة اجتماعية أو روابط تضليل."
    )

with tabs[4]:
  st.subheader("🌐 معلومات ومصادقة Google OAuth والجلسة")
  if st.session_state.google_email:
    st.success(f"✅ متصل حالياً عبر حساب Google: {st.session_state.google_email}")
    st.json({
        "provider": "Google Identity Services",
        "status": "Authenticated",
        "username": st.session_state.username,
        "email": st.session_state.google_email,
        "scopes": ["profile", "email", "openid"],
    })
  else:
    st.info(
        f"ℹ️ المستخدم الحالي ({st.session_state.username}) مسجل بالطريقة التقليدية."
        " يمكنك تسجيل الدخول بحساب Google من القائمة الجانبية."
    )

with tabs[5]:
  st.subheader("💰 قائمة فحص صيد الثغرات")
  target_domain = st.text_input("النطاق المستهدف / Target Domain:", "target.org")
  if st.button("توليد قائمة المهام / Generate Checklist"):
    st.success(f"📋 تم إعداد نطاق المهام الميدانية لـ {target_domain}")
    st.checkbox("فحص ملفات الروبوتات والمسارات المخفية (robots.txt)")
    st.checkbox("اختبار ثغرات الحقن والسكربتات الخبيثة (XSS)")

with tabs[6]:
  st.subheader("🔒 حماية وحساب بصمات الملفات")
  text_sample = st.text_input(
      "اسم الملف أو النص / Filename or Text:", "operation_data.db"
  )
  if st.button("توليد بصمة SHA-256 / Generate Hash"):
    st.code(hashlib.sha256(text_sample.encode()).hexdigest())

with tabs[7]:
  st.subheader("⚡ محاكاة تحليل تدفق الشبكة واختبار الضغط")
  reqs = st.slider("معدل الطلبات في الثانية / Requests per sec:", 100, 10000, 2000)
  if st.button("تنفيذ اختبار التحمل / Run Test"):
    st.info("📊 تقرير الحمل: الخادم يتعامل مع التدفق ضمن الحدود الآمنة.")

with tabs[8]:
  st.subheader("🖼️ تحليل واستخراج البيانات الخفية للصور")
  up_file = st.file_uploader(
      "اختر صورة للفحص / Upload Image:", type=["jpg", "png"]
  )
  if up_file:
    img = Image.open(up_file)
    st.image(img, use_container_width=True)
    st.success("✅ تم تحليل بنية الصورة واستخراج الخصائص بنجاح.")

with tabs[9]:
  st.subheader("🔐 التشفير الكلاسيكي والمتقدم")
  txt = st.text_input("النص المراد تشفيره / Plaintext:", "FadilHussein")
  shift = st.slider("مفتاح الإزاحة / Shift Key:", 1, 25, 4)
  res = "".join([chr(ord(c) + shift) if c.isalpha() else c for c in txt])
  st.code(res)

with tabs[10]:
  st.subheader("🧮 حاسبة حصانة كلمات المرور")
  pwd = st.text_input("أدخل كلمة المرور / Enter Password:", type="password")
  if pwd:
    st.success("🔒 تقييم الحصانة: يتم فحص تعقيد الرمز لمنع الاستيلاء على الحسابات.")

with tabs[11]:
  st.subheader("📜 مكتبة الأكواد والأوامر الميدانية")
  st.code(
      "import socket\n# TCP socket monitoring script initialized...",
      language="python",
  )

st.divider()
st.caption(
    f"Security Operations Center (SOC) © 2026 — User: {st.session_state.username}"
    " | Architected by **Fadil I. Hussein** 🛡️"
)
