# model_train.py
import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Create models directory if not exists
os.makedirs('models', exist_ok=True)

# Load dataset
df = pd.read_csv('job_data.csv')

# Drop unnecessary columns
df = df.drop(columns=['Job Id', 'Job Description', 'Benefits', 'Responsibilities', 'Contact', 
                      'Contact Person', 'Job Posting Date', 'Company Profile', 'Job Portal'], errors='ignore')

# Drop rows with missing important fields
df = df.dropna(subset=['Qualifications', 'Experience', 'skills'])

# Encode input features
label_encoders = {}
for col in ['Qualifications', 'Experience', 'skills']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

# Define input features
X = df[['Qualifications', 'Experience', 'skills']]
target_columns = ['Job Title', 'Role', 'Work Type', 'Company', 'location', 'Country', 'Salary Range']

# Train and save one model per target (lightweight RF)
for target in target_columns:
    print(f"🔄 Training model for {target}...")

    y = df[target].astype(str)
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    X_train, _, y_train, _ = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    # Memory-efficient RF
    model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    # Save model and encoder
    joblib.dump(model, f'models/{target}_model.pkl')
    joblib.dump(le, f'models/{target}_encoder.pkl')
    print(f"✅ Saved: {target}_model.pkl & encoder")

# Save input encoders
for col, le in label_encoders.items():
    joblib.dump(le, f'models/{col}_encoder.pkl')

print("\n🎉 All models and encoders saved successfully in 'models/' directory.")
