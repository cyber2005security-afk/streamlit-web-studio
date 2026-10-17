import base64
import hashlib
import platform
import random
import string
import sys
import time
from PIL import Image
import streamlit as st

# 1. إعدادات الصفحة والتصميم
st.set_page_config(
    page_title="CyberStudio Pro - Fadil I. Hussein", page_icon="🛡️", layout="wide"
)

# 2. القائمة الجانبية (Sidebar)
with st.sidebar:
  st.title("👨‍💻 Developer Profile")
  st.subheader("Fadil I. Hussein")
  st.write("🎓 **Cybersecurity Sciences Student**")
  st.write("🏛️ Al-Qadisiyah University")
  st.divider()
  st.caption("🚀 CyberStudio Suite v4.0 (Multi-Language Edition)")

# 3. العنوان الرئيسي
st.title("🛡️ CyberStudio Pro — المنصة الأمنية والبرمجية الشاملة")
st.markdown("### **Developed & Designed by: Fadil I. Hussein**")
st.write(
    "لوحة تحكم تفاعلية متكاملة تجمع بين أدوات الأمن السيبراني ولغات البرمجة"
    " المختلفة."
)
st.divider()

# 4. التبويبات المتقدمة (تشمل الأدوات السابقة + تبويب لغات البرمجة الجديد)
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
    "💻 النظام والسيرفر",
    "💻 لغات البرمجة (Multi-Lang)",
    "🎣 فحص التصيد (Phishing)",
    "💰 صيد الثغرات (Bug Bounty)",
    "🔒 برمجيات الفدية (Ransomware)",
    "⚡ هجمات (DDoS) والضغط",
    "🖼️ تحليل الصور وميتاداتا",
    "🔐 التشفير وشفرة قيصر",
    "🧮 حماية الحسابات وقوة المرور",
    "📜 مكتبة الأكواد الأمنية",
])

# ---------------------------------------------------------
# Tab 1: System Info
# ---------------------------------------------------------
with tab1:
  st.subheader("💻 معلومات بيئة التشغيل والحالة الحية")
  col1, col2, col3 = st.columns(3)

  start_time = time.time()
  _ = 1 + 1
  latency = round((time.time() - start_time) * 1000, 2)

  with col1:
    st.metric(label="إصدار بايثون", value=sys.version.split()[0])
    st.metric(label="نظام التشغيل", value=platform.system())
  with col2:
    st.metric(label="إصدار Streamlit", value=st.__version__)
    st.metric(label="سرعة الاستجابة", value=f"{latency} ms")
  with col3:
    st.metric(label="المعمارية", value=platform.machine())
    st.metric(label="حالة المنصة", value="Online 🟢")

  with st.expander("🔍 تفاصيل النظام الكاملة (JSON)"):
    st.json({
        "Developer": "Fadil I. Hussein",
        "Field": "Cybersecurity Sciences",
        "Python Full": sys.version,
        "OS Release": platform.release(),
    })

# ---------------------------------------------------------
# Tab 2: Multi-Language Playground (تبويب لغات البرمجة الجديد)
# ---------------------------------------------------------
with tab2:
  st.subheader("💻 مختبر لغات البرمجة في الأمن السيبراني (Multi-Language Studio)")
  st.write(
      "اختر اللغة البرمجية لاستعراض أمثلة عملات أمنية وتطبيقات حية لكل لغة:"
  )

  lang_choice = st.selectbox(
      "اختر اللغة البرمجية:",
      ["Python", "C / C++", "JavaScript", "SQL", "Bash / Shell"],
  )

  if lang_choice == "Python":
    st.markdown("### 🐍 Python — لغة الأتمتة واختبار الاختراق")
    st.write("أداة سريعة لتوليد مصفوفات أو فحص نصوص:")
    py_code = st.text_area(
        "كود بايثون تفاعلي:",
        "def check_secure(text):\n    return 'Secure' if len(text) > 8 else"
        " 'Weak'\nprint(check_secure('MyPass123'))",
    )
    if st.button("تشغيل كود بايثون مبسط"):
      st.info("نتيجة الكود: Secure")

  elif lang_choice == "C / C++":
    st.markdown("### ⚡ C / C++ — الهندسة العكسية وتطوير الأنظمة")
    st.write("تُستخدم في تحليل الذاكرة (Buffer Overflow) وتطوير برامج الخفاء:")
    st.code(
        """
#include <iostream>
using namespace std;

int main() {
    char buffer[10];
    cout << "C++ Security Context Loaded." << endl;
    return 0;
}
""",
        language="cpp",
    )

  elif lang_choice == "JavaScript":
    st.markdown("### 🌐 JavaScript — ثغرات الويب واختراق المتصفحات (XSS)")
    st.write("تُستخدم في بناء واجهات الويب واكتشاف ثغرات الـ DOM:")
    st.code(
        """
// كود توعوي لفحص ثغرات XSS
function testPayload(input) {
    console.log("Testing XSS Payload: " + input);
}
testPayload("<script>alert('XSS')</script>");
""",
        language="javascript",
    )

  elif lang_choice == "SQL":
    st.markdown("### 🗄️ SQL — قواعد البيانات وحقن الاستعلامات (SQLi)")
    user_input = st.text_input("اختبار إدخال المستخدم للبحث:", "admin' OR '1'='1")
    st.write("**الاستعلام الناتج بدون حماية (عرضة للحقن):**")
    st.code(
        f"SELECT * FROM users WHERE username = '{user_input}' AND password ="
        " '123';",
        language="sql",
    )
    st.write("**الاستعلام الآمن باستعمال Prepared Statements:**")
    st.code(
        "SELECT * FROM users WHERE username = ? AND password = ?;",
        language="sql",
    )

  elif lang_choice == "Bash / Shell":
    st.markdown("### 🐚 Bash — أوامر أنظمة Linux و Kali Linux")
    st.write("أوامر إدارة السيرفرات وفحص الشبكات:")
    st.code(
        """
# فحص السيرفرات النشطة في الشبكة
nmap -sp 192.168.1.0/24
# إظهار الاتصالات الحالية
netstat -tuln
""",
        language="bash",
    )

# ---------------------------------------------------------
# Tab 3: Phishing & URL Analyzer
# ---------------------------------------------------------
with tab3:
  st.subheader("🎣 أداة تحليل الروابط وكشف الهندسة الاجتماعية والتصيد")
  input_url = st.text_input(
      "أدخل الرابط للفحص:", "http://192.168.1.50/login-secure-update"
  )

  if st.button("فحص مؤشرات التصيد"):
    score = 0
    if input_url.startswith("http://"):
      score += 1
      st.warning("⚠️ تحذير: الرابط غير مشفر (HTTP).")
    if "@" in input_url:
      score += 2
      st.error("🚨 خطر: وجود رمز '@' في الرابط لتضليل المتصفح.")
    if any(
        kw in input_url.lower()
        for kw in ["login", "verify", "update", "bank", "secure"]
    ):
      score += 1
      st.warning("⚠️ الرابط يحتوي على كلمات حساسة تستخدم غالباً في صفحات المزيفة.")

    if score >= 2:
      st.error(f"❌ النتيجة: رابط مشبوه بشدة (مؤشر التهديد: {score})")
    else:
      st.success("✅ النتيجة: لا توجد مؤشرات تصيد خطيرة واضحة.")

# ---------------------------------------------------------
# Tab 4: Bug Bounty
# ---------------------------------------------------------
with tab4:
  st.subheader("💰 أداة مساعد صائد الثغرات (Bug Bounty)")
  target_domain = st.text_input("النطاق المستهدف (Target Domain):", "target.com")
  if st.button("توليد قائمة فحص الثغرات (Checklist)"):
    st.success(f"📋 قائمة الفحص المقترحة للنطاق: {target_domain}")
    st.checkbox("1. فحص ملفات robots.txt و sitemap.xml")
    st.checkbox("2. البحث عن ثغرات XSS في حقول الإدخال")
    st.checkbox("3. فحص معالجة طلبات معرفات المستخدمين (IDOR)")
    st.checkbox("4. اختبار حقول الرفع (File Upload Vulnerabilities)")

# ---------------------------------------------------------
# Tab 5: Ransomware Concept
# ---------------------------------------------------------
with tab5:
  st.subheader("🔒 توعية وفحص تشفير الملفات (Ransomware Defense)")
  text_sample = st.text_input("أدخل نص أو اسم الملف للفحص:", "important_data.docx")
  if st.button("توليد بصمة الحماية (SHA-256)"):
    file_hash = hashlib.sha256(text_sample.encode()).hexdigest()
    st.code(file_hash, language="text")

# ---------------------------------------------------------
# Tab 6: DDoS Simulation
# ---------------------------------------------------------
with tab6:
  st.subheader("⚡ محاكاة تحليل تدفق الشبكة وضغط الطلبات (DDoS Analysis)")
  req_per_sec = st.slider("عدد الطلبات الوهمية في الثانية:", 100, 10000, 1500)

  if st.button("اختبار ضغط السيرفر"):
    if req_per_sec > 5000:
      st.error("🚨 تحذير حرج: تدفق هائل للطلبات! (DDoS Attack Detected).")
    elif req_per_sec > 2000:
      st.warning("⚠️ ضغط عالي جداً على السيرفر.")
    else:
      st.success("✅ السيرفر يتحمل تدفق الطلبات بشكل طبيعي.")

# ---------------------------------------------------------
# Tab 7: Image Metadata
# ---------------------------------------------------------
with tab7:
  st.subheader("🖼️ استخراج البيانات الخفية من الصور (Image Exif)")
  uploaded_file = st.file_uploader(
      "اختر صورة لتحليلها أمنياً:", type=["jpg", "jpeg", "png"]
  )
  if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة المرفوعة", use_container_width=True)
    st.write(f"• **الأبعاد:** {image.size[0]} x {image.size[1]} بكسل")
    st.write(f"• **الصيغة:** {image.format}")

# ---------------------------------------------------------
# Tab 8: Cryptography
# ---------------------------------------------------------
with tab8:
  st.subheader("🔐 التشفير الكلاسيكي وشفرة قيصر")
  text_to_cipher = st.text_input("أدخل النص:", "CyberSecurity")
  shift_val = st.slider("مفتاح الإزاحة:", 1, 25, 3)

  def caesar_cipher(text, shift):
    res = ""
    for c in text:
      if c.isalpha():
        start = ord("A") if c.isupper() else ord("a")
        res += chr((ord(c) - start + shift) % 26 + start)
      else:
        res += c
    return res

  st.code(caesar_cipher(text_to_cipher, shift_val))

# ---------------------------------------------------------
# Tab 9: Passwords & ATO
# ---------------------------------------------------------
with tab9:
  st.subheader("🧮 حاسبة قوة كلمة المرور ومنع اختراق الحسابات (ATO)")
  pwd = st.text_input("أدخل كلمة المرور لاختبارها:", type="password")
  if pwd:
    score = sum([
        len(pwd) >= 10,
        any(c.isupper() for c in pwd),
        any(c.isdigit() for c in pwd),
        any(not c.isalnum() for c in pwd),
    ])
    st.progress(score / 4)
    if score >= 3:
      st.success("🔒 كلمة مرور قوية.")
    else:
      st.error("❌ كلمة مرور ضعيفة.")

# ---------------------------------------------------------
# Tab 10: Code Helper
# ---------------------------------------------------------
with tab10:
  st.subheader("📜 مكتبة الأكواد البرمجية الأمنية")
  st.code(
      """
# فحص منفذ شبكي بـ Python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
if s.connect_ex(('127.0.0.1', 80)) == 0:
    print("Port Open")
s.close()
""",
      language="python",
  )

st.divider()
st.caption(
    "All rights reserved © 2026 — Created & Developed by **Fadil I. Hussein** (Cybersecurity Sciences) 🚀"
)
