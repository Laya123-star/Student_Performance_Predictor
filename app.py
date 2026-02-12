import streamlit as st
import pandas as pd
import pickle
import os
from PIL import Image

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance Intelligence System",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}
h1, h2, h3 {
    color: #4da6ff;
}
.stButton>button {
    border-radius: 8px;
    height: 45px;
    font-weight: bold;
}
.metric-card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}
.result-card {
    background: linear-gradient(135deg, #1f77b4, #4da6ff);
    padding: 40px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGO ----------------
if os.path.exists("logo.png"):
    logo = Image.open("logo.png")
    st.image(logo, width=120)

# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    with open("Models/best_rf_model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

# ---------------- MODEL INFO ----------------
MODEL_NAME = "Random Forest Classifier"
MODEL_ACCURACY = 0.87

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "prediction" not in st.session_state:
    st.session_state.prediction = None

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 Navigation")
menu = st.sidebar.radio(
    "Select Menu",
    ["🏠 Home", "🤖 Model Information", "📊 Student Performance"]
)

# ======================================================
# ======================== HOME ========================
# ======================================================
if menu == "🏠 Home":
    st.title("🎓 Student Performance Dashboard")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="metric-card"><h3>Model</h3><p>{MODEL_NAME}</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="metric-card"><h3>Accuracy</h3><p>{MODEL_ACCURACY*100:.2f}%</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>Status</h3><p>Production Ready 🚀</p></div>', unsafe_allow_html=True)

    st.markdown("---")
    st.write("""
    This AI-powered system predicts student final grade using
    behavioral, engagement, academic and psychological indicators.
    """)

# ======================================================
# ================= MODEL INFO ========================
# ======================================================
elif menu == "🤖 Model Information":
    st.title("🤖 Model Information")
    st.markdown(f"""
    - **Model Name:** {MODEL_NAME}
    - **Algorithm:** Random Forest
    - **Validation Accuracy:** {MODEL_ACCURACY*100:.2f}%
    """)

# ======================================================
# =============== STUDENT PERFORMANCE =================
# ======================================================
elif menu == "📊 Student Performance":

    # ---------------- FORM PAGE ----------------
    if st.session_state.page == "home":
        st.title("📊 Student Performance Prediction")

        col1, col2, col3 = st.columns(3)

        with col1:
            StudyHours = float(st.number_input("Study Hours (0-24)", 0, 24, step=1))
            Attendance = float(st.number_input("Attendance (%)", 0, 100, step=1))
            Resources = int(st.selectbox("Resources (0-2)", [0,1,2]))
            Extracurricular = int(st.selectbox("Extracurricular (0/1)", [0,1]))
            Motivation = int(st.selectbox("Motivation (0-2)", [0,1,2]))

        with col2:
            Internet = int(st.selectbox("Internet (0/1)", [0,1]))
            Gender = int(st.selectbox("Gender (0/1)", [0,1]))
            Age = int(st.number_input("Age (18-30)", 18, 30, step=1))
            LearningStyle = int(st.selectbox("Learning Style (0-3)", [0,1,2,3]))
            OnlineCourses = float(st.number_input("Online Courses (0-20)", 0, 20, step=1))

        with col3:
            Discussions = int(st.selectbox("Discussions (0/1)", [0,1]))
            AssignmentCompletion = float(st.number_input("Assignment Completion (%)", 0, 100, step=1))
            EduTech = int(st.selectbox("EduTech (0/1)", [0,1]))
            StressLevel = int(st.selectbox("Stress Level (0-2)", [0,1,2]))

        predict = st.button("🚀 Predict Performance")

        if predict:
            # Validate ranges
            errors = []
            if Attendance < 0 or Attendance > 100:
                errors.append("Attendance must be 0-100.")
            if AssignmentCompletion < 0 or AssignmentCompletion > 100:
                errors.append("Assignment Completion must be 0-100.")
            if Age < 18 or Age > 30:
                errors.append("Age must be 18-30.")
            if OnlineCourses < 0 or OnlineCourses > 20:
                errors.append("Online Courses must be 0-20.")

            if errors:
                for e in errors:
                    st.error(e)
            else:
                # Input dataframe (exact column order as used in training)
                input_df = pd.DataFrame([[ 
                    StudyHours, Attendance, Resources, Extracurricular,
                    Motivation, Internet, Gender, Age,
                    LearningStyle, OnlineCourses, Discussions,
                    AssignmentCompletion, EduTech, StressLevel
                ]], columns=[
                    "StudyHours","Attendance","Resources","Extracurricular",
                    "Motivation","Internet","Gender","Age",
                    "LearningStyle","OnlineCourses","Discussions",
                    "AssignmentCompletion","EduTech","StressLevel"
                ])

                # Predict
                st.session_state.prediction = model.predict(input_df)[0]
                st.session_state.page = "result"  # Navigate to result page

    # ---------------- RESULT PAGE ----------------
    elif st.session_state.page == "result":
        st.title("🎯 Final Grade Prediction")
        st.markdown(
            f'<div class="result-card">Predicted Final Grade Class: {st.session_state.prediction}</div>',
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("⬅ Back to Form"):
            st.session_state.page = "home"
            st.session_state.prediction = None  # Clear prediction
