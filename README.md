# SkillElevate: AI-Powered Career Growth and Salary Optimization System

**Internship Title**: EDUNET FOUNDATION - IBM SKILLSBUILD - ARTIFICIAL INTELLIGENCE  
**Project Title**: SkillElevate: AI-Powered Career Growth and Salary Optimization System  
**Intern**: Utsav Raj

---

## 📌 Project Overview

**SkillElevate** is an intelligent machine learning-based system designed to help individuals explore optimal job roles, companies, work types, and salary expectations based on their educational qualifications, experience, and skills.

The system uses real-world job data to build predictive models that provide personalized recommendations, guiding users towards better career decisions and salary insights.

---
## 🎯 Objectives

- Predict relevant career opportunities based on user profile.
- Estimate expected salary range using industry data.
- Provide personalized suggestions for:
  - 🎓 Job Title
  - 👨‍💼 Role
  - 🏢 Company
  - 🕒 Work Type
  - 🌍 Location & Country
  - 💸 Salary Range

---
## 🧠 Features

- Predicts **Job Title**, **Role**, **Work Type**, **Company**, **Location**, **Country**, and **Salary Range**
- Input required: `Qualifications`, `Experience`, and `Skills`
- Trained with machine learning models (Random Forest Classifier)
- Interactive web interface built using **Streamlit**
- Modular and scalable code for future enhancements

---

## 🧰 Tech Stack

| Tool / Library         | Purpose                            |
|------------------------|------------------------------------|
| Python (3.9+)          | Programming language               |
| Pandas, NumPy          | Data preprocessing                 |
| scikit-learn           | ML model training                  |
| Joblib                 | Model serialization                |
| Streamlit              | Web-based UI                       |

---

## 📂 Project Structure
SkillElevate/
│
├── models/ # Saved ML models and encoders
│ ├── Job Title_model.pkl
│ ├── Role_model.pkl
│ ├── ...
│
├── job_data.csv # Source job dataset (cleaned)
├── model_train.py # Model training script
├── app.py # Streamlit web application
├── README.md # Project documentation


---

## 🔄 Workflow

1. **Preprocessing**:
   - Drop irrelevant or missing data
   - Encode categorical fields (e.g., qualifications, experience, skills)

2. **Model Training**:
   - One RandomForestClassifier per target field
   - Save models and encoders with `joblib`

3. **Prediction**:
   - User enters input in web app
   - Predictions displayed for each output category

---

## 🧪 Example Usage (Streamlit)

**Input**
- Qualifications: `M.Tech`
- Experience: `3 to 5 Years`
- Skills: `Python, Data Science, SQL`

**Predicted Output**
- Job Title: `Data Analyst`
- Role: `Business Intelligence Analyst`
- Company: `Infosys`
- Work Type: `Full-Time`
- Location: `Bengaluru`
- Country: `India`
- Salary Range: `₹6.5L – ₹10L`

---

## ⚙️ Setup & Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/utsavraj1/SkillElevate.git
cd SkillElevate
```
### 2. Install Requirements
```bash
pip install -r requirements.txt
```
### 3. Train Models (only once)
```bash
python model_train.py
```
### 4. Run Web App
```bash
streamlit run app.py
```

### 📊 Dataset Details
- Total Records: 1.6 Million+
- Fields: Job Title, Experience, Qualifications, Skills, Salary Range, Company, Location, etc.
- Preprocessing: Null value removal, Label Encoding, Feature Selection

### 🙏 Acknowledgements
- IBM SkillsBuild & Edunet Foundation – for mentorship and learning platform
- Mentors & Trainers – for consistent support and guidance
- Kaggle / StackOverflow Jobs Dataset – for initial data inspiration

### 💬 Feedback
- If you have suggestions or improvements, feel free to raise an issue or submit a pull request!
- LinkedIn : https://www.linkedin.com/in/utsavraj123/
