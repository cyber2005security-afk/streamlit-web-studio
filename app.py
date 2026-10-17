
import hashlib
import streamlit as st
import platform
import sys
import time
import io
import string
from urllib.parse import urlparse
from PIL import Image

st.set_page_config(
    page_title="SOC Operations Center - Fadil I. Hussein",
    page_icon="🛡️",
    layout="wide",
)

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #090d16, #111827);
    color: #f8fafc;
}
[data-testid="stSidebar"] {
    background-color: #1e293b;
}
h1, h2, h3 {
    color: #38bdf8 !important;
}
.stButton > button {
    background: linear-gradient(90deg, #1d4ed8, #2563eb);
    color: white;
    border-radius: 7px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# تهيئة الجلسة
if "demo_login" not in st.session_state:
    st.session_state.demo_login = False
if "demo_name" not in st.session_state:
    st.session_state.demo_name = ""

# Google OAuth الحقيقي يحتاج إعداد secrets.toml
google_logged_in = st.user.is_logged_in

if google_logged_in:
    username = st.user.get("name") or "Google User"
    email = st.user.get("email", "")
    logged_in = True
elif st.session_state.demo_login:
    username = st.session_state.demo_name
    email = ""
    logged_in = True
else:
    username = ""
    email = ""
    logged_in = False

# القائمة الجانبية
with st.sidebar:
    st.title("🌐 اللغة / Language")
    lang = st.selectbox("اختر اللغة", ["العربية", "English"])
    en = lang == "English"

    st.divider()
    st.subheader("👤 تسجيل الدخول")

    if not logged_in:
        with st.form("login_form"):
            name = st.text_input("اسم المستخدم")
            password = st.text_input("كلمة المرور", type="password")
            submit = st.form_submit_button("تسجيل الدخول")

        if submit:
            if name.strip() and password:
                st.session_state.demo_login = True
                st.session_state.demo_name = name.strip()
                st.rerun()
            else:
                st.warning("أدخل اسم المستخدم وكلمة المرور.")

        if st.button("🔴 تسجيل الدخول باستخدام Google"):
            st.login("google")

        st.caption("الدخول العادي تجريبي، وليس نظام مصادقة آمن.")

    else:
        st.success(f"مرحباً، {username}")

        if email:
            st.caption(f"حساب Google: {email}")

        if st.button("تسجيل الخروج"):
            if google_logged_in:
                st.logout()
            st.session_state.demo_login = False
            st.session_state.demo_name = ""
            st.rerun()

    st.divider()
    st.title("🛡️ SOC Profile")
    st.subheader("Fadil I. Hussein")
    st.write("🎓 Cybersecurity Sciences")
    st.write("🏛️ Al-Qadisiyah University")

if not logged_in:
    st.title("🛡️ غرفة عمليات الأمن السيبراني")
    st.warning("سجّل الدخول من القائمة الجانبية للوصول إلى التطبيق.")
    st.stop()

# العنوان بدون البريد الإلكتروني
if en:
    title = "🛡️ Security Operations Center (SOC)"
    subtitle = f"System Architect: Fadil I. Hussein | Active User: {username}"
    description = "Cybersecurity monitoring and defensive tools."
    tabs_names = [
        "💻 System Pulse", "🤖 AI Analysis", "💻 Code Studio",
        "🎣 Phishing Analyzer", "🌐 Google OAuth", "💰 Bug Bounty",
        "🔒 Ransomware Defense", "⚡ Network Tools", "🖼️ Image Analysis",
        "🔐 Cryptography", "🧮 Password Security", "📜 Code Library"
    ]
else:
    title = "🛡️ غرفة عمليات الأمن السيبراني"
    subtitle = f"مهندس النظام: Fadil I. Hussein | المستخدم النشط: {username}"
    description = "لوحة تحكم لمراقبة النظام وتحليل الروابط والصور والأدوات الدفاعية."
    tabs_names = [
        "💻 نبض النظام", "🤖 تحليل الذكاء الاصطناعي", "💻 استوديو البرمجة",
        "🎣 فحص التصيد", "🌐 بيانات Google OAuth", "💰 صيد الثغرات",
        "🔒 حماية الفدية", "⚡ أدوات الشبكة", "🖼️ تحليل الصور",
        "🔐 التشفير", "🧮 حماية الحسابات", "📜 الأكواد الأمنية"
    ]

st.title(title)
st.markdown(f"### {subtitle}")
st.write(description)
st.divider()

tabs = st.tabs(tabs_names)

# 1 معلومات النظام
with tabs[0]:
    st.subheader("💻 معلومات النظام")
    c1, c2, c3 = st.columns(3)
    start = time.perf_counter()
    sum(range(1000))
    latency = round((time.perf_counter() - start) * 1000, 2)

    c1.metric("إصدار Python", sys.version.split()[0])
    c1.metric("نظام التشغيل", platform.system())
    c2.metric("وقت تنفيذ محلي", f"{latency} ms")
    c2.metric("حالة لوحة التحكم", "ONLINE")
    c3.metric("معمارية المعالج", platform.machine() or "Unknown")
    c3.metric("خوارزمية التجزئة", "SHA-256")

# 2 تحليل أمني
with tabs[1]:
    st.subheader("🤖 تحليل النصوص الأمنية")
    text = st.text_area("أدخل سجل النظام أو النص المشبوه")

    if st.button("تحليل النص"):
        if not text.strip():
            st.warning("أدخل النص أولاً.")
        else:
            keywords = [
                "failed login", "unauthorized", "malware",
                "ransomware", "sql injection", "brute force"
            ]
            found = [word for word in keywords if word in text.lower()]

            if found:
                st.warning("تم العثور على مؤشرات:")
                for word in found:
                    st.write("- " + word)
            else:
                st.success("لم يتم العثور على الكلمات المحددة.")
            st.caption("فحص أولي بالكلمات وليس نظام ذكاء اصطناعي متكاملاً.")

# 3 استوديو البرمجة
with tabs[2]:
    st.subheader("💻 استوديو البرمجة")
    code = st.text_area(
        "اكتب كود Python",
        value='print("Hello SOC!")',
        height=200
    )
    st.download_button(
        "تحميل الكود",
        data=code,
        file_name="soc_code.py",
        mime="text/x-python"
    )
    st.info("يمكن تنزيل الكود. تشغيل أكواد المستخدم مباشرة على الخادم معطّل للحماية.")

# 4 فحص التصيد
with tabs[3]:
    st.subheader("🎣 فحص الروابط المشبوهة")
    url = st.text_input("أدخل الرابط")

    if st.button("فحص الرابط"):
        parsed = urlparse(url.strip())
        findings = []

        if parsed.scheme not in ("http", "https"):
            findings.append("الرابط يجب أن يستخدم HTTP أو HTTPS.")
        if not parsed.hostname:
            findings.append("الرابط غير مكتمل أو غير صحيح.")
        if parsed.username or parsed.password:
            findings.append("الرابط يحتوي بيانات دخول.")
        if parsed.scheme == "http":
            findings.append("الرابط لا يستخدم HTTPS.")
        if parsed.hostname and (
            parsed.hostname.startswith("xn--")
            or ".xn--" in parsed.hostname
        ):
            findings.append("تحقق من احتمال تقليد اسم النطاق.")

        if findings:
            for finding in findings:
                st.warning(finding)
        else:
            st.info("لم تظهر مؤشرات محددة، وهذا لا يثبت أن الرابط آمن.")

# 5 Google OAuth
with tabs[4]:
    st.subheader("🌐 بيانات Google OAuth")
    if google_logged_in:
        st.success("تم تسجيل الدخول باستخدام Google.")
        st.write("اسم المستخدم:", username)
        if email:
            st.write("البريد المرتبط بحساب Google:", email)
    else:
        st.info("اضغط زر Google في القائمة الجانبية بعد إعداد OAuth.")
    st.caption("لا يمكن تفعيل Google الحقيقي دون بيانات OAuth.")

# 6 صيد الثغرات
with tabs[5]:
    st.subheader("💰 قائمة فحص صيد الثغرات")
    for task in [
        "التأكد من وجود تصريح",
        "تحديد نطاق الاختبار",
        "مراجعة ترويسات الأمان",
        "فحص صلاحيات الوصول",
        "توثيق النتائج",
    ]:
        st.checkbox(task)
    notes = st.text_area("ملاحظات الفحص")
    st.download_button("تحميل الملاحظات", notes, "bug_bounty_notes.txt")

# 7 حماية الفدية
with tabs[6]:
    st.subheader("🔒 الحماية من برمجيات الفدية")
    for task in [
        "الاحتفاظ بنسخ احتياطية",
        "تفعيل المصادقة متعددة العوامل",
        "تحديث البرامج",
        "تقليل صلاحيات المسؤول",
        "مراقبة تغييرات الملفات",
        "إعداد خطة استجابة للحوادث",
    ]:
        st.checkbox(task)
    st.info("هذه إرشادات دفاعية وليست أداة لإزالة البرمجيات الضارة.")

# 8 أدوات الشبكة
with tabs[7]:
    st.subheader("⚡ أدوات الشبكة")
    target = st.text_input("عنوان الموقع للتحقق من صيغته")
    if st.button("التحقق من العنوان"):
        parsed = urlparse(target.strip())
        if parsed.scheme in ("http", "https") and parsed.hostname:
            st.success("صيغة العنوان تبدو صحيحة.")
            st.write("اسم النطاق:", parsed.hostname)
        else:
            st.error("صيغة العنوان غير صحيحة.")
    st.caption("لا يتم إرسال طلبات أو إجراء فحص منافذ.")

# 9 تحليل الصور
with tabs[8]:
    st.subheader("🖼️ تحليل الصور")
    uploaded = st.file_uploader(
        "ارفع صورة",
        type=["png", "jpg", "jpeg", "webp", "bmp"]
    )

    if uploaded:
        raw = uploaded.getvalue()
        try:
            with Image.open(io.BytesIO(raw)) as img:
                img.verify()

            with Image.open(io.BytesIO(raw)) as img:
                st.image(img, use_container_width=True)
                st.write("العرض:", img.width)
                st.write("الارتفاع:", img.height)
                st.write("الصيغة:", img.format)
                st.write("حجم الملف:", len(raw), "bytes")
                st.write("SHA-256:", hashlib.sha256(raw).hexdigest())
        except Exception:
            st.error("تعذرت قراءة الصورة.")

# 10 التشفير والتجزئة
with tabs[9]:
    st.subheader("🔐 حساب البصمة الرقمية")
    value = st.text_area("النص")
    algorithm = st.selectbox("الخوارزمية", ["SHA-256", "SHA-512", "SHA-3-256"])

    if st.button("حساب البصمة"):
        if not value:
            st.warning("أدخل النص أولاً.")
        else:
            raw = value.encode("utf-8")
            if algorithm == "SHA-256":
                digest = hashlib.sha256(raw).hexdigest()
            elif algorithm == "SHA-512":
                digest = hashlib.sha512(raw).hexdigest()
            else:
                digest = hashlib.sha3_256(raw).hexdigest()
            st.code(digest)

# 11 كلمات المرور
with tabs[10]:
    st.subheader("🧮 فحص قوة كلمة المرور")
    password = st.text_input("كلمة مرور تجريبية", type="password")

    if st.button("فحص القوة"):
        if not password:
            st.warning("أدخل كلمة مرور تجريبية.")
        else:
            score = sum([
                len(password) >= 12,
                any(c.islower() for c in password),
                any(c.isupper() for c in password),
                any(c.isdigit() for c in password),
                any(c in string.punctuation for c in password),
            ])
            if len(password) < 8 or score <= 2:
                st.warning("ضعيفة وفق الفحص الأولي.")
            elif score <= 4:
                st.info("متوسطة وفق الفحص الأولي.")
            else:
                st.success("أقوى وفق الفحص الأولي.")
            st.write(f"المعايير المتحققة: {score}/5")
            st.caption("لا تدخل كلمة مرورك الحقيقية.")

# 12 مكتبة الأكواد
with tabs[11]:
    st.subheader("📜 مكتبة الأكواد الأمنية")
    examples = {
        "SHA-256": (
            "import hashlib\n"
            'text = "Hello SOC"\n'
            'print(hashlib.sha256(text.encode()).hexdigest())'
        ),
        "Random Token": (
            "import secrets\n"
            "print(secrets.token_urlsafe(32))"
        ),
        "HMAC": (
            "import hashlib, hmac\n"
            'key = b"example-key"\n'
            'message = b"example-message"\n'
            'print(hmac.new(key, message, hashlib.sha256).hexdigest())'
        ),
    }
    selected = st.selectbox("اختر مثالاً", list(examples.keys()))
    st.code(examples[selected], language="python")
    st.download_button(
        "تحميل المثال",
        examples[selected],
        "security_example.py"
    )

st.divider()
st.caption("غرفة عمليات الأمن السيبراني | مشروع تعليمي قابل للتطوير")
