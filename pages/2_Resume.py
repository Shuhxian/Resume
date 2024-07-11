import streamlit as st
import base64
from constant import info

st.set_page_config(page_title="Goy's Resume" ,layout="wide", page_icon="📝")

st.header("Resume")

with open("resources/Goy_Shuh_Xian_Resume.pdf","rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000mm" height="1000mm" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
  
