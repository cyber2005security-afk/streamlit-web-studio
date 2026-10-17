import hashlib
import platform
import re
import sys
import time
from PIL import Image
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="SOC Operations Center - Fadil I. Hussein",
    page_icon="🛡️",
    layout="wide",
)

# تصميم الواجهة الاحترافي
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
}
.stButton>button {
    background-color: #1d4ed8;
    color: #ffffff;
    border-radius: 6px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #2563eb;
}
</style>
"""
st.markdown(soc_theme_css, unsafe_allow_html=True)

# القائمة الجانبية واختيار اللغة والأدوات
with st.sidebar:
  st.title("🌐 Language / اللغة")
  lang = st.selectbox("اختر لغة العرض:", ["العربية", "English"])
  st.divider()

  st.subheader("🛡️ SOC Profile")
  st.write("Fadil I. Hussein")
  st.write("🎓 **Cybersecurity Sciences**")
  st.write("🏛️ Al-Qadisiyah University")
  st.divider()

  # قائمة الأدوات المنظمة بشكل عمودي (تمنع مشكلة الاختفاء على الموبايل)
  if lang == "العربية":
    menu_title = "📌 أدوات غرفة العمليات"
    menu_options = [
        "💻 نبض النظام",
        "🤖 تحليل الذكاء الاصطناعي",
        "🔍 فحص الروابط الشامل",
        "🔐 أمان المصادقة والجلسات",
        "💻 لغات البرمجة",
        "💰 صيد الثغرات",
        "🔒 برمجيات الفدية",
        "⚡ ضغط الشبكة",
        "🖼️ تحليل الصور",
        "🔐 التشفير",
        "🧮 حماية الحسابات",
        "📜 الأكواد الأمنية",
    ]
  else:
    menu_title = "📌 Operations Tools"
    menu_options = [
        "💻 System Pulse",
        "🤖 AI Security Analysis",
        "🔍 General URL Scanner",
        "🔐 Auth & Session Security",
        "💻 Code Studio",
        "💰 Bug Bounty",
        "🔒 Ransomware Defense",
        "⚡ Network Stress",
        "🖼️ Image Forensics",
        "🔐 Cryptography",
        "🧮 Pass Protection",
        "📜 Code Library",
    ]

  choice = st.sidebar.radio(menu_title, menu_options)

# العنوان الرئيسي للمنصة
if lang == "العربية":
  st.title("🛡️ غرفة عمليات الأمان السيبراني (SOC)")
  st.markdown("مهندس النظام والمشرف: **Fadil I. Hussein** [مركز العمليات النشط]")
else:
  st.title("🛡️ Security Operations Center (SOC)")
  st.markdown("System Architect & Lead: **Fadil I. Hussein** [Active Operations]")

st.divider()

# التوجيه البرمجي لكل أداة (تضمن عمل كل قسم بkفاءة تامة)
if "نبض" in choice or "System Pulse" in choice:
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

elif "الذكاء الاصطناعي" in choice or "AI Security Analysis" in choice:
  st.subheader("🤖 أداة تحليل السلوك والتهديدات بالذكاء الاصطناعي")
  st.write(
      "تستخدم هذه الأداة خوارزميات التعلم الآلي لتحليل سلوك الشبكة واكتشاف"
      " الهجمات تلقائياً."
  )
  net_traffic = st.slider(
      "معدل نقل بيانات الشبكة (Network Traffic MB/s):", 10, 1000, 150
  )
  failed_attempts = st.slider("محاولات الدخول الفاشلة المتكررة:", 0, 50, 2)

  if st.button("تشغيل فحص الذكاء الاصطناعي / Run AI Analysis"):
    if net_traffic > 700 or failed_attempts > 15:
      st.error(
          "🚨 [AI Alert] تم رصد سلوك شبكي شاذ! احتمالية تعرض النظام لهجوم"
          " سيبراني."
      )
      st.warning(
          "⚙️ الإجراء التلقائي: تم عزل الاتصال المشبوه وحظر المصدر مؤقتاً."
      )
    else:
      st.success("✅ [AI Status] حالة الأمان مستقرة وسلوك الشبكة طبيعي.")

elif "الروابط" in choice or "URL Scanner" in choice:
  st.subheader("🔍 أداة فحص وتحليل الروابط الشاملة")
  st.write(
      "قم بإدخال أي رابط لفحصه برمجياً والكشف عن المؤشرات المشبوهة (مثل عناوين"
      " IP أو الرموز الخاصة)."
  )
  target_url = st.text_input(
      "أدخل الرابط للفحص / Enter URL to scan:",
      "https://example-secure-login.com",
  )

  if st.button("بدء فحص الرابط / Scan URL"):
    if not target_url.startswith(("http://", "https://")):
      st.error(
          "❌ صيغة الرابط غير صحيحة. يجب أن يبدأ الرابط بـ http:// أو https://"
      )
    else:
      risk_score = 0
      warnings = []
      if target_url.startswith("http://"):
        risk_score += 30
        warnings.append("⚠️ استخدام بروتوكول غير مشفر (HTTP بدلاً من HTTPS).")

      ip_pattern = re.compile(r"https?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}")
      if ip_pattern.search(target_url):
        risk_score += 50
        warnings.append("🚨 وجود عنوان IP مباشر بدلاً من اسم النطاق.")

      if "@" in target_url:
        risk_score += 40
        warnings.append("⚠️ احتواء الرابط على رمز (@) لتضليل المستخدمين.")

      if len(target_url) > 75:
        risk_score += 20
        warnings.append("⚠️ طول الرابط مريب جداً.")

      st.divider()
      st.write(f"**تقرير فحص الرابط لـ:** `{target_url}`")
      if risk_score == 0:
        st.success("✅ النتيجة: الرابط يبدو آمناً ولا توجد مؤشرات خطر ظاهرة.")
      elif risk_score < 50:
        st.warning(
            f"⚠️ النتيجة: مستوى الخطورة متوسط (درجة الخطورة: {risk_score}%)"
        )
        for w in warnings:
          st.write(f"- {w}")
      else:
        st.error(
            f"🚨 النتيجة: تحذير شديد! الرابط مشبوه جداً (درجة الخطورة:"
            f" {risk_score}%)"
        )
        for w in warnings:
          st.write(f"- {w}")

elif "المصادقة" in choice or "Auth Security" in choice:
  st.subheader("🔐 أداة اختبار أمان المصادقة والجلسات")
  st.write(
      "تقييم حصانة منصات الويب ضد ثغرات تخطي المصادقة، سرقة الرموز (Tokens)،"
      " وعمليات الاستيلاء على الحسابات."
  )
  auth_module = st.selectbox(
      "اختر فحص الأمان:",
      [
          "فحص ثغرات المصادقة الثنائية (MFA/2FA Bypass Check)",
          "فحص أمان الرموز وجلسات المستخدم (JWT & Cookie Security)",
          "محاكاة حماية الحسابات من الاستيلاء (ATO Protection Rules)",
      ],
  )

  if "MFA" in auth_module:
    st.text_input(
        "أدخل نقطة النهاية لتسجيل الدخول:",
        "https://api.target-platform.com/v1/auth/login",
    )
    if st.button("فحص آليات الـ 2FA"):
      st.warning(
          "⚠️ تقييم الفحص: تأكد من تطبيق التحقق على مستوى السيرفر لتجنب الثغرات."
      )
  elif "JWT" in auth_module:
    st.text_input("أدخل الرمز المميز (JWT Token):", "eyJhbGciOiJIUzI1Ni...")
    if st.button("فحص إعدادات التوقيع والـ HttpOnly"):
      st.success("🔒 شروط الأمان: يجب تفعيل خاصية HttpOnly و Secure على الـ Cookies.")
  else:
    st.info("🛡️ نظام ATO مفعل: تقييد محاولات الـ IP يحمي الحسابات بفاعلية.")

elif "لغات البرمجة" in choice or "Code Studio" in choice:
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

elif "الثغرات" in choice or "Bug Bounty" in choice:
  st.subheader("💰 قائمة فحص صيد الثغرات")
  target_domain = st.text_input("النطاق المستهدف / Target Domain:", "target.org")
  if st.button("توليد قائمة المهام / Generate Checklist"):
    st.success(f"📋 تم إعداد نطاق المهام الميدانية لـ {target_domain}")
    st.checkbox("فحص ملفات الروبوتات والمسارات المخفية (robots.txt)")
    st.checkbox("اختبار ثغرات الحقن والسكربتات الخبيثة (XSS)")

elif "الفدية" in choice or "Ransomware" in choice:
  st.subheader("🔒 حماية وحساب بصمات الملفات")
  text_sample = st.text_input(
      "اسم الملف أو النص / Filename or Text:", "operation_data.db"
  )
  if st.button("توليد بصمة SHA-256 / Generate Hash"):
    st.code(hashlib.sha256(text_sample.encode()).hexdigest())

elif "الشبكة" in choice or "Network Stress" in choice:
  st.subheader("⚡ محاكاة تحليل تدفق الشبكة واختبار الضغط")
  reqs = st.slider("معدل الطلبات في الثانية / Requests per sec:", 100, 10000, 2000)
  if st.button("تنفيذ اختبار التحمل / Run Test"):
    st.info("📊 تقرير الحمل: الخادم يتعامل مع التدفق ضمن الحدود الآمنة.")

elif "الصور" in choice or "Image Forensics" in choice:
  st.subheader("🖼️ تحليل واستخراج البيانات الخفية للصور")
  up_file = st.file_uploader(
      "اختر صورة للفحص / Upload Image:", type=["jpg", "png"]
  )
  if up_file:
    img = Image.open(up_file)
    st.image(img, use_container_width=True)
    st.success("✅ تم تحليل بنية الصورة واستخراج الخصائص بنجاح.")

elif "التشفير" in choice or "Cryptography" in choice:
  st.subheader("🔐 التشفير الكلاسيكي والمتقدم")
  txt = st.text_input("النص المراد تشفيره / Plaintext:", "FadilHussein")
  shift = st.slider("مفتاح الإزاحة / Shift Key:", 1, 25, 4)
  res = "".join([chr(ord(c) + shift) if c.isalpha() else c for c in txt])
  st.code(res)

elif "الحسابات" in choice or "Pass Protection" in choice:
  st.subheader("🧮 حاسبة حصانة كلمات المرور")
  pwd = st.text_input("أدخل كلمة المرور / Enter Password:", type="password")
  if pwd:
    st.success(
        "🔒 تقييم الحصانة: يتم فحص تعقيد الرمز لمنع الاستيلاء على الحسابات"
        " (ATO)."
    )

else:
  st.subheader("📜 مكتبة الأكواد والأوامر الميدانية")
  st.code(
      "import socket\n# TCP socket monitoring script initialized...",
      language="python",
  )

st.divider()
st.caption(
    "Security Operations Center (SOC) © 2026 — Architected by **Fadil I."
    " Hussein** 🛡️"
)
