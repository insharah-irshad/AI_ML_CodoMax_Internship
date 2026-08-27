# AI Student Performance Predictor

A Machine Learning web application that predicts a student's expected final score based on academic performance and study-related factors.

This project was developed as the final project for **Module 6 of the CodoMax AI/ML Internship**.

---

## Project Overview

The AI Student Performance Predictor uses a Machine Learning regression model to estimate a student's final score from five input features:

- Study Hours
- Attendance
- Previous Score
- Assignments Completed
- Sleep Hours

The project demonstrates the complete Machine Learning workflow, from dataset creation and preprocessing to model training, evaluation, prediction, and deployment through Streamlit.

---

## Objectives

The main objectives of this project are to:

- Apply Machine Learning concepts learned during the internship.
- Work with a structured dataset using Python.
- Train a regression model using Scikit-learn.
- Evaluate the model using standard regression metrics.
- Build an interactive prediction interface.
- Visualize student performance factors.
- Deploy the trained model through a Streamlit application.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

---

## Machine Learning Model

The project uses **Linear Regression** for predicting the student's final score.

Linear Regression was selected because the target variable, `Final_Score`, is a continuous numerical value.

### Input Features

| Feature | Description |
|---|---|
| Study_Hours | Number of hours spent studying per day |
| Attendance | Student attendance percentage |
| Previous_Score | Previous academic score |
| Assignments_Completed | Number of completed assignments |
| Sleep_Hours | Average sleep hours per day |

### Target Variable

`Final_Score`

The model predicts the expected final score on a scale from 0 to 100.

---

## Dataset

A synthetic dataset containing **200 student records** was created for this project.

The dataset contains six numerical columns:

```text
Study_Hours
Attendance
Previous_Score
Assignments_Completed
Sleep_Hours
Final_Score

The dataset was divided into:

Training samples: 160
Testing samples: 40

This represents an 80/20 train-test split.


# Machine Learning Workflow

The project follows these steps:

Dataset Creation
       ↓
Data Loading
       ↓
Data Exploration
       ↓
Feature Selection
       ↓
Train-Test Split
       ↓
Linear Regression Training
       ↓
Prediction
       ↓
Model Evaluation
       ↓
Model Serialization
       ↓
Streamlit Application

# Model Evaluation

The trained model was evaluated using three standard regression metrics.

Metric	Result
Mean Absolute Error (MAE)	3.36
Root Mean Squared Error (RMSE)	4.38
R² Score	0.86

# Interpretation

An MAE of 3.36 means that the model's predictions differ from the actual scores by approximately 3.36 points on average.

An RMSE of 4.38 indicates the overall prediction error while giving more weight to larger errors.

The R² score of 0.86 indicates that the model explains approximately 86% of the variation in the target variable within this dataset.

# Streamlit Application

The project includes an interactive Streamlit dashboard.

Users can enter:

Study hours per day
Attendance
Previous score
Assignments completed
Sleep hours per day

After clicking Predict Performance, the application generates:

Predicted final score
Performance level
Prediction progress
Student profile
Input visualization

The application also displays the trained model's evaluation metrics.

# Project Structure
AI_Student_Performance_Predictor/
│
├── data/
│   └── student_performance.csv
│
├── models/
│   └── student_performance_model.pkl
│
├── app.py
├── create_dataset.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore

# Key Features
## Interactive Prediction

Users can adjust student information using sidebar controls and generate predictions instantly.

## Model Evaluation

The dashboard displays:

MAE
RMSE
R² Score
Data Visualization

The application provides a visual overview of the student's input factors.

## Saved Model

The trained model is serialized using Joblib and loaded directly by the Streamlit application.

# Learning Outcomes

Through this project, I practiced:

Python programming
Dataset creation
Pandas data handling
NumPy fundamentals
Feature and target selection
Train-test splitting
Regression modelling
Linear Regression
Model prediction
MAE, RMSE, and R² evaluation
Data visualization
Model serialization with Joblib
Streamlit application development

