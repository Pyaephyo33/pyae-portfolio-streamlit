from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import json

# --- PAGE CONFIG (must be first) ---
st.set_page_config(page_title="Digital CV | Pyae Linn", page_icon=":wave:", layout="wide")

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

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Pyae.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
lottie_file = current_dir / "assets" / "coding-animation.json"

# --- LOAD ASSETS ---
def load_lottie(filepath: Path):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading animation: {e}")
        return None

lottie_coding = load_lottie(lottie_file)
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- MAIN PAGE CONTENT ---
col1, col2 = st.columns(2, gap="small")
with col1:
    if lottie_coding:
        st_lottie(lottie_coding, height=250, key="coding")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📃 Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📬", EMAIL)

# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.markdown("## 💼 Experience & Qualifications")
st.markdown("---")
st.write(
    """
- ✓ 1 year and 1 month of professional experience in **Software Development**  
- ✓ Backend development using **Laravel (PHP)** with solid knowledge of MVC architecture  
- ✓ Frontend experience with **Vue.js** and **React.js** for building responsive, dynamic UIs  
- ✓ Proficient in **Python** for scripting, data analysis, and machine learning  
- ✓ Strong foundation in **Data Science**: data preprocessing, EDA, and statistical analysis  
- ✓ Hands-on experience with **Machine Learning** techniques including classification, regression, and time series forecasting  
- ✓ Familiar with libraries such as **scikit-learn**, **pandas**, **NumPy**, **XGBoost**, and **TensorFlow**  
- ✓ Built ML models for real-world applications like **wind turbine failure prediction** and **personal finance forecasting**  
- ✓ Comfortable with **SQL**, **NoSQL**, **REST APIs**, and working in **Git-based** collaborative environments  
- ✓ Strong analytical thinking, problem-solving skills, and a passion for learning new technologies  
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("🧠 Technical Skills")
st.write("---")
st.write(
    """
- 💻 **Programming Languages**: Python, R, PHP, SQL, JavaScript  
- 🧮 **Data Manipulation & Analysis**: pandas, NumPy  
- 📊 **Data Visualization**: Matplotlib, Seaborn, Plotly  
- 🤖 **Machine Learning & Deep Learning**: scikit-learn, TensorFlow, PyTorch, Keras  
- 🛠️ **Web & Software Development**: React.js, Vue.js, Laravel, Flask  
- 🗄️ **Databases**: MySQL, PostgreSQL, MongoDB  
"""
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("💼 Work Experience")
st.write("---")

st.markdown('<div class="experience-container">', unsafe_allow_html=True)

# Job 1
st.markdown(
    """
    <div class="experience-card">
        <h4>🏢 Junior Web Developer | KMD Group of Companies</h4>
        <small>📍 Yangon, Myanmar | 🗓️ Jul 2023 – Jul 2024</small>
        <ul>
            <li>🔧 Developed and maintained full-stack web applications using <strong>Laravel</strong> and <strong>Blade templating engine</strong></li>
            <li>🎨 Built interactive frontends using <strong>HTML</strong>, <strong>CSS</strong>, <strong>Tailwind CSS</strong>, and <strong>JavaScript</strong></li>
            <li>🚀 Assisted with deploying Laravel applications, focusing on <strong>security</strong>, <strong>performance optimization</strong>, and <strong>environment configuration</strong></li>
            <li>🛠️ Collaborated with the team to implement new features, resolve bugs, and improve overall code quality</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# Job 2
st.markdown(
    """
    <div class="experience-card">
        <h4>🏢 Intern Web Developer | KMD Group of Companies</h4>
        <small>📍 Yangon, Myanmar | 🗓️ Apr 2023 – May 2023</small>
        <ul>
            <li>🌐 Developed and updated the company’s <strong>static website</strong>, implementing new UI designs and feature updates</li>
            <li>🧪 Tested and provided QA support for internal service applications, ensuring reliable functionality and UX</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# --- PROJECTS ---
st.write("#")
st.markdown("## 🚀 Projects")
st.markdown("---")
for project, link in PROJECTS.items():
    st.markdown(f"🔗 **[{project}]({link})**")
