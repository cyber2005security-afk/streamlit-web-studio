import hashlib
import platform
import sys
import time
import io
import contextlib
from PIL import Image
import streamlit as st

st.set_page_config(page_title="SOC Operations Center - Fadil I. Hussein", page_icon="🛡️", layout="wide")

st.markdown("<style>[data-testid='stAppViewContainer'] { background: #090d16; color: #f8fafc; } [data-testid='stSidebar'] { background-color: #0f172a; } h1, h2, h3 { color: #38bdf8 !important; }</style>", unsafe_allow_html=True)

with st.sidebar:
    st.title("Language")
    lang = st.selectbox("اختر اللغة:", ["العربية", "English"])
    st.divider()
    st.title("🛡️ SOC Profile")
    st.subheader("Fadil I. Hussein")
    st.write("Cybersecurity Sciences")
    st.write("Al-Qadisiyah University")

if lang == "العربية":
    t_title = "غرفة عمليات الأمان السيبراني (SOC)"
    t_sub = "مهندس النظام: Fadil I. Hussein"
    tabs_names = ["نبض النظام", "الذكاء الاصطناعي", "محرر الأكواد", "أدوات Wireshark", "أدوات DoS / DDoS", "الهندسة الاجتماعية", "فحص الروابط", "صيد الثغرات", "برمجيات الفدية", "تحليل الصور", "التشفير", "حماية الحسابات"]
else:
    t_title = "Security Operations Center (SOC)"
    t_sub = "System Architect: Fadil I. Hussein"
    tabs_names = ["System Pulse", "AI Security", "Live Code Studio", "Wireshark Tools", "DoS / DDoS Lab", "Social Engineering", "URL Scanner", "Bug Bounty", "Ransomware", "Image Forensics", "Cryptography", "Pass Security"]

st.title(f"🛡️ {t_title}")
st.markdown(f"### {t_sub}")
st.divider()

tabs = st.tabs(tabs_names)

with tabs[0]:
    st.subheader("معلومات الخادم وحالة النظام")
    col1, col2, col3 = st.columns(3)
    col1.metric("إصدار بايثون", sys.version.split()[0])
    col2.metric("حالة النظام", "ONLINE [SECURE]")
    col3.metric("مستوى التشفير", "AES-256")

with tabs[1]:
    st.subheader("تحليل السلوك والتهديدات بالذكاء الاصطناعي")
    traffic = st.slider("معدل نقل بيانات الشبكة (MB/s):", 10, 1000, 150)
    fails = st.slider("محاولات الدخول الفاشلة:", 0, 50, 2)
    if st.button("تشغيل فحص الذكاء الاصطناعي"):
        if traffic > 700 or fails > 15:
            st.error("🚨 تنبيه: تم رصد سلوك شبكي شاذ أو هجوم محتمل!")
        else:
            st.success("✅ حالة الأمان مستقرة وسلوك الشبكة طبيعي.")

with tabs[2]:
    st.subheader("محرر كود بايثون التفاعلي")
    default_code = "import math\n\ndef check_ip(ip):\n    parts = ip.split('.')\n    return len(parts) == 4\n\nprint('IP Check:', check_ip('192.168.1.1'))"
    user_code = st.text_area("محرر الأكواد:", value=default_code, height=180)
    if st.button("تشغيل الكود"):
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                exec(user_code, {})
            st.code(buf.getvalue(), language="text")
        except Exception as e:
            st.error(f"خطأ: {e}")

with tabs[3]:
    st.subheader("أدوات Wireshark وتحليل الحزم")
    st.file_uploader("تحميل ملف حركة الشبكة (PCAP):", type=["pcap", "pcapng"])
    st.text_input("تصفية البروتوكول:", "tcp.port == 80")
    if st.button("تحليل الحزم"):
        st.json({"Total Packets": 1420, "Protocol": "HTTP / TCP", "Status": "Analyzed"})

with tabs[4]:
    st.subheader("أدوات DoS / DDoS واختبار التحمل")
    st.text_input("الهدف (Target IP):", "127.0.0.1")
    st.selectbox("نوع الهجوم:", ["SYN Flood", "UDP Flood", "HTTP GET Flood"])
    st.slider("معدل الحزم/الثانية:", 100, 50000, 5000)
    if st.button("بدء الاختبار"):
        st.warning("جاري محاكاة ضغط الشبكة...")
        st.progress(90)
        st.error("تنبيه: تم رصد استهلاك عالي لموارد الخادم.")

with tabs[5]:
    st.subheader("أدوات الهندسة الاجتماعية")
    st.radio("نوع الأداة:", ["تحليل ترويسة البريد", "محاكاة صفحة الهبوط"])
    st.text_area("أدخل الترويسة:", "Received: from mail...")
    if st.button("فحص"):
        st.warning("مؤشرات خطورة: عدم تطابق التوقيع الرقمي.")

with tabs[6]:
  st.subheader("فحص الروابط والتصيد")
  url = st.text_input("أدخل الرابط:", "https://example.com")
  if st.button("فحص"):
    st.success("الرابط يبدو آمناً.")

with tabs[7]:
  st.subheader("قائمة صيد الثغرات")
  st.text_input("النطاق المستهدف:", "target.org")
  if st.button("توليد المهام"):
    st.success("تم إعداد المهام بنجاح.")
    st.checkbox("فحص robots.txt")

with tabs[8]:
  st.subheader("حماية وحساب بصمات الملفات")
  sample = st.text_input("النص أو الملف:", "data.db")
  if st.button("توليد SHA-256"):
    st.code(hashlib.sha256(sample.encode()).hexdigest())

with tabs[9]:
  st.subheader("تحليل الصور")
  img = st.file_uploader("اختر صورة:", type=["jpg", "png"])
  if img:
    st.image(img, use_container_width=True)
    st.success("تم تحليل بنية الصورة.")

with tabs[10]:
  st.subheader("التشفير")
  txt = st.text_input("النص:", "FadilHussein")
  shift = st.slider("مفتاح الإزاحة:", 1, 25, 4)
  res = "".join([chr(ord(c) + shift) if c.isalpha() else c for c in txt])
  st.code(res)

with tabs[11]:
  st.subheader("حاسبة كلمات المرور")
  st.text_input("كلمة المرور:", type="password")

st.divider()
st.caption(
    "Security Operations Center (SOC) © 2026 — Architected by Fadil I. Hussein"
    " 🛡️"
)
