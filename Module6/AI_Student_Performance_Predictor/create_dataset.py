import pandas as pd
import numpy as np


np.random.seed(42)

number_of_students = 200


study_hours = np.random.uniform(
    1,
    10,
    number_of_students
)

attendance = np.random.uniform(
    50,
    100,
    number_of_students
)

previous_score = np.random.uniform(
    40,
    95,
    number_of_students
)

assignments_completed = np.random.randint(
    1,
    11,
    number_of_students
)

sleep_hours = np.random.uniform(
    4,
    9,
    number_of_students
)


final_score = (
    study_hours * 3.5
    + attendance * 0.25
    + previous_score * 0.35
    + assignments_completed * 1.5
    + sleep_hours * 1.0
    + np.random.normal(
        0,
        5,
        number_of_students
    )
)


final_score = np.clip(
    final_score,
    0,
    100
)


data = pd.DataFrame({
    "Study_Hours": study_hours.round(2),
    "Attendance": attendance.round(2),
    "Previous_Score": previous_score.round(2),
    "Assignments_Completed": assignments_completed,
    "Sleep_Hours": sleep_hours.round(2),
    "Final_Score": final_score.round(2)
})


data.to_csv(
    "data/student_data.csv",
    index=False
)


print("Dataset created successfully.")
print()
print(data.head())
print()
print(f"Total students: {len(data)}")