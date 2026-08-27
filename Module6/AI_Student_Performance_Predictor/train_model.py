import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import numpy as np
import joblib


# -------------------------------
# Load Dataset
# -------------------------------

data = pd.read_csv("data/student_data.csv")


# -------------------------------
# Basic Data Analysis
# -------------------------------

print("Dataset Shape:")
print(data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nStatistical Summary:")
print(data.describe())


# -------------------------------
# Data Visualization
# -------------------------------

# Study Hours vs Final Score
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=data,
    x="Study_Hours",
    y="Final_Score"
)

plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.tight_layout()

plt.savefig("study_hours_vs_score.png")
plt.show()


# Attendance vs Final Score
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=data,
    x="Attendance",
    y="Final_Score"
)

plt.title("Attendance vs Final Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.tight_layout()

plt.savefig("attendance_vs_score.png")
plt.show()


# Correlation Heatmap
plt.figure(figsize=(9, 6))

correlation = data.corr(
    numeric_only=True
)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Feature Correlation Heatmap")
plt.tight_layout()

plt.savefig("correlation_heatmap.png")
plt.show()


# -------------------------------
# Feature Selection
# -------------------------------

features = [
    "Study_Hours",
    "Attendance",
    "Previous_Score",
    "Assignments_Completed",
    "Sleep_Hours"
]

X = data[features]

y = data["Final_Score"]


# -------------------------------
# Train-Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


print("\nTrain-Test Split:")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# -------------------------------
# Train Linear Regression Model
# -------------------------------

model = LinearRegression()

model.fit(
    X_train,
    y_train
)


print("\nModel trained successfully.")


# -------------------------------
# Make Predictions
# -------------------------------

y_pred = model.predict(
    X_test
)


print("\nPredictions:")
print(y_pred[:10])


# -------------------------------
# Model Evaluation
# -------------------------------

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

r2 = r2_score(
    y_test,
    y_pred
)


print("\nModel Evaluation:")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")


# -------------------------------
# Save Model
# -------------------------------

joblib.dump(
    model,
    "models/student_performance_model.pkl"
)


print(
    "\nModel saved successfully to "
    "models/student_performance_model.pkl"
)

# -------------------------------
# Actual vs Predicted Visualization
# -------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    y_test,
    y_pred,
    alpha=0.7
)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)

plt.title("Actual vs Predicted Final Scores")
plt.xlabel("Actual Final Score")
plt.ylabel("Predicted Final Score")

plt.tight_layout()

plt.savefig(
    "actual_vs_predicted.png"
)

plt.show()


print(
    "Actual vs Predicted visualization saved successfully."
)