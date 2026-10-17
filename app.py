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
  st.caption("🚀 CyberStudio Suite v2.0 (Pro Edition)")

# 3. العنوان الرئيسي
st.title("🛡️ CyberStudio Pro — منصة الأدوات الأمنية المتقدمة")
st.markdown("### **Developed & Designed by: Fadil I. Hussein**")
st.write(
    "بيئة تفاعلية متكاملة تجمع بين أدوات الفحص، التشفير، تحليل البيانات"
    " والصور، والتوعية الأمنية."
)
st.divider()

# 4. التبويبات المتقدمة
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "💻 النظام والسيرفر",
    "🔗 فحص الروابط والتصيد",
    "🖼️ تحليل الصور والميتاداتا",
    "🔐 التشفير وشفرة قيصر",
    "🧮 الحسابات وقوة المرور",
    "📊 تحليل السجلات والبيانات",
    "📜 مكتبة الأكواد الأمنية",
])

# ---------------------------------------------------------
# Tab 1: System Info
# ---------------------------------------------------------
with tab1:
  st.subheader("💻 معلومات بيئة التشغيل والحالة الحية")
  col1, col2, col3 = st.columns(3)

  # حساب سرعة الاستجابة اللحظية
  start_time = time.time()
  _ = 1 + 1
  latency = round((time.time() - start_time) * 1000, 2)

  with col1:
    st.metric(label="إصدار بايثون", value=sys.version.split()[0])
    st.metric(label="نظام التشغيل", value=platform.system())
  with col2:
    st.metric(label="إصدار Streamlit", value=st.__version__)
    st.metric(label="سرعة استجابة السيرفر", value=f"{latency} ms")
  with col3:
    st.metric(label="المعمارية", value=platform.machine())
    st.metric(label="حالة المنصة", value="Online 🟢")

  with st.expander("🔍 تفاصيل النظام الكاملة (JSON)"):
    st.json({
        "Developer": "Fadil I. Hussein",
        "Field": "Cybersecurity Sciences",
        "Python Full": sys.version,
        "OS Release": platform.release(),
        "Platform": platform.platform(),
    })

# ---------------------------------------------------------
# Tab 2: URL & Phishing Threat Analyzer (جديد ومميز)
# ---------------------------------------------------------
with tab2:
  st.subheader("🔗 أداة تحليل الروابط واكتشاف مؤشرات التصيد (URL Analyzer)")
  input_url = st.text_input(
      "أدخل الرابط المراد تحليله أمنياً:", "http://192.168.1.1/login-paypal-verify"
  )

  if st.button("بدء تحليل الرابط"):
    suspicious_score = 0
    reasons = []

    # فحوصات أمنية منطقية على الرابط
    if input_url.startswith("http://"):
      suspicious_score += 1
      reasons.append("⚠️ الرابط غير مشفر (HTTP وليس HTTPS).")

    if "@" in input_url:
      suspicious_score += 2
      reasons.append("🚨 يحتوي الرابط على رمز '@' الذي يُستخدم للتضليل.")

    if any(
        char.isdigit() for char in input_url.split("/")[2] if "/" in input_url
    ):
      if "." in input_url.split("/")[2]:
        suspicious_score += 1
        reasons.append(
            "⚠️ يستخدم عنوان IP مباشر بدلاً من اسم نطاق (Domain Name)."
        )

    keywords = ["login", "verify", "secure", "bank", "account", "update"]
    if any(kw in input_url.lower() for kw in keywords):
      suspicious_score += 1
      reasons.append("⚠️ يحتوي الرابط على كلمات حساسة تستخدم في صفحات التصيد.")

    if suspicious_score >= 2:
      st.error(f"🚨 رابط عالي الخطورة! (مؤشر التهديد: {suspicious_score}/4)")
      for r in reasons:
        st.write(r)
    elif suspicious_score == 1:
      st.warning(f"⚠️ رابط متوسط الخطورة. (مؤشر التهديد: {suspicious_score}/4)")
      for r in reasons:
        st.write(r)
    else:
      st.success("✅ الرابط لا يحتوي على مؤشرات تصيد شائعة ظاهرة.")

# ---------------------------------------------------------
# Tab 3: Image Metadata Viewer (جديد ومميز)
# ---------------------------------------------------------
with tab3:
  st.subheader("🖼️ استخراج البيانات الخفية من الصور (Image Exif Metadata)")
  uploaded_file = st.file_uploader(
      "اختر صورة لرفعها وتحليل بياناتها:", type=["jpg", "jpeg", "png"]
  )

  if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="الصورة المرفوعة", use_container_width=True)

    st.write("### 📊 البيانات المستخرجة:")
    st.write(f"• **أبعاد الصورة:** {image.size[0]} x {image.size[1]} بكسل")
    st.write(f"• **صيغة الصورة:** {image.format}")
    st.write(f"• **نمط الألوان:** {image.mode}")

    # استخراج بيانات Exif إن وجدت
    exif_data = image._getexif()
    if exif_data:
      st.success("✅ تم العثور على بيانات Exif خفية في الصورة!")
      st.json({str(k): str(v) for k, v in list(exif_data.items())[:5]})
    else:
      st.info(
          "ℹ️ لا تحوي هذه الصورة بيانات Exif خفية (أو تمت إزالتها أثناء"
          " الضغط)."
      )

# ---------------------------------------------------------
# Tab 4: Cryptography & Caesar Cipher
# ---------------------------------------------------------
with tab4:
  st.subheader("🔐 أدوات التشفير وشفرة قيصر (Caesar Cipher)")

  text_to_cipher = st.text_input("أدخل النص للتشفير:", "Cyber Security 2026")
  shift_val = st.slider("مفتاح الإزاحة (Shift Key):", 1, 25, 3)

  col_c1, col_c2 = st.columns(2)

  def caesar_cipher(text, shift):
    result = ""
    for char in text:
      if char.isalpha():
        start = ord("A") if char.isupper() else ord("a")
        result += chr((ord(char) - start + shift) % 26 + start)
      else:
        result += char
    return result

  with col_c1:
    encrypted = caesar_cipher(text_to_cipher, shift_val)
    st.write("**النص المشفر بشفرة قيصر:**")
    st.code(encrypted)

    b64_enc = base64.b64encode(text_to_cipher.encode()).decode()
    st.write("**تشفير Base64:**")
    st.code(b64_enc)

  with col_c2:
    decrypted = caesar_cipher(encrypted, -shift_val)
    st.write("**فك تشفير قيصر:**")
    st.code(decrypted)

    sha256_hash = hashlib.sha256(text_to_cipher.encode()).hexdigest()
    st.write("**توليد SHA-256 Hash:**")
    st.code(sha256_hash)

# ---------------------------------------------------------
# Tab 5: Password Assessment
# ---------------------------------------------------------
with tab5:
  st.subheader("🧮 حاسبة قوة كلمة المرور وتوليد المفاتيح")
  pwd = st.text_input("أدخل كلمة المرور لاختبارها:", type="password")

  if pwd:
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_sym = any(not c.isalnum() for c in pwd)

    score = sum([length >= 10, has_upper, has_lower, has_digit, has_sym])

    st.progress(score / 5)
    if score >= 4:
      st.success("🔒 كلمة مرور ممتازة وقوية جداً.")
    elif score == 3:
      st.warning("⚠️ كلمة مرور متوسطة القوة.")
    else:
      st.error("❌ كلمة مرور ضعيفة.")

# ---------------------------------------------------------
# Tab 6: Log Analyzer
# ---------------------------------------------------------
with tab6:
  st.subheader("📊 تحليل سجلات الخوادم (Server Log Analyzer)")
  sample_log = st.text_area(
      "صق السجلات هنا:",
      "192.168.1.5 - - [17/Oct/2026] 'GET /admin' 403\n"
      "10.0.0.2 - - [17/Oct/2026] 'POST /login' 200\n"
      "192.168.1.5 - - [17/Oct/2026] 'GET /etc/passwd' 404",
  )

  if st.button("تحليل السجلات الآن"):
    st.write(f"• إجمالي الأسطر: {len(sample_log.splitlines())}")
    if "403" in sample_log or "passwd" in sample_log:
      st.error(
          "🚨 تم رصد محاولات فحص ثغرات أو وصول غير مصرح به (Path Traversal /"
          " Forbidden Access)!"
      )
    else:
      st.success("✅ السجلات نظيفة ولا توجد تهديدات ظاهرة.")

# ---------------------------------------------------------
# Tab 7: Code Helper & Cheatsheet (جديد ومميز)
# ---------------------------------------------------------
with tab7:
  st.subheader("📜 مكتبة الأكواد والأوامر السريعة للأمن السيبراني")
  st.write("مجموعة مقتطفات برمجية سريعة بلغة Python لاستخدامها في سكربتاتك:")

  st.markdown("#### 1. فحص الاتصال بالشبكة (Socket Connection Test):")
  st.code(
      """
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
result = s.connect_ex(('127.0.0.1', 80))
if result == 0:
    print("Port is Open!")
s.close()
""",
      language="python",
  )

  st.markdown("#### 2. إرسال طلب HTTP والتحقق من الاستجابة:")
  st.code(
      """
import requests
response = requests.get('https://example.com')
print("Status Code:", response.status_code)
print("Headers:", response.headers.get('Server'))
""",
      language="python",
  )

st.divider()
st.caption(
    "All rights reserved © 2026 — Created & Developed by **Fadil I. Hussein** 🚀"
)
