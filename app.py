import base64
import hashlib
import json
import os
import platform
import random
import string
import sys
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="CyberSecurity Web Studio", page_icon="🛡️", layout="wide"
)

st.title("🛡️ منصة الأدوات الأمنية والبرمجية الشاملة")
st.write(
    "لوحة تحكم تفاعلية متكاملة للأمن السيبراني، تشمل أدوات التشفير، الفحص، الحماية، والهجوم الأخلاقي."
)

# إنشاء شريط التنقل العلوي (التبويبات الرئيسية)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
    [
        "💻 النظام والإصدار",
        "🔐 التشفير وفك التشفير",
        "🔍 فحص الثغرات والنطاقات",
        "🧮 الحسابات الأمنية",
        "📊 تحليل البيانات",
        "🛡️ الحماية والدفاع",
        "⚔️ الأدوات الهجومية",
        "🌐 أدوات البرمجة والتصيد",
    ]
)

# ---------------------------------------------------------
# 1. معلومات النظام والإصدار
# ---------------------------------------------------------
with tab1:
  st.subheader("💻 معلومات البيئة والسيرفر")
  c1, c2 = st.columns(2)
  with c1:
    st.metric(label="إصدار بايثون", value=sys.version.split()[0])
    st.metric(label="نظام التشغيل", value=platform.system())
  with c2:
    st.metric(label="إصدار Streamlit", value=st.__version__)
    st.metric(label="المعمارية", value=platform.machine())

# ---------------------------------------------------------
# 2. أدوات التشفير وفك التشفير
# ---------------------------------------------------------
with tab2:
  st.subheader("🔐 أدوات التشفير وفك التشفير (Crypto & Hash)")
  user_text = st.text_input("أدخل النص المراد تشفيره أو فحصه:", "Cyber2026")

  col_a, col_b = st.columns(2)
  with col_a:
    if st.button("تشفير Base64"):
      enc = base64.b64encode(user_text.encode("utf-8")).decode("utf-8")
      st.code(enc, language="text")
    if st.button("توليد MD5 Hash"):
      md5_res = hashlib.md5(user_text.encode("utf-8")).hexdigest()
      st.code(md5_res, language="text")

  with col_b:
    if st.button("فك تشفري Base64"):
      try:
        dec = base64.b64decode(user_text.encode("utf-8")).decode("utf-8")
        st.code(dec, language="text")
      except Exception:
        st.error("خطأ: النص ليس بتنسيق Base64 صالح.")
    if st.button("توليد SHA-256 Hash"):
      sha = hashlib.sha256(user_text.encode("utf-8")).hexdigest()
      st.code(sha, language="text")

# ---------------------------------------------------------
# 3. أدوات فحص الثغرات (Vulnerability Scanning Tools)
# ---------------------------------------------------------
with tab3:
  st.subheader("🔍 فحص الثغرات والنطاقات السريعة")
  target_url = st.text_input(
      "أدخل الرابط أو النطاق للفحص المبدئي:", "https://example.com"
  )

  if st.button("بدء فحص الرؤوس الأمنية (Security Headers)"):
    st.info("جاري تحليل الرؤوس الأمنية الوهمية للنطاق...")
    st.write("• X-Frame-Options: غير مفعيل (تحذير)")
    st.write("• Content-Security-Policy: مفقود (عرضة لاختراق XSS)")
    st.write("• Strict-Transport-Security (HSTS): مفعل (آمن)")
    st.warning("⚠️ هذه أداة فحص محاكاة تعليمية للـ Headers.")

# ---------------------------------------------------------
# 4. أدوات الحسابات الأمنية (Security Calculations)
# ---------------------------------------------------------
with tab4:
  st.subheader("🧮 حاسبة قوة كلمات المرور ومقاييس التشفير")
  pass_input = st.text_input(
      "أدخل كلمة المرور لاختبار قوتها:", type="password"
  )

  if pass_input:
    length = len(pass_input)
    has_upper = any(c.isupper() for c in pass_input)
    has_lower = any(c.islower() for c in pass_input)
    has_digit = any(c.isdigit() for c in pass_input)
    has_sym = any(not c.isalnum() for c in pass_input)

    score = sum([length >= 8, has_upper, has_lower, has_digit, has_sym])

    st.write(f"• طول الرمز: {length} خانات")
    if score >= 4:
      st.success("🔒 كلمة المرور قوية جداً وممتازة.")
    elif score == 3:
      st.warning("⚠️ كلمة المرور متوسطة القوة، يفضل إضافة رموز وأرقام.")
    else:
      st.error("❌ كلمة المرور ضعيفة وعرضة للاختراق بسهولة.")

# ---------------------------------------------------------
# 5. أدوات تحليل البيانات (Data Analytics & Logs)
# ---------------------------------------------------------
with tab5:
  st.subheader("📊 تحليل السجلات وملفات البيانات (Log Analyzer)")
  log_data = st.text_area(
      "صق سجلات الدخول (Server Logs) هنا للتحليل:",
      "192.168.1.10 - - [2026-10-17] 'GET /admin' 403\n10.0.0.5 - - [2026-10-17] 'POST /login' 200",
  )

  if st.button("تحليل السجلات"):
    lines = log_data.split("\n")
    st.write(f"• إجمالي عدد السطور المدخلة: {len(lines)}")
    if "403" in log_data or "404" in log_data:
      st.warning(
          "⚠️ تم رصد محاولات وصول مرفوضة (Unauthorized Access Attempts) في"
          " السجلات!"
      )
    else:
      st.success("✅ السجلات تبدو طبيعية.")

# ---------------------------------------------------------
# 6. أدوات الحماية الدفاعية (Blue Team / Defense)
# ---------------------------------------------------------
with tab6:
  st.subheader("🛡️ أدوات الحماية والدفاع السيبراني")
  st.write(
      "هنا يتم وضع قواعد الجدار الناري الوهمية، وفلاتر حماية مدخلات المستخدم"
      " (Sanitization)."
  )

  raw_payload = st.text_input("اختبار فلتر ضد حقن SQL / XSS:")
  if st.button("فحص المدخلات أمنياً"):
    dangerous_keywords = ["'", "OR", "DROP", "<script>", "--", "SELECT"]
    if any(keyword.lower() in raw_payload.lower() for keyword in dangerous_keywords):
      st.error("🚨 تم اكتشاف محاولة حقن (Injection Attempt) وتم حظر المدخلات!")
    else:
      st.success("✅ المدخلات آمنة ولا توجد أكواد خبيثة ظاهرة.")

# ---------------------------------------------------------
# 7. الأدوات الهجومية (Red Team / Offensive Simulation)
# ---------------------------------------------------------
with tab7:
  st.subheader("⚔️ أدوات المحاكاة الهجومية (أغراض تعليمية دفاعية)")
  st.warning(
      "⚠️ تنبيه: هذه الأدوات مخصصة حصرياً للفحص القانوني واختبار الاختبار"
      " الأخلاقي (Ethical Hacking & Bug Bounty)."
  )

  target_ip = st.text_input("أدخل عنوان الهدف للمحاكاة:", "127.0.0.1")
  if st.button("محاكاة فحص المنافذ (Port Scanning)"):
    st.info(f"جاري فحص المنافذ الشائعة للهدف {target_ip}...")
    st.write("• Port 21 (FTP): مغلق")
    st.write("• Port 80 (HTTP): مفتوح")
    st.write("• Port 443 (HTTPS): مفتوح")
    st.write("• Port 22 (SSH): مغلق")

# ---------------------------------------------------------
# 8. لغات البرمجة ومحاكاة التصيد التوعوي (Phishing Awareness)
# ---------------------------------------------------------
with tab8:
  st.subheader("🌐 أدوات البرمجة والتوعية بالتصيد الاحتيالي (Phishing Awareness)")
  st.write(
      "في مجال الأمن السيبراني، دراسة هندسة التصيد (Phishing) تتم بهدف"
      " **التوعية والدفاع** وليس للاختراق الضار."
  )

  with st.expander("📌 نموذج توعوي لكشف رسائل التصيد الاحتيالي"):
    st.write(
        "1. تحقق دائماً من نطاق المرسل الحقيقي (Sender Domain).\n2. احذر من"
        " الروابط المختصرة أو التي تستخدم أسماء شركات وهمية.\n3. الشركات"
        " الحقيقية لا تطلب كلمات المرور عبر البريد الإلكتروني أبداً."
    )

  st.markdown("---")
  st.write("### 💻 مقتطف كود بايثون سريع لفحص الروابط:")
  st.code(
      """
import urllib.parse
url = "https://example.com/login"
parsed = urllib.parse.urlparse(url)
print("Domain:", parsed.netloc)
""",
      language="python",
  )

st.divider()
st.caption(
    "CyberSecurity Web Studio — تم التطوير بغرض البحث العلمي والأمني والأكاديمي"
    " 🚀"
)
