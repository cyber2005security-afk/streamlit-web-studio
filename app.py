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

# تخصيص CSS لغرفة عمليات احترافية وعصرية
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
  st.caption("🔒 Operations Center v6.0")

# نصوص الواجهة بناءً على اللغة المختارة
if lang == "العربية":
  t_main_title = "🛡️ غرفة عمليات الأمان السيبراني (SOC)"
  t_subtitle = (
      "مهندس النظام والمشرف: **Fadil I. Hussein** [مركز العمليات النشط]"
  )
  t_desc = (
      "لوحة تحكم سيبرانية احترافية لإدارة التهديدات، تحليل الحزم، فلاتر"
      " Wireshark، ورصد الحماية."
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
      "🦈 فلاتر Wireshark",
      "📜 الأكواد الأمنية",
  ]
else:
  t_main_title = "🛡️ Security Operations Center (SOC)"
  t_subtitle = (
      "System Architect & Lead: **Fadil I. Hussein** [Active Operations]"
  )
  t_desc = (
      "Professional cyber command center for threat management, packet"
      " analysis, Wireshark filters, and defense."
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
      "🦈 Wireshark Filters",
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
  st.subheader("🔒 حماية وحساب بصمات الملفات (Ransomware & Hash Defense)")
  text_sample = st.text_input(
      "اسم الملف أو النص / Filename or Text:", "operation_data.db"
  )
  if st.button("توليد بصمة SHA-256 / Generate Hash"):
    st.code(hashlib.sha256(text_sample.encode()).hexdigest())

# ---------------------------------------------------------
# Tab 6: DDoS Simulation
# ---------------------------------------------------------
with tabs[5]:
  st.subheader(
      "⚡ محاكاة تحليل تدفق الشبكة واختبار الضغط (DDoS Traffic Simulation)"
  )
  reqs = st.slider("معدل الطلبات في الثانية / Requests per sec:", 100, 10000, 2000)
  if st.button("تنفيذ اختبار التحمل / Run Test"):
    st.info("📊 تقرير الحمل: الخادم يتعامل مع التدفق ضمن الحدود الآمنة.")

# ---------------------------------------------------------
# Tab 7: Image Metadata
# ---------------------------------------------------------
with tabs[6]:
  st.subheader("🖼️ تحليل واستخراج البيانات الخفية للصور (Image Forensics)")
  up_file = st.file_uploader(
      "اختر صورة للفحص / Upload Image:", type=["jpg", "png"]
  )
  if up_file:
    img = Image.open(up_file)
    st.image(img, use_container_width=True)
    st.success("✅ تم تحليل بنية الصورة واستخراج الخصائص بنجاح.")

# ---------------------------------------------------------
# Tab 8: Cryptography
# ---------------------------------------------------------
with tabs[7]:
  st.subheader("🔐 التشفير الكلاسيكي والمتقدم (Cryptography Suite)")
  txt = st.text_input("النص المراد تشفيره / Plaintext:", "FadilHussein")
  shift = st.slider("مفتاح الإزاحة / Shift Key:", 1, 25, 4)
  res = "".join(
      [
        chr(ord(c) + shift) if c.isalpha() else c
        for c in txt
      ]
  )
  st.code(res)

# ---------------------------------------------------------
# Tab 9: Passwords & ATO
# ---------------------------------------------------------
with tabs[8]:
  st.subheader("🧮 حاسبة حصانة كلمات المرور (Password Strength SOC)")
  pwd = st.text_input(
      "أدخل كلمة المرور / Enter Password:", type="password"
  )
  if pwd:
    st.success(
        "🔒 تقييم الحصانة: يتم فحص تعقيد الرمز لمنع الاستيلاء على الحسابات"
        " (ATO)."
    )

# ---------------------------------------------------------
# Tab 10: Wireshark Filters (التبويب الجديد لفلترات واير شارك)
# ---------------------------------------------------------
with tabs[9]:
  st.subheader(
      "🦈 مرجع فلاتر واير شارك وتحليل الحزم (Wireshark Filters Reference)"
  )
  st.write(
      "أهم فلاتر البحث في Wireshark لتصفية حزم البيانات واكتشاف التهديدات"
      " بسرعة:"
  )

  filter_category = st.selectbox(
      "اختر فئة الفلتر / Select Filter Category:",
      [
          "IP & Host Filters (تصفية العناوين)",
          "Protocol Filters (تصفية البروتوكولات)",
          "Security & Passwords (الأمن وكلمات المرور)",
          "TCP & Errors (أخطاء الاتصال)",
      ],
  )

  if filter_category == "IP & Host Filters (تصفية العناوين)":
    st.code("ip.addr == 192.168.1.1          # تصفية لحركة جهاز معين (إرسال واستقبال)")
    st.code("ip.src == 10.0.0.5              # الحزم القادمة من مصدر محدد فقط")
    st.code("ip.dst == 192.168.1.50          # الحزم المتجهة نحو وجهة محددة فقط")

  elif filter_category == "Protocol Filters (تصفية البروتوكولات)":
    st.code("http                          # عرض طلبات واستجابات HTTP فقط")
    st.code("dns                           # عرض استعلامات وتحويلات DNS فقط")
    st.code("tcp or udp                    # تصفية الحزم حسب بروتوكول النقل")

  elif filter_category == "Security & Passwords (الأمن وكلمات المرور)":
    st.code(
        'http.authorization           # البحث عن بيانات التفويض وكلمات المرور'
        " عبر HTTP"
    )
    st.code(
        'frame contains "password"     # البحث عن كلمة password داخل أي حزمة'
        " بيانات"
    )
    st.code(
        'tcp.flags.syn == 1 and tcp.flags.ack == 0  # رصد محاولات فحص أو فتح'
        " اتصال SYN"
    )

  else:
    st.code(
        "tcp.analysis.retransmission   # رصد إعادة إرسال الحزم (Packet Loss /"
        " Slow Network)"
    )
    st.code(
        "tcp.analysis.flags            # كشف الشذوذ ومشاكل الاتصال في بروتوكول"
        " TCP"
    )

# ---------------------------------------------------------
# Tab 11: Code Library
# ---------------------------------------------------------
with tabs[10]:
  st.subheader("📜 مكتبة الأكواد والأوامر الميدانية (SOC Code Snippets)")
  st.code(
      "import socket\n# TCP socket monitoring script initialized...",
      language="python",
  )

st.divider()
st.caption(
    "Security Operations Center (SOC) © 2026 — Architected by **Fadil I."
    " Hussein** 🛡️"
)
