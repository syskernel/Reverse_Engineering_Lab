import streamlit as st
from python_org import org

st.markdown("""
<h1 style="
    font-size: 50px;
    margin-left: 60px;
">
   Welcome to the scraper of python.org!
</h1>
""", unsafe_allow_html=True)

version = st.text_input('Enter the python version which you would like to see!').replace('.', '')
data = org(version)
st.json(data)