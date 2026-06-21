# ❤️ Heart Disease Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a patient is likely to have heart disease using Machine Learning. Multiple classification algorithms were trained and compared, and the best-performing model (Random Forest) was selected for deployment using Streamlit.....

---
DEMO
<img width="1920" height="881" alt="heart disease prediction(1)Screenshot" src="https://github.com/user-attachments/assets/b5315d5c-b266-4f9c-b805-934a468e7a6e" />
<img width="1920" height="917" alt="heart disease prediction(2)Screenshot" src="https://github.com/user-attachments/assets/fcfe1857-28b0-4ed0-a21a-d702c95b700d"/> 
<img width="1920" height="823" alt="heart disease prediction(3)Screenshot" src="https://github.com/user-attachments/assets/28a978c8-780e-4021-88f5-8cc27c5d8bce" />
## 🚀 Features

- Predicts the likelihood of heart disease
- Interactive Streamlit web application
- Data preprocessing and cleaning
- Correlation heatmap visualization
- Feature importance analysis
- Comparison of multiple machine learning models
- User-friendly prediction interface

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib

---

## 📊 Machine Learning Models

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 77.05% |
| Decision Tree | 73.77% |
| **Random Forest** | **85.25%** |
| K-Nearest Neighbors | 73.77% |

**Best Model:** Random Forest

---

## 📂 Project Structure

```
heart-disease-prediction/
│
├── data/
│   └── heart.csv
│
├── notebooks/
│   └── Heart_Disease_Prediction.ipynb
│
├── images/
│   └── app_screenshot.png
│
├── app.py
├── heart_model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## 📈 Dataset Features

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression (Oldpeak)
- Slope
- Number of Major Vessels (CA)
- Thalassemia

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

## 📌 Future Improvements

- Hyperparameter tuning
- Cross-validation
- Additional evaluation metrics
- Feature selection
- Cloud deployment

---

## 👨‍💻 Author

**Mohd Abdul Razzaq**
