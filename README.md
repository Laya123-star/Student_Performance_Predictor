# 🎓 Student Performance Predictor – Streamlit Deployment

A supervised machine learning web application built using **Streamlit** to predict the **final grade of students** based on study habits, attendance, motivation, learning style, and other educational features.

---
# 🎓 Student Performance Predictor – Streamlit Deployment

## 🚀 Live Streamlit App

👉 **Click here to use the app:**  
https://laya123-star-student-performance-predictor-app-o3lju5.streamlit.app/

---

## 📘 Project Overview

- This project builds and deploys a **Random Forest Classifier** to predict students’ final grades.  
- The dataset contains student-related numerical and categorical features.  
- The best-performing trained model is deployed as a **Streamlit web app**.  
- Users can input student data to get real-time predictions of final grades.

---

## 🎯 Objective

The project includes:

🔹 Data Cleaning  
🔹 Exploratory Data Analysis (EDA)  
🔹 Feature Engineering  
🔹 Feature Scaling  
🔹 Feature Selection  
🔹 Model Building (Random Forest)  
🔹 Hyperparameter Tuning  
🔹 Model Evaluation  
🔹 Model Saving using Pickle  
🔹 Streamlit Web App Deployment  

---

## 📂 Dataset Description

| Component | Description |
|------------|-------------|
| Target Variable | FinalGrade |
| Classes | e.g., A, B, C, D, F (or numeric scale if applicable) |
| Problem Type | Multi-class Classification |
| Features | StudyHours, Attendance, Motivation, LearningStyle, Extracurricular, Resources, OnlineCourses, etc. |

---

## 🧹 Data Preprocessing Steps

✔ Dataset loaded using Pandas  
✔ Checked and handled missing values  
✔ Removed duplicates  
✔ Checked and removed Outliers.  
✔ Scaled numerical features using **StandardScaler**  
✔ Split dataset into Training and Testing sets (80:20)  

---

## 📊 Exploratory Data Analysis (EDA)

Visualizations used:

- Histogram  
- Box Plot  
- Count Plot  
- Heatmap Correlation  
- Bar Plot  
- KDE Plot  

EDA helped in:

- Understanding feature distribution  
- Identifying outliers  
- Detecting correlations  
- Checking class balance  

---

## 🤖 Machine Learning Model Implemented

- **Random Forest Classifier** (best-performing model)  

Other models may have been explored (SVM, Logistic Regression, Decision Tree, Naive Bayes, K-Nearest Neighbours) during experiments in **Colab notebook**.

---

## ⚙️ Hyperparameter Tuning

- GridSearchCV applied for optimal parameters  
- Pipeline used to avoid data leakage  

---

## 📊 Model Evaluation Metrics

Evaluation included:

- Accuracy Score  
- Confusion Matrix  
- Precision, Recall, F1-Score  
- Feature Importance  

---

## 🏆 Best Performing Model

✔ Random Forest Classifier selected as the best model  
✔ Saved using Pickle for deployment  

```python
import pickle

pickle.dump(best_rf_model, open("Models/best_rf_model.pkl", "wb"))
