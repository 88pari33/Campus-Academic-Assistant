
import streamlit as st

st.set_page_config(
    page_title="Campus Academic Assistant",
    page_icon="🎓"
)

st.title("🎓 Campus Academic Assistant")

st.write(
    "Welcome! Ask questions about your college syllabus "
    "and academic guidelines."
)

question = st.text_input("Enter your academic question:")

if question:
    st.info(f"Your question: {question}")
    st.write("AI answers will be added in the next steps.")
