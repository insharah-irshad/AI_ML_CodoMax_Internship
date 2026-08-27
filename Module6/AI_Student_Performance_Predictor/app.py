import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Student Performance Predictor",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# SIMPLE STYLING
# ============================================================

st.title("Student Performance Predictor")

st.write(
    "A Machine Learning application that predicts a student's "
    "expected final score based on academic and study-related factors."
)

st.divider()


# ============================================================
# LOAD MODEL
# ============================================================

try:
    model = joblib.load(
        "models/student_performance_model.pkl"
    )

except FileNotFoundError:

    st.error(
        "Model not found. Please run train_model.py first."
    )

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("Student Predictor")

    st.write(
        "Enter the student's information below."
    )

    st.divider()

    study_hours = st.slider(
        "Study Hours per Day",
        min_value=0.0,
        max_value=12.0,
        value=5.0,
        step=0.5
    )

    attendance = st.slider(
        "Attendance",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=1.0
    )

    previous_score = st.slider(
        "Previous Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )

    assignments_completed = st.slider(
        "Assignments Completed",
        min_value=0,
        max_value=10,
        value=7,
        step=1
    )

    sleep_hours = st.slider(
        "Sleep Hours per Day",
        min_value=0.0,
        max_value=12.0,
        value=7.0,
        step=0.5
    )

    st.divider()

    predict_button = st.button(
        "Predict Performance",
        type="primary",
        width="stretch"
    )


# ============================================================
# MODEL INFORMATION
# ============================================================

st.header("Model Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Training Samples",
        "160"
    )

with col2:
    st.metric(
        "Testing Samples",
        "40"
    )

with col3:
    st.metric(
        "R² Score",
        "0.86"
    )

with col4:
    st.metric(
        "MAE",
        "3.36"
    )


st.divider()


# ============================================================
# PREDICTION
# ============================================================

st.header("Performance Prediction")

st.write(
    "Use the sidebar to enter student information and "
    "generate a predicted final score."
)


if predict_button:

    # --------------------------------------------------------
    # Prepare input
    # --------------------------------------------------------

    input_data = pd.DataFrame(
        {
            "Study_Hours": [study_hours],
            "Attendance": [attendance],
            "Previous_Score": [previous_score],
            "Assignments_Completed": [assignments_completed],
            "Sleep_Hours": [sleep_hours]
        }
    )


    # --------------------------------------------------------
    # Prediction
    # --------------------------------------------------------

    prediction = model.predict(
        input_data
    )[0]

    prediction = max(
        0,
        min(100, prediction)
    )


    # --------------------------------------------------------
    # Performance level
    # --------------------------------------------------------

    if prediction >= 80:

        performance = "High Performance"

    elif prediction >= 60:

        performance = "Moderate Performance"

    else:

        performance = "Needs Improvement"


    # --------------------------------------------------------
    # Main prediction
    # --------------------------------------------------------

    st.success(
        f"Predicted Final Score: {prediction:.2f}"
    )

    st.write(
        f"Performance Level: {performance}"
    )

    st.progress(
        prediction / 100
    )


    # ========================================================
    # STUDENT PROFILE
    # ========================================================

    st.subheader("Student Profile")

    profile1, profile2, profile3, profile4, profile5 = st.columns(5)

    with profile1:

        st.metric(
            "Study Hours",
            f"{study_hours:.1f}"
        )

    with profile2:

        st.metric(
            "Attendance",
            f"{attendance:.0f}%"
        )

    with profile3:

        st.metric(
            "Previous Score",
            f"{previous_score:.0f}"
        )

    with profile4:

        st.metric(
            "Assignments",
            assignments_completed
        )

    with profile5:

        st.metric(
            "Sleep Hours",
            f"{sleep_hours:.1f}"
        )


    # ========================================================
    # VISUALIZATION
    # ========================================================

    st.subheader(
        "Student Input Visualization"
    )

    chart_data = pd.DataFrame(
        {
            "Factor": [
                "Study Hours",
                "Attendance",
                "Previous Score",
                "Assignments",
                "Sleep Hours"
            ],

            "Value": [
                study_hours,
                attendance,
                previous_score,
                assignments_completed,
                sleep_hours
            ]
        }
    )


    fig, ax = plt.subplots(
        figsize=(10, 4)
    )

    ax.bar(
        chart_data["Factor"],
        chart_data["Value"]
    )

    ax.set_title(
        "Student Performance Factors"
    )

    ax.set_ylabel(
        "Value"
    )

    plt.xticks(
        rotation=20
    )

    plt.tight_layout()

    st.pyplot(
        fig,
        width="stretch"
    )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.divider()

st.header("Model Performance")

performance_data = pd.DataFrame(
    {
        "Evaluation Metric": [
            "Mean Absolute Error",
            "Root Mean Squared Error",
            "R² Score"
        ],

        "Value": [
            3.36,
            4.38,
            0.86
        ]
    }
)

st.dataframe(
    performance_data,
    width="stretch",
    hide_index=True
)


# ============================================================
# FEATURES
# ============================================================

st.header("Features Used by the Model")

feature1, feature2, feature3 = st.columns(3)

with feature1:

    st.subheader("Study Habits")

    st.write(
        "Daily study hours provide an indication "
        "of the student's study habits."
    )


with feature2:

    st.subheader("Academic History")

    st.write(
        "Previous score and assignment completion "
        "represent previous academic performance."
    )


with feature3:

    st.subheader("Student Routine")

    st.write(
        "Attendance and sleep hours are used as "
        "additional student performance factors."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Student Performance Predictor | "
    "Python | Pandas | Scikit-learn | Streamlit"
)