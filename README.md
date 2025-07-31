# 📊 NSAP Scheme Eligibility Predictor

This project predicts the **eligible scheme code** for applicants under the **National Social Assistance Programme (NSAP)** using district-wise data and a trained machine learning model. It simplifies eligibility checking using an easy-to-use web interface.

## 🚀 Project Features

- 🧠 Built with IBM Watson AutoAI (Snap Random Forest Classifier)
- 🌐 Frontend connected with Flask backend
- 📁 Sample dataset download option for reference
- ✅ Hosted locally for demo (Flask server)
- 🎨 Polished UI/UX for user-friendly interaction

---

## 🖥️ How it Works

1. User clicks a "Start Prediction" button after reading project purpose.
2. Inputs applicant/district details in a clean form.
3. Backend ML model returns the eligible `scheme code`.
4. User sees the result on screen instantly.

---
## 🗃 Dataset Overview
The dataset contains information on:
- Region (`statename`, `districtname`)
- Welfare scheme (`schemecode`)
- Beneficiary distribution (`totalmale`, `totalfemale`, `totalsc`, `totalobc`, `totalaadhaar`, etc.)

---
## 🎯 ML Objective
- **Task**: Multi-class classification
- **Target Column**: `schemecode`
- **Input Features**: District demographics and scheme statistics
- **Challenge**: Class imbalance – one scheme dominates most districts

## 📈 Model Performance
- Best pipeline: **Snap Random Forest Classifier**
- Accuracy (Cross-validation): **98.4%**
- AutoAI applied feature engineering and hyperparameter optimization

---
## 📷 Screenshots

### 🔍 Model Pipeline
![Experiment Summary](./Screenshot%202025-07-29%20153115.png)

### ⚙️ Pipeline Leaderboard
![Leaderboard](./Screenshot%2025-07-29%153212.png)

### 📊 Bottom Pipelines
![Pipeline Comparison](./Screenshot%202025-07-29%20153245.png)

### 📊 Metrics Comparison
![Data Config](./Screenshot%202025-07-29%20153318.png)

### 🧹 Preprocessing
![Preprocessing Summary](./Screenshot%202025-07-29%20153527.png)

### 🔬 Feature Summary
![Feature Breakdown](./Screenshot%202025-07-29%20153441.png)

---
## 📚 Learnings
- AutoAI makes ML accessible for non-coders
- Accuracy alone can be misleading due to class imbalance
- Important to analyze metrics like F1-score and confusion matrix
- Real-world policy modeling must account for ethical deployment

## 🛠️ Tech Stack

- **IBM Watson AutoAI**
- **Flask (Python)**
- **HTML/CSS/Vanilla JS**
- **Responsive UI with minimal framework**

---
## 👤 Author
**C Sai Bala Krishna**  
📫 [LinkedIn](https://www.linkedin.com/in/c-sai-bala-krishna-5109b5265/)
## 📁 Project Structure

