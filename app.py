import streamlit as st

st.set_page_config(page_title="Credux.ai", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #E0E0E0;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Welcome to Credux.ai")
st.subheader("Enterprise-Grade AI Architecture")

st.write("Select a service from the sidebar to begin.")
