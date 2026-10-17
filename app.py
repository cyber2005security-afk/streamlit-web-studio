
import hashlib
import hmac
import io
import platform
import re
import secrets
import string
import sys
import time
from urllib.parse import urlparse

import streamlit as st
from PIL import Image

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="SOC Operations Center - Fadil I. Hussein",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =====================================================
# 2. PROFESSIONAL SOC THEME
# =====================================================
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #090d16, #111827);
        color: #f8fafc;
    }
    [data-testid="stSidebar"] {
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }
    h1, h2, h3 {
        color: #38bdf8 !important;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    [data-testid="stMetric"] {
        background: #172033;
        border: 1px solid #334155;
        padding: 15px;
        border-radius: 10px;
    }
    .stButton > button {
        background: linear-gradient(90deg, #1d4ed8, #2563eb);
        color: white;
        border: 1px solid #3b82f6;
        border-radius: 7px;
        font-weight: bold;
        width: 100%;
    }
    .stButton > button:hover {
        border-color: #60a5fa;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# 3. SESSION STATE
# =====================================================
defaults = {
    "logged_in": False,
    "username": "",
    "google_email": "",
    "login_attempts": 0,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =====================================================
# 4. LANGUAGE
# =====================================================
with st.sidebar:
    st.title("🌐 Language / اللغة")

    lang = st.selectbox(
        "اختر لغة العرض / Choose Language:",
        ["العربية", "English"],
    )

    is_en = lang == "English"

    st.divider()

    # -------------------------------------------------
    # LOGIN
    # -------------------------------------------------
    st.subheader(
        "👤 User Login" if is_en else "👤 بوابة المستخدم"
    )

    if not st.session_state.logged_in:

        with st.form("login_form"):
            input_user = st.text_input(
                "Username" if is_en else "اسم المستخدم"
            )

            input_pass = st.text_input(
                "Password" if is_en else "كلمة المرور",
                type="password",
            )

            login_submit = st.form_submit_button(
                "Login / تسجيل الدخول"
            )

        if login_submit:
            if input_user.strip() and input_pass:
                # Demo login only. This is not a production
                # authentication system.
                st.session_state.logged_in = True
                st.session_state.username = input_user.strip()
                st.session_state.google_email = ""
                st.rerun()
            else:
                st.warning(
                    "Enter username and password."
                    if is_en
                    else "يرجى إدخال اسم المستخدم وكلمة المرور."
                )

        st.caption(
            "Demo login only; credentials are not verified."
            if is_en
            else "تسجيل تجريبي فقط؛ لا يتم التحقق من صحة بيانات الدخول."
        )

        if st.button(
            "🔴 Google Sign-In" if is_en
            else "🔴 تسجيل الدخول عبر Google"
        ):
            st.info(
                "Google OAuth is not configured. Set up real "
                "OAuth credentials before enabling sign-in."
                if is_en
                else "تسجيل Google غير مفعّل بعد. يجب إعداد "
                "OAuth الحقيقي قبل استخدام هذه الميزة."
            )

    else:
        st.success(
            f"Welcome, {st.session_state.username}!"
            if is_en
            else f"أهلاً بك، {st.session_state.username}!"
        )

        if st.session_state.google_email:
            st.info(st.session_state.google_email)

        if st.button(
            "Logout" if is_en else "تسجيل الخروج"
        ):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.google_email = ""
            st.rerun()

    st.divider()

    st.title("🛡️ SOC Profile")
    st.subheader("Fadil I. Hussein")
    st.write("🎓 Cybersecurity Sciences")
    st.write("🏛️ Al-Qadisiyah University")
    st.caption("🔒 Operations Center Core")


# =====================================================
# 5. LOGIN GATE
# =====================================================
if not st.session_state.logged_in:
    st.title("🛡️ SOC Operations Center")

    st.warning(
        "Please log in using the sidebar to access the dashboard."
        if is_en
        else "يرجى تسجيل الدخول من القائمة الجانبية للوصول إلى لوحة التحكم."
    )

    st.stop()


# =====================================================
# 6. MAIN DASHBOARD
# =====================================================
if is_en:
    main_title = "🛡️ Security Operations Center (SOC)"
    subtitle = (
        f"System Architect: Fadil I. Hussein | "
        f"Active User: {st.session_state.username}"
    )
    description = (
        "Cybersecurity dashboard for system monitoring, "
        "security analysis, and defensive tools."
    )

    tab_names = [
        "💻 System Pulse",
        "🤖 AI Security Analysis",
        "💻 Code Studio",
        "🎣 Phishing Analyzer",
        "🌐 Google OAuth",
        "💰 Bug Bounty",
        "🔒 Ransomware Defense",
        "⚡ Network Tools",
        "🖼️ Image Forensics",
        "🔐 Cryptography",
        "🧮 Password Security",
        "📜 Security Code Library",
    ]
else:
    main_title = "🛡️ غرفة عمليات الأمن السيبراني"
    subtitle = (
        f"مهندس النظام: Fadil I. Hussein | "
        f"المستخدم النشط: {st.session_state.username}"
    )
    description = (
        "لوحة تحكم للأمن السيبراني لمراقبة النظام "
        "وتحليل الروابط والصور واستخدام الأدوات الدفاعية."
    )

    tab_names = [
        "💻 نبض النظام",
        "🤖 تحليل الذكاء الاصطناعي",
        "💻 استوديو البرمجة",
        "🎣 فحص التصيد",
        "🌐 Google OAuth",
        "💰 صيد الثغرات",
        "🔒 حماية الفدية",
        "⚡ أدوات الشبكة",
        "🖼️ تحليل الصور",
        "🔐 التشفير",
        "🧮 حماية كلمات المرور",
        "📜 مكتبة الأكواد الأمنية",
    ]

st.title(main_title)
st.markdown(f"### {subtitle}")
st.write(description)
st.divider()

tabs = st.tabs(tab_names)


# =====================================================
# TAB 1: SYSTEM INFORMATION
# =====================================================
with tabs[0]:
    st.subheader(
        "System Information" if is_en
        else "معلومات النظام وحالة غرفة العمليات"
    )

    col1, col2, col3 = st.columns(3)

    start = time.perf_counter()
    _ = sum(range(1000))
    latency = round((time.perf_counter() - start) * 1000, 2)

    with col1:
        st.metric(
            "Python Version" if is_en else "إصدار Python",
            sys.version.split()[0],
        )
        st.metric(
            "Operating System" if is_en else "نظام التشغيل",
            platform.system(),
        )

    with col2:
        st.metric(
            "Local Execution Time" if is_en else "وقت تنفيذ محلي",
            f"{latency} ms",
        )
        st.metric(
            "Dashboard" if is_en else "لوحة التحكم",
            "ONLINE" if is_en else "تعمل",
        )

    with col3:
        st.metric(
            "CPU Architecture" if is_en else "معمارية المعالج",
            platform.machine() or "Unknown",
        )
        st.metric(
            "Hash Algorithm" if is_en else "خوارزمية التجزئة",
            "SHA-256",
        )

    st.info(
        "Execution time measures a small local calculation, "
        "not internet or server latency."
        if is_en else
        "وقت التنفيذ يقيس عملية محلية بسيطة، وليس سرعة الإنترنت "
        "أو زمن استجابة الخادم."
    )


# =====================================================
# TAB 2: SECURITY ANALYSIS
# =====================================================
with tabs[1]:
    st.subheader(
        "🤖 Security Text Analyzer"
        if is_en else
        "🤖 محلل النصوص والمؤشرات الأمنية"
    )

    st.write(
        "Enter a log, alert, or suspicious message for a basic "
        "rule-based review."
        if is_en else
        "أدخل سجل نظام أو تنبيهًا أو رسالة مشبوهة لإجراء تحليل "
        "أولي يعتمد على قواعد بسيطة."
    )

    security_text = st.text_area(
        "Log / Message" if is_en else "النص أو سجل النظام",
        height=180,
        key="security_text",
    )

    if st.button(
        "Analyze Text" if is_en else "تحليل النص",
        key="analyze_security_text",
    ):
        if not security_text.strip():
            st.warning(
                "Enter some text first."
                if is_en else "أدخل النص أولاً."
            )
        else:
            text_lower = security_text.lower()

            indicators = {
                "failed login": (
                    "Failed login attempts",
                    "محاولات تسجيل دخول فاشلة",
                ),
                "unauthorized": (
                    "Unauthorized access indicator",
                    "مؤشر على وصول غير مصرح به",
                ),
                "malware": (
                    "Malware reference",
                    "إشارة إلى برمجية ضارة",
                ),
                "ransomware": (
                    "Ransomware reference",
                    "إشارة إلى برمجية فدية",
                ),
                "sql injection": (
                    "Possible SQL injection reference",
                    "إشارة محتملة إلى حقن SQL",
                ),
                "brute force": (
                    "Brute-force reference",
                    "إشارة إلى هجوم تخمين كلمات المرور",
                ),
                "powershell": (
                    "PowerShell command reference",
                    "إشارة إلى أمر PowerShell",
                ),
            }

            findings = []

            for keyword, descriptions in indicators.items():
                if keyword in text_lower:
                    findings.append(
                        descriptions[0] if is_en else descriptions[1]
                    )

            if findings:
                st.warning(
                    "Indicators found:" if is_en
                    else "تم العثور على مؤشرات:"
                )
                for finding in findings:
                    st.write(f"- {finding}")
            else:
                st.success(
                    "No configured keywords were detected."
                    if is_en else
                    "لم يتم العثور على الكلمات المحددة في قواعد الفحص."
                )

            st.caption(
                "This is a basic keyword check, not an AI model "
                "or a complete threat detection system."
                if is_en else
                "هذا فحص أولي للكلمات، وليس نموذج ذكاء اصطناعي "
                "أو نظام كشف تهديدات متكاملاً."
            )


# =====================================================
# TAB 3: CODE STUDIO
# =====================================================
with tabs[2]:
    st.subheader(
        "💻 Python Code Studio" if is_en
        else "💻 استوديو البرمجة"
    )

    language_options = ["python", "json", "sql", "javascript"]

    code_language = st.selectbox(
        "Programming Language" if is_en else "لغة البرمجة",
        language_options,
    )

    default_code = (
        'print("Hello, SOC!")\n'
        'for number in range(1, 4):\n'
        '    print(number)\n'
    )

    code = st.text_area(
        "Code Editor" if is_en else "محرر الأكواد",
        value=default_code,
        height=260,
    )

    if st.button(
        "Run Python Code" if is_en
        else "تشغيل كود Python",
        key="run_python_code",
    ):
        if code_language != "python":
            st.warning(
                "Only Python execution is supported here."
                if is_en else
                "تشغيل الأكواد متاح للغة Python فقط."
            )
        elif not code.strip():
            st.warning(
                "Enter code first." if is_en else "أدخل الكود أولاً."
            )
        else:
            # Deliberately do not execute arbitrary user-supplied
            # Python inside the Streamlit server.
            st.info(
                "Code execution is disabled for server safety. "
                "Use a properly isolated sandbox to execute arbitrary code."
                if is_en else
                "تشغيل الكود معطّل لحماية الخادم. استخدم بيئة "
                "معزولة وآمنة لتنفيذ الأكواد التي يدخلها المستخدم."
            )

    st.download_button(
        "Download Code" if is_en else "تحميل الكود",
        data=code,
        file_name="soc_code.py" if code_language == "python"
        else f"soc_code.{code_language}",
        mime="text/plain",
    )


# =====================================================
# TAB 4: PHISHING ANALYZER
# =====================================================
with tabs[3]:
    st.subheader(
        "🎣 Phishing URL Analyzer" if is_en
        else "🎣 محلل الروابط المشبوهة"
    )

    url_input = st.text_input(
        "Enter URL" if is_en else "أدخل الرابط",
        placeholder="https://example.com",
    )

    if st.button(
        "Check URL" if is_en else "فحص الرابط",
        key="check_url",
    ):
        if not url_input.strip():
            st.warning(
                "Enter a URL first." if is_en
                else "أدخل الرابط أولاً."
            )
        else:
            candidate = url_input.strip()
            parsed = urlparse(candidate)
            findings = []

            if parsed.scheme.lower() not in ("http", "https"):
                findings.append(
                    "URL must use HTTP or HTTPS."
                    if is_en else
                    "يجب أن يبدأ الرابط ببروتوكول HTTP أو HTTPS."
                )

            if not parsed.hostname:
                findings.append(
                    "Hostname is missing or the URL is malformed."
                    if is_en else
                    "اسم النطاق مفقود أو صيغة الرابط غير صحيحة."
                )

            if parsed.username or parsed.password:
                findings.append(
                    "Credentials appear inside the URL."
                    if is_en else
                    "الرابط يحتوي على بيانات دخول ضمن عنوانه."
                )

            host = (parsed.hostname or "").lower()

            if host.startswith("xn--") or ".xn--" in host:
                findings.append(
                    "Internationalized domain: check for lookalike characters."
                    if is_en else
                    "نطاق بأحرف دولية: تحقق من احتمال تقليد اسم نطاق معروف."
                )

            if "@" in candidate:
                findings.append(
                    "The URL contains an @ character."
                    if is_en else
                    "الرابط يحتوي على الرمز @."
                )

            if parsed.scheme.lower() == "http":
                findings.append(
                    "The URL does not use HTTPS."
                    if is_en else
                    "الرابط لا يستخدم HTTPS."
                )

            if host and not (
                host == "localhost"
                or re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", host)
                or "." in host
            ):
                findings.append(
                    "The hostname looks unusual."
                    if is_en else
                    "اسم النطاق يبدو غير معتاد."
                )

            if findings:
                st.warning(
                    "Review these indicators:"
                    if is_en else
                    "راجع المؤشرات التالية:"
                )
                for item in findings:
                    st.write(f"- {item}")
            else:
                st.info(
                    "No configured URL indicators were detected. "
                    "This does not prove the URL is safe."
                    if is_en else
                    "لم تُكتشف المؤشرات المحددة، لكن هذا لا يثبت أن الرابط آمن."
                )

            st.caption(
                "Offline checks only. The URL is not opened or submitted "
                "to an external service."
                if is_en else
                "الفحص محلي فقط؛ لن يتم فتح الرابط أو إرساله إلى خدمة خارجية."
            )


# =====================================================
# TAB 5: GOOGLE OAUTH
# =====================================================
with tabs[4]:
    st.subheader(
        "🌐 Google OAuth Integration"
        if is_en else
        "🌐 تكامل تسجيل الدخول عبر Google"
    )

    st.write(
        "Google sign-in requires a configured OAuth client, "
        "redirect URI, and server-side verification."
        if is_en else
        "يتطلب تسجيل الدخول عبر Google إعداد عميل OAuth وعنوان "
        "إعادة توجيه والتحقق من بيانات المصادقة على الخادم."
    )

    st.info(
        "Google OAuth is not configured in this application."
        if is_en else
        "لم تتم تهيئة Google OAuth في هذا التطبيق."
    )

    st.markdown(
        "- Create an OAuth client in Google Cloud.\n"
        "- Configure authorized redirect URLs.\n"
        "- Store credentials in Streamlit secrets.\n"
        "- Verify identity using a supported OAuth library."
        if is_en else
        "- أنشئ عميل OAuth في Google Cloud.\n"
        "- أضف عناوين إعادة التوجيه المسموح بها.\n"
        "- خزّن بيانات الاعتماد في Streamlit Secrets.\n"
        "- تحقق من الهوية باستخدام مكتبة OAuth موثوقة."
    )


# =====================================================
# TAB 6: BUG BOUNTY
# =====================================================
with tabs[5]:
    st.subheader(
        "💰 Bug Bounty Workspace"
        if is_en else
        "💰 مساحة عمل صيد الثغرات"
    )

    st.write(
        "Use this checklist only on systems you own or are "
        "explicitly authorized to test."
        if is_en else
        "استخدم قائمة الفحص على الأنظمة التي تملكها أو لديك "
        "تصريح واضح لاختبارها فقط."
    )

    bounty_tasks = [
        "Confirm written authorization",
        "Define scope and excluded assets",
        "Review security headers",
        "Check authentication and access control",
        "Document reproducible findings",
        "Remove secrets and personal data from reports",
    ]

    bounty_tasks_ar = [
        "التأكد من وجود تصريح مكتوب",
        "تحديد النطاق والأصول المستثناة",
        "مراجعة ترويسات الأمان",
        "فحص المصادقة والتحكم بالوصول",
        "توثيق النتائج القابلة لإعادة الاختبار",
        "حذف الأسرار والبيانات الشخصية من التقارير",
    ]

    for i, task in enumerate(bounty_tasks):
        st.checkbox(
            task if is_en else bounty_tasks_ar[i],
            key=f"bounty_task_{i}",
        )

    report = st.text_area(
        "Finding Notes" if is_en else "ملاحظات الثغرة",
        height=150,
    )

    st.download_button(
        "Download Notes" if is_en else "تحميل الملاحظات",
        data=report,
        file_name="bug_bounty_notes.txt",
        mime="text/plain",
    )


# =====================================================
# TAB 7: RANSOMWARE DEFENSE
# =====================================================
with tabs[6]:
    st.subheader(
        "🔒 Ransomware Defense"
        if is_en else
        "🔒 الحماية من برمجيات الفدية"
    )

    defense_steps = [
        (
            "Maintain offline or immutable backups",
            "احتفظ بنسخ احتياطية منفصلة أو غير قابلة للتعديل"
        ),
        (
            "Enable multi-factor authentication",
            "فعّل المصادقة متعددة العوامل"
        ),
        (
            "Patch operating systems and applications",
            "حدّث أنظمة التشغيل والتطبيقات"
        ),
        (
            "Restrict administrator privileges",
            "قيّد صلاحيات المسؤول"
        ),
        (
            "Monitor unusual file changes",
            "راقب التغييرات غير المعتادة على الملفات"
        ),
        (
            "Prepare an incident response plan",
            "جهّز خطة للاستجابة للحوادث"
        ),
    ]

    for i, (english, arabic) in enumerate(defense_steps):
        st.checkbox(
            english if is_en else arabic,
            key=f"ransomware_step_{i}",
        )

    st.warning(
        "This module provides defensive guidance; it does not "
        "detect or remove ransomware from your device."
        if is_en else
        "هذه الوحدة تقدم إرشادات دفاعية فقط، ولا تكشف برمجيات "
        "الفدية أو تزيلها من جهازك."
    )


# =====================================================
# TAB 8: NETWORK TOOLS
# =====================================================
with tabs[7]:
    st.subheader(
        "⚡ Network Utilities" if is_en
        else "⚡ أدوات الشبكة"
    )

    st.write(
        "Validate a target address format without sending network traffic."
        if is_en else
        "تحقق من صيغة عنوان الموقع دون إرسال أي حركة مرور للشبكة."
    )

    target = st.text_input(
        "Target URL" if is_en else "عنوان الموقع",
        placeholder="https://example.com",
    )

    if st.button(
        "Validate Address" if is_en
        else "التحقق من العنوان",
        key="validate_network_address",
    ):
        if not target.strip():
            st.warning(
                "Enter an address first." if is_en
                else "أدخل العنوان أولاً."
            )
        else:
            parsed_target = urlparse(target.strip())

            if (
                parsed_target.scheme in ("http", "https")
                and parsed_target.hostname
                and not parsed_target.username
                and not parsed_target.password
            ):
                st.success(
                    "Address format appears valid."
                    if is_en else
                    "صيغة العنوان تبدو صحيحة."
                )
                st.write(
                    "Hostname:", parsed_target.hostname
                )
                st.write(
                    "Protocol:", parsed_target.scheme.upper()
                )
            else:
                st.error(
                    "Invalid or unsupported URL format."
                    if is_en else
                    "صيغة الرابط غير صحيحة أو غير مدعومة."
                )

    st.caption(
        "No stress tests, flooding, port scans, or requests are performed."
        if is_en else
        "لا يتم تنفيذ اختبارات ضغط أو إغراق أو مسح منافذ أو إرسال طلبات."
    )


# =====================================================
# TAB 9: IMAGE FORENSICS
# =====================================================
with tabs[8]:
    st.subheader(
        "🖼️ Image Forensics" if is_en
        else "🖼️ تحليل الصور"
    )

    uploaded_image = st.file_uploader(
        "Upload an image" if is_en
        else "ارفع صورة للتحليل",
        type=["png", "jpg", "jpeg", "webp", "bmp"],
    )

    if uploaded_image is not None:
        image_bytes = uploaded_image.getvalue()

        try:
            with Image.open(io.BytesIO(image_bytes)) as img:
                img.verify()

            with Image.open(io.BytesIO(image_bytes)) as img:
                st.image(
                    img,
                    caption=uploaded_image.name,
                    use_container_width=True,
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Width" if is_en else "العرض",
                        img.width,
                    )

                with col2:
                    st.metric(
                        "Height" if is_en else "الارتفاع",
                        img.height,
                    )

                with col3:
                    st.metric(
                        "Format" if is_en else "الصيغة",
                        img.format or "Unknown",
                    )

                st.write(
                    "Color mode:" if is_en else "نمط الألوان:",
                    img.mode,
                )

                st.write(
                    "File size:" if is_en else "حجم الملف:",
                    f"{len(image_bytes):,} bytes",
                )

                st.write(
                    "SHA-256:",
                    hashlib.sha256(image_bytes).hexdigest(),
                )

                st.info(
                    "These checks inspect image properties and its hash; "
                    "they do not prove whether the image is authentic."
                    if is_en else
                    "هذا الفحص يعرض خصائص الصورة وبصمتها الرقمية، "
                    "ولا يثبت أن الصورة أصلية أو معدلة."
                )

        except Exception:
            st.error(
                "The uploaded file could not be read as a valid image."
                if is_en else
                "تعذرت قراءة الملف باعتباره صورة صالحة."
            )


# =====================================================
# TAB 10: CRYPTOGRAPHY
# =====================================================
with tabs[9]:
    st.subheader(
        "🔐 Cryptography Tools"
        if is_en else
        "🔐 أدوات التشفير والتجزئة"
    )

    crypto_text = st.text_area(
        "Text to hash" if is_en else "النص المراد حساب بصمته",
        key="crypto_text",
    )

    hash_algorithm = st.selectbox(
        "Algorithm" if is_en else "الخوارزمية",
        ["SHA-256", "SHA-512", "SHA-3-256"],
    )

    if st.button(
        "Calculate Hash" if is_en
        else "حساب البصمة الرقمية",
        key="calculate_hash",
    ):
        if not crypto_text:
            st.warning(
                "Enter text first." if is_en else "أدخل النص أولاً."
            )
        else:
            encoded_text = crypto_text.encode("utf-8")

            if hash_algorithm == "SHA-256":
                digest = hashlib.sha256(encoded_text).hexdigest()
            elif hash_algorithm == "SHA-512":
                digest = hashlib.sha512(encoded_text).hexdigest()
            else:
                digest = hashlib.sha3_256(encoded_text).hexdigest()

            st.code(digest)

    st.divider()

    st.write(
        "A hash is not encryption and cannot be directly decrypted."
        if is_en else
        "البصمة الرقمية ليست تشفيرًا، ولا يمكن فكها مباشرة لاسترجاع النص."
    )


# =====================================================
# TAB 11: PASSWORD SECURITY
# =====================================================
with tabs[10]:
    st.subheader(
        "🧮 Password Strength Checker"
        if is_en else
        "🧮 فحص قوة كلمة المرور"
    )

    password = st.text_input(
        "Test password" if is_en else "كلمة المرور للفحص",
        type="password",
    )

    if st.button(
        "Check Strength" if is_en
        else "فحص القوة",
        key="check_password",
    ):
        if not password:
            st.warning(
                "Enter a password." if is_en
                else "أدخل كلمة المرور."
            )
        else:
            score = 0

            if len(password) >= 12:
                score += 1
            if any(c.islower() for c in password):
                score += 1
            if any(c.isupper() for c in password):
                score += 1
            if any(c.isdigit() for c in password):
                score += 1
            if any(c in string.punctuation for c in password):
                score += 1

            if len(password) < 8:
                result = (
                    "Very short" if is_en else "قصيرة جداً"
                )
                st.error(result)
            elif score <= 2:
                result = (
                    "Weak" if is_en else "ضعيفة"
                )
                st.warning(result)
            elif score <= 4:
                result = (
                    "Moderate" if is_en else "متوسطة"
                )
                st.info(result)
            else:
                result = (
                    "Stronger by these basic checks"
                    if is_en else
                    "أقوى وفق معايير الفحص الأساسية"
                )
                st.success(result)

            st.write(
                f"Criteria met: {score}/5"
                if is_en else
                f"المعايير المتحققة: {score}/5"
            )

            st.caption(
                "This is a basic estimate, not a guarantee of security. "
                "Do not enter a real password you currently use."
                if is_en else
                "هذا تقدير أولي وليس ضمانًا للأمان. لا تدخل كلمة مرور "
                "حقيقية تستخدمها حاليًا."
            )


# =====================================================
# TAB 12: SECURITY CODE LIBRARY
# =====================================================
with tabs[11]:
    st.subheader(
        "📜 Security Code Library"
        if is_en else
        "📜 مكتبة الأكواد الأمنية"
    )

    snippets = {
        "SHA-256 Hash": (
            "import hashlib\n\n"
            'text = "Hello, SOC!"\n'
            'digest = hashlib.sha256(text.encode("utf-8")).hexdigest()\n'
            "print(digest)\n"
        ),
        "Random Token": (
            "import secrets\n\n"
            "token = secrets.token_urlsafe(32)\n"
            "print(token)\n"
        ),
        "HMAC Verification": (
            "import hashlib\n"
            "import hmac\n\n"
            'key = b"example-key"\n'
            'message = b"example-message"\n'
            "signature = hmac.new(key, message, hashlib.sha256).hexdigest()\n"
            "print(signature)\n"
        ),
    }

    snippet_names = list(snippets.keys())

    selected_snippet = st.selectbox(
        "Select example" if is_en else "اختر مثالاً",
        snippet_names,
        format_func=lambda item: (
            item if is_en else {
                "SHA-256 Hash": "حساب SHA-256",
                "Random Token": "إنشاء رمز عشوائي",
                "HMAC Verification": "التحقق باستخدام HMAC",
            }[item]
        ),
    )

    st.code(
        snippets[selected_snippet],
        language="python",
    )

    st.download_button(
        "Download Example" if is_en
        else "تحميل المثال",
        data=snippets[selected_snippet],
        file_name="security_example.py",
        mime="text/x-python",
    )


# =====================================================
# FOOTER
# =====================================================
st.divider()

st.caption(
    "SOC Operations Center | Educational Cybersecurity Project"
    if is_en else
    "غرفة عمليات الأمن السيبراني | مشروع تعليمي قابل للتطوير"
)
