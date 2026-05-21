# 🛡️ InsureCast – Real-Time Insurance Premium Category Prediction

InsureCast is a Machine Learning-powered web application that predicts the **Insurance Premium Category** of a user based on lifestyle, income, occupation, BMI, and city tier information.

The project integrates a trained ML model with a **FastAPI backend** and an interactive **Streamlit frontend** to provide real-time predictions.

Predicted categories:
- 🔴 High
- 🟡 Medium
- 🟢 Low

---

# 🚀 Features

- Real-time insurance premium category prediction
- FastAPI backend for ML model serving
- Streamlit frontend UI
- BMI calculation using user inputs
- Lifestyle risk analysis
- City tier classification
- Input validation using Pydantic
- REST API integration

---

# 🧠 Machine Learning Workflow

The ML model predicts insurance premium categories based on:

- Age
- Weight
- Height
- Income (LPA)
- Smoking habits
- Occupation
- City Tier
- BMI
- Lifestyle Risk
- Age Group

The model processes these features and classifies users into:
- High Premium
- Medium Premium
- Low Premium

---
# 📸 Screenshots

## Streamlit Frontend

![InsureCast UI](image(20).png)


# 🛠️ Tech Stack

## Backend
- FastAPI
- Pydantic
- Pandas
- Pickle

## Frontend
- Streamlit
- Requests

## Machine Learning
- Scikit-learn
- Jupyter Notebook

---

# 📂 Project Structure

```bash
InsureCast/
│
├── app.py                 # FastAPI backend
├── frontend.py            # Streamlit frontend
├── model.pkl              # Trained ML model
├── model.ipynb            # Model training notebook
├── requirements.txt
└── README.md
