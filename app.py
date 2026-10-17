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
  st.caption("🚀 CyberStudio Suite v3.0 (Master Edition)")

# 3. العنوان الرئيسي
st.title("🛡️ CyberStudio Pro — المنصة الأمنية الشاملة")
st.markdown("### **Developed & Designed by: Fadil I. Hussein**")
st.write(
    "لوحة تحكم متقدمة تضم أدوات التشفير، فحص التصيد، محاكاة الهجمات، وتحليل"
    " الثغرات."
)
st.divider()

# 4. التبويبات المتقدمة (تشمل الأدوات السابقة + أقسام الأشهر في الأمن السيبراني)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "💻 النظام والسيرفر",
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
    st.metric(label="إصدار بايث
