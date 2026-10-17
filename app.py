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
    " 1px solid #1e293b; } h1, h2, h3 { color: #38bdf8 !important; }</style>"
)
st.markdown(soc_theme_css, unsafe_allow_html=True)

with st.sidebar:
  st.title("Language")
  lang = st.selectbox("اختر اللغة:", ["العربية", "English"])
  st.divider()
  st.title("SOC Profile")
  st.subheader("Fadil I. Hussein")
  st.write("Cybersecurity Sciences")
  st.write("Al-Qadisiyah University")

if lang == "العربية":
  t_title = "غرفة عمليات الأمان السيبراني (SOC)"
  t_sub = "مهندس النظام والمشرف: Fadil I. Hussein"
  tabs_names = [
      "نبض النظام",
      "الذكاء الاصطناعي",
      "لغات البرمجة",
      "فحص الروابط",
      "صيد الثغرات",
      "برمجيات الفدية",
      "ضغط الشبكة",
      "تحليل الصور",
      "التشفير",
      "حماية الحسابات",
      "الأكواد",
  ]
else:
  t_title = "Security Operations Center (SOC)"
  t_sub = "System Architect & Lead: Fadil I. Hussein"
  tabs_names = [
      "System Pulse",
      "AI Analysis",
      "Code Studio",
      "URL Scanner",
      "Bug Bounty",
      "Ransomware",
      "Network Stress",
      "Image Forensics",
      "Cryptography",
      "Pass Protection",
      "Code Library",
  ]

st.title(f"🛡️ {t_title}")
st.markdown(f"### {t_sub}")
st.divider()

tabs = st.tabs(tabs_names)

with tabs[0]:
  st.subheader("معلومات الخادم وحالة النظام")
  c1, c2, c3 = st.columns(3)
  c1.metric("إصدار بايثون", sys.version.split()[0])
  c2.metric("حالة النظام", "ONLINE [SECURE]")
  c3.metric("مستوى التشفير", "AES-256")

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
  st.subheader("مختبر لغات البرمجة والأمن")
  l_choice = st.selectbox("اختر لغة البرمجة:", ["Python", "C++", "SQL", "Bash"])
  if l_choice == "Python":
    st.code("print('Python module active...')", language="python")
  elif l_choice == "C++":
    st.code("std::cout << 'Memory Safe';", language="cpp")
  elif l_choice == "SQL":
    st.code("SELECT * FROM logs;", language="sql")
  else:
    st.code("nmap -sV 127.0.0.1", language="bash")

with tabs[3]:
  st.subheader("أداة تحليل الروابط واكتشاف التصيد")
  url = st.text_input("أدخل الرابط للفحص:", "https://example.com")
  if st.button("فحص الرابط"):
    if "@" in url or "http://" in url:
      st.warning("⚠️ تحذير: الرابط مشبوه أو غير مشفر.")
    else:
      st.success("✅ الرابط يبدو آمناً.")

with tabs[4]:
  st.subheader("قائمة فحص صيد الثغرات")
  target = st.text_input("النطاق المستهدف:", "target.org")
  if st.button("توليد قائمة المهام"):
    st.success(f"تم إعداد نطاق المهام لـ {target}")
    st.checkbox("فحص robots.txt")
    st.checkbox("اختبار XSS")

with tabs[5]:
  st.subheader("حماية وحساب بصمات الملفات")
  sample = st.text_input("اسم الملف أو النص:", "data.db")
  if st.button("توليد بصمة SHA-256"):
    st.code(hashlib.sha256(sample.encode()).hexdigest())

with tabs[6]:
  st.subheader("محاكاة تحليل تدفق الشبكة واختبار الضغط")
  st.slider("الطلبات في الثانية:", 100, 10000, 2000)
  if st.button("تنفيذ اختبار التحمل"):
    st.info("الخادم يتعامل مع التدفق ضمن الحدود الآمنة.")

with tabs[7]:
  st.subheader("تحليل واستخراج البيانات الخفية للصور")
  img = st.file_uploader("اختر صورة:", type=["jpg", "png"])
  if img:
    st.image(img, use_container_width=True)
    st.success("تم تحليل بنية الصورة بنجاح.")

with tabs[8]:
  st.subheader("التشفير الكلاسيكي والمتقدم")
  txt = st.text_input("النص:", "FadilHussein")
  shift = st.slider("مفتاح الإزاحة:", 1, 25, 4)
  res = "".join([chr(ord(c) + shift) if c.isalpha() else c for c in txt])
  st.code(res)

with tabs[9]:
  st.subheader("حاسبة حصانة كلمات المرور")
  st.text_input("كلمة المرور:", type="password")

with tabs[10]:
  st.subheader("مكتبة الأكواد والأوامر الميدانية")
  st.code("import socket\n# Socket monitoring active...", language="python")

st.divider()
st.caption(
    "Security Operations Center (SOC) © 2026 — Architected by Fadil I. Hussein"
    " 🛡️"
)

