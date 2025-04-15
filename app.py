from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Pyae.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Pyae Linn"
PAGE_ICON = ":wave:"
NAME = "PYAE LINN"
DESCRIPTION = """
    Data Scientist | ML Enthusiast | Problem Solver
"""
EMAIL = "pyaephyolinn778899@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/pyae-linn-2b0107258/", 
    "GitHub": "https://github.com/Pyaephyo33"
}

PROJECTS = {
    "📌 Fuel Consumption - Machine Learning and Predictive Analysis Project": "https://github.com/Pyaephyo33/fuel_consumption",
    "📌 House Property Price Prediction - Real Estate Pricing Model": "https://github.com/Pyaephyo33/property-pred-backend",
    "📌 Smart Budgeting - ML-powered expense tracker & Spending Prediction with Scikit-Learn": "https://github.com/Pyaephyo33",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# -- HEAD SECTION --
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
    
























