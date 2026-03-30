# 🎓 Student Performance Predictor – Streamlit Deployment

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Machine Learning](https://img.shields.io/badge/MachineLearning-Classification-orange)
![Model](https://img.shields.io/badge/Model-RandomForest-green)
![Platform](https://img.shields.io/badge/Platform-Streamlit-red)

A supervised machine learning web application built using **Streamlit** to predict students' final grades based on study habits, attendance, motivation, learning style, and other educational features.

---

## 🚀 Live Streamlit App

👉 Click below to use the deployed app:

🔗 https://laya123-star-student-performance-predictor-app-o3lju5.streamlit.app/

---

## 🚀 Run Notebook in Google Colab

Click below to open the notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1YXx3_6zEF7y2lFX7jJyVTtHnSgaNr8s2)

---

# 📘 Project Overview

This project builds and deploys a **Machine Learning Classification Model** to predict students' final grades.

The complete pipeline includes:

* Data Cleaning
  
* Exploratory Data Analysis (EDA)

* Feature Engineering
  
* Feature Scaling
  
* Feature Selection
  
* Model Building
  
* Hyperparameter Tuning
  
* Model Evaluation
  
* Model Deployment using Streamlit

Users can input student details and get **real-time grade predictions**.

---

# 🎯 Objective

The main objectives of this project are:

🔹 Analyze student performance data

🔹 Identify key factors affecting academic success

🔹 Build multiple ML classification models

🔹 Compare model performances

🔹 Optimize the best model using hyperparameter tuning

🔹 Deploy the model using Streamlit

---

# 📂 Dataset Description

| Component       | Description                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------- |
| Target Variable | FinalGrade                                                                                         |
| Problem Type    | Multi-class Classification                                                                         |
| Classes         | A, B, C, D, F                                                                                      |
| Features        | StudyHours, Attendance, Motivation, LearningStyle, Extracurricular, Resources, OnlineCourses, etc. |

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

✔ Loaded dataset using Pandas

✔ Handled missing values

✔ Removed duplicate records

✔ Detected and removed outliers

✔ Scaled numerical features using **StandardScaler**

✔ Split dataset into **Training (80%) and Testing (20%)**

---

# 📊 Exploratory Data Analysis (EDA)

Visualizations used:

* Histogram
  
* Box Plot
  
* Count Plot
  
* Heatmap Correlation
  
* Bar Plot
  
* KDE Plot

### Insights:

* Understood feature distributions
* Identified outliers
* Analyzed feature relationships
* Checked class balance

---

# 🤖 Machine Learning Models Implemented

The following models were trained and evaluated:

* Decision Tree
  
* Random Forest
  
* k-Nearest Neighbors (k-NN)
  
* Support Vector Machine (SVM)
  
* Naive Bayes
  
* Logistic Regression

---

# 📊 Model Performance (Before Tuning)

| Model               | Accuracy | ROC-AUC |
| ------------------- | -------- | ------- |
| Decision Tree       | 0.878    | 0.919   |
| Random Forest       | 0.824    | 0.946   |
| k-NN                | 0.401    | 0.661   |
| SVM (RBF)           | 0.352    | 0.606   |
| Naive Bayes         | 0.287    | 0.532   |
| Logistic Regression | 0.284    | 0.526   |

✅ **Best Model:** Decision Tree

❌ **Worst Model:** Logistic Regression

---

# ⚙️ Hyperparameter Tuning

* Applied **GridSearchCV**
  
* Used **Pipeline** to avoid data leakage
  
* Tuned key parameters for better performance

---

# 📊 Model Performance (After Tuning)

| Model               | Accuracy | ROC-AUC | Best CV Score |
| ------------------- | -------- | ------- | ------------- |
| Random Forest       | 0.901    | 0.986   | 0.859         |
| k-NN                | 0.899    | 0.950   | 0.860         |
| Decision Tree       | 0.878    | 0.919   | 0.839         |
| SVM (RBF)           | 0.402    | 0.657   | 0.395         |
| Naive Bayes         | 0.287    | 0.532   | 0.255         |
| Logistic Regression | 0.284    | 0.526   | 0.235         |

🏆 **Best Model:** Random Forest Classifier

* Accuracy: **90.1%**
  
* ROC-AUC: **0.986**

---

# 🏆 Final Model

✔ **Random Forest Classifier selected**

✔ Optimized using hyperparameter tuning

✔ Saved using Pickle for deployment

```python
import pickle

pickle.dump(best_rf_model, open("Models/best_rf_model.pkl", "wb"))
```

---

# 📊 Evaluation Metrics

* Accuracy Score
  
* Confusion Matrix
  
* Precision
  
* Recall
  
* F1-Score
  
* ROC-AUC Score
  
* Feature Importance

---

# 🌐 Streamlit Deployment

The trained model is deployed using **Streamlit**.

### Features:

✔ User-friendly interface

✔ Real-time predictions

✔ Input student data easily

✔ Instant grade prediction output

---

# ⚠️ Limitations

* The model depends on the quality and completeness of the dataset
  
* Limited features may not capture all real-world academic influence
  
* Performance may vary for students from different educational systems
  
* Does not include psychological or external environmental factors
  
* Model may not generalize well to unseen or highly imbalanced data

---

# 🛠 Tech Stack

| Tool                 | Purpose                   |
| -------------------- | ------------------------- |
| Python               | Programming language      |
| Pandas               | Data handling             |
| NumPy                | Numerical computation     |
| Scikit-learn         | ML models & preprocessing |
| Matplotlib / Seaborn | Visualization             |
| Pickle               | Model saving              |
| Streamlit            | Web app deployment        |
| Google Colab         | Development               |

---

# 📁 Repository Structure

student-performance-predictor/

│

├── app.py

├── Models/

│   └── best_rf_model.pkl

├── notebook.ipynb

├── README.md

---

# 🚀 How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd student-performance-predictor
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 📌 Academic Submission

This repository was developed as part of a **Machine Learning & Data Science program** to demonstrate data preprocessing, exploratory data analysis (EDA), model building, hyperparameter tuning, and deployment of a machine learning model using Streamlit for real-time student performance prediction.

# 👤 Author

**Name:** Laya Mary Joy

**Organization:** Entri Elevate

**Date:** February 14, 2026

---

# ⭐ Acknowledgment

Thanks to **Entri Elevate** for guidance and support in building this project.

---

# 📌 Future Improvements

* Add more student behavioral features
  
* Improve model generalization
  
* Deploy using Docker / Cloud platforms
  
* Add visualization dashboard

---
