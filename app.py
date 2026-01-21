import streamlit as st

st.title("🎓 Smart Student Counselling AI Agent")
st.write("Welcome to the AI-based system for automated counseling support.")

name = st.text_input("Student Name")
m = st.number_input("Maths Marks", 0, 100)
s = st.number_input("Science Marks", 0, 100)
e = st.number_input("English Marks", 0, 100)
att = st.number_input("Attendance %", 0, 100)

if st.button("Get AI Counselling"):
    avg = (m + s + e) / 3
    if avg < 50 or att < 60:
        st.error("Risk Level: High Risk")
        st.info("Advice: Needs academic counseling and emotional support.")
    elif avg < 65 or att < 75:
        st.warning("Risk Level: Medium Risk")
        st.info("Advice: Suggesting improvement in academics.")
    else:
        st.success("Risk Level: Low Risk")
        st.info("Advice: Excellent performance! Keep it up.")
  
