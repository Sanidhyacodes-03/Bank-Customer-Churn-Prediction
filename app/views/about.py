import streamlit as st


def show():

    # ==========================================
    # HERO
    # ==========================================

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#2563EB,#7C3AED);
    padding:30px;
    border-radius:20px;
    color:white;
    margin-bottom:25px;
    ">

    <h1>ℹ️ About This Project</h1>

    <p style="font-size:18px;">
    AI-powered Bank Customer Churn Prediction System
    built using Machine Learning and Streamlit.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.info(
        "This project helps banks identify customers who are likely to leave and enables proactive customer retention strategies."
    )

    st.divider()

        # ==========================================
    # PROJECT OVERVIEW
    # ==========================================

    st.markdown("## 🎯 Project Overview")

    st.success("""
### Bank Customer Churn Prediction Dashboard

Customer churn is one of the biggest challenges in the banking industry.

This application uses a **Random Forest Machine Learning model** to predict whether a customer is likely to leave the bank.

The dashboard enables banks to analyze customer behavior, visualize important trends, and make informed business decisions using predictive analytics.
""")

    st.divider()

        # ==========================================
    # OBJECTIVES
    # ==========================================

    st.markdown("## 🚀 Project Objectives")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
### Objectives

- Predict customer churn
- Analyze customer behaviour
- Improve customer retention
- Support business decisions
- Build an interactive analytics dashboard
""")

    with col2:

        st.info("""
### Technologies

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Plotly
- Joblib
""")

    st.divider()

        # ==========================================
    # MACHINE LEARNING
    # ==========================================

    st.markdown("## 🤖 Machine Learning Workflow")

    st.success("""
1️⃣ Data Collection

2️⃣ Data Cleaning & Preprocessing

3️⃣ Exploratory Data Analysis

4️⃣ Feature Engineering

5️⃣ Model Training

6️⃣ Model Evaluation

7️⃣ Customer Churn Prediction
""")

    st.divider()

    # ==========================================
    # FEATURES
    # ==========================================

    st.markdown("## ⭐ Application Features")

    st.info("""
- 📊 Interactive Dashboard
- 🔮 Customer Churn Prediction
- 📈 Exploratory Data Analysis
- 📉 Model Performance Evaluation
- ⭐ Feature Importance Analysis
- 📄 Download Prediction Report
- 💡 Business Recommendations
""")

    st.divider()

        # ==========================================
    # FUTURE IMPROVEMENTS
    # ==========================================

    st.markdown("## 🚀 Future Improvements")

    st.warning("""
- Deploy the application to the cloud.
- Integrate with real-time banking databases.
- Add advanced machine learning models.
- Implement customer segmentation.
- Enable automated retention recommendations.
""")

    st.divider()

    # ==========================================
    # DEVELOPER
    # ==========================================

    st.markdown("## 👨‍💻 Developer")

    st.success("""
### Developed by

**Sanidhya Singh Sisodiya**

Python • Machine Learning • Data Analytics • Streamlit
""")

    st.divider()

    st.markdown("""
<div style="
background:#1E293B;
padding:20px;
border-radius:15px;
text-align:center;
color:white;
">

### 🏦 Bank Customer Churn Prediction Dashboard

Built using  Python, Streamlit and Machine Learning

</div>
""", unsafe_allow_html=True)