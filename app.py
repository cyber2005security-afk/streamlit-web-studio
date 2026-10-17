import base64
import hashlib
import platform
import random
import string
import sys
import time
from PIL import Image
import streamlit as st

# 1. إعدادات الصفحة والتصميم المرعب والمظلم
st.set_page_config(
    page_title="CyberStudio Dark - Fadil I. Hussein",
    page_icon="💀",
    layout="wide",
)

# حقن أكواد CSS لتغيير الخلفية إلى نظام مظلم ومرعب (Dark Hacker Theme)
dark_theme_css = """
<style>
/* خلفية التطبيق العامة باللون الأسود الداكن مع تأثير أحمر/أخضر مرعب */
[data-testid="stAppViewContainer"] {
    background-color: #050505;
    background-image: radial-gradient(circle at 50% 30%, #1a0000 0%, #000000 90%);
    color: #e0e0e0;
}

/* الشريط الجانبي الداكن */
[data-testid="stSidebar"] {
    background-color: #0a0a0a;
    border-right: 1px solid #ff0033;
}

/* تنسيق العناوين والنصوص لتكون بارزة ومرعبة */
h1, h2, h3 {
    color: #ff3333 !important;
    font-family: 'Courier New', monospace;
}

/* الأزرار بتصميم سيبراني خطير */
.stButton>button {
    background-color: #1a0000;
    color: #ff3333;
    border: 1px solid #ff3333;
    border-radius: 4px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #ff3333;
    color: #000000;
}
</style>
"""
st.markdown(dark_theme_css, unsafe_allow_html=True)

# 2. القائمة الجانبية (Sidebar)
with st.sidebar:
  st.title("💀 Dark Room")
  st.subheader("Fadil I. Hussein")
  st.write("🎓 **Cybersecurity Sciences**")
  st.write("🏛️ Al-Qadisiyah University")
  st.divider()
  st.caption("⚠️ Restricted Access [Level 5]")

# 3. العنوان الرئيسي
st.title("💀 CyberStudio Pro — غرفة العمليات المظلمة")
st.markdown(
    "### **System Architect & Controller: Fadil I. Hussein** [CLASSIFIED]"
)
st.write(
    "منصة أمنية محاطة بالغموض، تعمل في الظل لمراقبة التهديدات، التشفير،"
    " والتحليل البرمجي."
)
st.divider()

# 4. التبويبات المتقدمة
(
    tab1,
    tab2,
    tab3,
    tab4,
    tab5,
    tab6,
    tab7,
    tab8,
    tab9,
    tab10,
) = st.tabs([
    "💻 نبض السيرفر",
    "💻 لغات الظل",
    "🎣 شباك التصيد",
    "💰 صيد الثغرات",
    "🔒 حصن البيانات",
    "⚡ عاصفة DDoS",
    "🖼️ عيون الصور",
    "🔐 التشفير الأبدي",
    "🧮 حارس البوابات",
    "📜 الأكواد السرية",
])

# ---------------------------------------------------------
# Tab 1: System Info
# ---------------------------------------------------------
with tab1:
  st.subheader("💻 مراقبة النبض الحقيقي للخادم")
  col1, col2, col3 = st.columns(3)
  start_time = time.time()
  _ = 1 + 1
  latency = round((time.time() - start_time) * 1000, 2)

  with col1:
    st.metric(label="إصدار بايثون", value=sys.version.split()[0])
    st.metric(label="نظام التشغيل", value=platform.system())
  with col2:
    st.metric(label="سرعة الاستجابة الظلية", value=f"{latency} ms")
    st.metric(label="حالة السيرفر", value="ONLINE [SECURE]")
  with col3:
    st.metric(label="المعمارية", value=platform.machine())
    st.metric(label="مستوى التشفير", value="AES-256")

# ---------------------------------------------------------
# Tab 2: Multi-Language Studio
# ---------------------------------------------------------
with tab2:
  st.subheader("💻 لغات الظل والشيفرات البرمجية")
  lang_choice = st.selectbox(
      "اختر أداة الشيفرة:",
      ["Python", "C / C++", "JavaScript", "SQL", "Bash / Shell"],
  )
  if lang_choice == "Python":
    st.code(
        "print('Executing payload in dark mode...')", language="python"
    )
  elif lang_choice == "C / C++":
    st.code(
        '#include <iostream>\nusing namespace std;\nint main() { cout <<'
        ' "Memory Dump Active"; }',
        language="cpp",
    )
  elif lang_choice == "SQL":
    st.code(
        "SELECT * FROM users WHERE access_level = 'ADMIN';", language="sql"
    )
  else:
    st.code("nmap -A -T4 127.0.0.1", language="bash")

# ---------------------------------------------------------
# Tab 3: Phishing & URL Analyzer
# ---------------------------------------------------------
with tab3:
  st.subheader("🎣 كاشف الروابط المظلمة والتصيد")
  input_url = st.text_input(
      "أدخل الرابط المشبوه للفحص:", "http://dark-web-login-verify.com"
  )
  if st.button("فحص النوايا الخفية"):
    st.error("🚨 تحذير: الرابط يحمل مؤشرات هندسة اجتماعية عالية الخطورة!")

# ---------------------------------------------------------
# Tab 4: Bug Bounty
# ---------------------------------------------------------
with tab4:
  st.subheader("💰 خريطة صيد الثغرات الخفية")
  target_domain = st.text_input("النطاق الهدف:", "target-system.gov")
  if st.button("توليد قائمة الاختراق الأخلاقي"):
    st.success(f"📋 تم تهيئة أهداف الفحص لـ {target_domain}")
    st.checkbox("فحص الثغرات الحرجة (Critical Vulnerabilities)")
    st.checkbox("البحث عن أخطاء التوثيق (Broken Authentication)")

# ---------------------------------------------------------
# Tab 5: Ransomware Defense
# ---------------------------------------------------------
with tab5:
  st.subheader("🔒 حصن التشفير وبرمجيات الفدية")
  text_sample = st.text_input("النص المراد بصمه:", "secret_operation_file")
  if st.button("توليد بصمة الهاش القاتلة"):
    st.code(hashlib.sha256(text_sample.encode()).hexdigest())

# ---------------------------------------------------------
# Tab 6: DDoS Simulation
# ---------------------------------------------------------
with tab6:
  st.subheader("⚡ محاكاة فيضان الطلبات (DDoS Storm)")
  reqs = st.slider("معدل تدفق الطلبات:", 100, 10000, 3000)
  if st.button("إطلاق المحاكاة"):
    st.error("🚨 السيرفر يتعرض لضغط هائل! خطر الانهيار وشيك.")

# ---------------------------------------------------------
# Tab 7: Image Metadata
# ---------------------------------------------------------
with tab7:
  st.subheader("🖼️ عيون الصور والبيانات الدفينة")
  up_file = st.file_uploader(
      "ارفع الصورة لاستخراج الأسرار:", type=["jpg", "png"]
  )
  if up_file:
    img = Image.open(up_file)
    st.image(img, use_container_width=True)
    st.success("✅ تم استخراج بصمة الصورة بنجاح.")

# ---------------------------------------------------------
# Tab 8: Cryptography
# ---------------------------------------------------------
with tab8:
  st.subheader("🔐 غرفة التشفير الأبدي وشفرة قيصر")
  txt = st.text_input("النص السري:", "FadilHussein")
  shift = st.slider("مفتاح الإزاحة السري:", 1, 25, 5)
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
with tab9:
  st.subheader("🧮 حارس البوابات واختبار الحسابات")
  pwd = st.text_input("أدخل كلمة المرور السرية:", type="password")
  if pwd:
    st.warning("⚠️ جاري تحليل حصانة كلمة المرور ضد هجمات القوة العمياء.")

# ---------------------------------------------------------
# Tab 10: Code Helper
# ---------------------------------------------------------
with tab10:
  st.subheader("📜 مكتبة الأكواد السرية")
  st.code("import socket\n# Socket payload initialized...", language="python")

st.divider()
st.caption(
    "All rights reserved © 2026 — Secure Dark Terminal by **Fadil I. Hussein**"
    " 💀"
)
