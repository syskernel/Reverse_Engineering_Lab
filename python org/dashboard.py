import streamlit as st
from python_org import org

st.markdown("""
<h1 style="
    font-size: 40px;
    margin-left: 0px;
">
   Welcome to the scraper of python.org!
</h1>
""", unsafe_allow_html=True)

version = st.text_input('Enter the python version which you would like to see!').replace('.', '')
if version:
    data = org(version)
    st.json(data)