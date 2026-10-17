import platform
import sys
import streamlit as st

# إعدادات الصفحة الصحيحة
st.set_page_config(page_title="تطبيقي الأول - Streamlit", page_icon="🚀")

# عنوان رئيسي للتطبيق
st.title("🚀 أهلاً بك في تطبيقي التفاعلي الأول")
st.write("تم إنشاء ونشر هذا التطبيق بنجاح عبر GitHub و Streamlit Cloud.")

st.divider()

# قسم معلومات النظام والإصدار
st.subheader("💻 معلومات النظام والإصدار")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="إصدار بايثون", value=sys.version.split()[0])
    st.metric(label="نظام التشغيل", value=platform.system())

with col2:
    st.metric(label="إصدار Streamlit", value=st.__version__)
    st.metric(label="المعمارية", value=platform.machine())

# تفاصيل إضافية كاملة
with st.expander("🔍 اضغط هنا لعرض تفاصيل النظام الكاملة"):
    st.json(
        {
            "Python Full Version": sys.version,
            "OS Release": platform.release(),
            "Platform Details": platform.platform(),
            "Processor": platform.processor(),
        }
    )

st.divider()
st.success("✨ التطبيق يعمل بكفاءة وجاهز لتطويره وإضافة ميزات جديدة!")
