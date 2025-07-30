# app.py
import streamlit as st
import joblib
import numpy as np

st.title("🧠 SkillElevate AI-Powered Career Growth and Salary Optimization System")
st.markdown("Provide your **Qualifications**, **Experience**, and **Skills** to get predicted job outcomes.")

# Load encoders for input
qual_enc = joblib.load('models/Qualifications_encoder.pkl')
exp_enc = joblib.load('models/Experience_encoder.pkl')
skills_enc = joblib.load('models/skills_encoder.pkl')

# Load models and output encoders
target_fields = ['Job Title', 'Role', 'Work Type', 'Company', 'location', 'Country', 'Salary Range']
models = {field: joblib.load(f'models/{field}_model.pkl') for field in target_fields}
encoders = {field: joblib.load(f'models/{field}_encoder.pkl') for field in target_fields}

# Input section
qual_input = st.selectbox("Select Qualification", qual_enc.classes_)
exp_input = st.selectbox("Select Experience", exp_enc.classes_)
skill_input = st.selectbox("Select Skill", skills_enc.classes_)

# Convert to encoded input
try:
    qual_val = qual_enc.transform([qual_input])[0]
    exp_val = exp_enc.transform([exp_input])[0]
    skill_val = skills_enc.transform([skill_input])[0]
except:
    st.error("Invalid input combination.")
    st.stop()

input_data = np.array([[qual_val, exp_val, skill_val]])

if st.button("Predict Job Info"):
    st.markdown("### 🔍 Predictions:")
    for field in target_fields:
        model = models[field]
        encoder = encoders[field]
        pred = model.predict(input_data)[0]
        label = encoder.inverse_transform([pred])[0]
        st.write(f"**{field}:** {label}")
