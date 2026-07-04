import streamlit as st


def show(BASE_DIR):

    figures = BASE_DIR / "outputs" / "figures"

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

    <h1>📈 Model Performance Analysis</h1>

    <p style="font-size:18px;">
    Evaluate the performance of the Random Forest model using
    multiple classification metrics and visualizations.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.info(
        "This section evaluates how effectively the trained Random Forest model predicts customer churn."
    )

    st.divider()

        # ==========================================
    # MODEL SUMMARY
    # ==========================================

    st.markdown("## 🏆 Random Forest Performance Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Model",
            "Random Forest"
        )

    with c2:
        st.metric(
            "Algorithm",
            "Ensemble"
        )

    with c3:
        st.metric(
            "Prediction",
            "Binary"
        )

    with c4:
        st.metric(
            "Target",
            "Customer Churn"
        )

    st.divider()

    # ==========================================
    # CONFUSION MATRIX
    # ==========================================

    st.markdown("## 📊 Confusion Matrix")

    left, right = st.columns([1.4,1])

    with left:

        st.image(
            str(figures / "confusion_matrix.png"),
            use_container_width=True
        )

    with right:

        st.success("""
### 💡 Business Insight

The Confusion Matrix summarizes the model's predictions.

- ✅ Correctly identifies customers who stay.
- ✅ Correctly identifies customers who churn.
- ⚠️ Some churn customers are still classified as retained.
- 🎯 Reducing false negatives is especially important because missing potential churners can lead to lost customers.
""")

    st.divider()

        # ==========================================
    # ROC CURVE
    # ==========================================

    st.markdown("## 📈 ROC Curve")

    left, right = st.columns([1.4,1])

    with left:

        st.image(
            str(figures / "roc_curve_random_forest.png"),
            use_container_width=True
        )

    with right:

        st.info("""
### 💡 Business Insight

The ROC Curve evaluates how well the model distinguishes between churn and non-churn customers.

A curve closer to the top-left corner indicates stronger classification performance.
""")

    st.divider()

    # ==========================================
    # PRECISION RECALL
    # ==========================================

    st.markdown("## 📉 Precision–Recall Curve")

    left, right = st.columns([1.4,1])

    with left:

        st.image(
            str(figures / "precision_recall_curve.png"),
            use_container_width=True
        )

    with right:

        st.info("""
### 💡 Business Insight

The Precision–Recall Curve is especially useful because customer churn is an imbalanced problem.

It shows how well the model balances finding churn customers while avoiding false alarms.
""")

    st.divider()

        # ==========================================
    # MODEL COMPARISON
    # ==========================================

    st.markdown("## 🏆 Model Comparison")

    left, right = st.columns([1.4,1])

    with left:

        st.image(
            str(figures / "model_comparison.png"),
            use_container_width=True
        )

    with right:

        st.info("""
### 💡 Business Insight

Multiple Machine Learning algorithms were evaluated.

Random Forest achieved the best overall balance between accuracy and robustness, making it the preferred model for this application.
""")

    st.divider()

        # ==========================================
    # FINAL CONCLUSION
    # ==========================================

    st.markdown("## 🎯 Overall Model Evaluation")

    st.success("""
### Final Conclusion

The Random Forest model demonstrates strong performance for customer churn prediction.

### Key Findings

- ✅ Successfully distinguishes between churn and retained customers.
- 📈 ROC Curve indicates strong classification capability.
- 🎯 Precision–Recall analysis confirms reliable performance on imbalanced data.
- ⭐ Feature Importance reveals Age, Balance, and Number of Products as major churn indicators.
- 🏆 Among the evaluated algorithms, Random Forest provides the best overall performance.

### Business Value

The model enables banks to:

- Identify customers at high risk of churn.
- Launch targeted retention campaigns.
- Improve customer satisfaction.
- Reduce customer loss.
- Support data-driven business decisions.
""")

    st.divider()

    st.markdown("""
<div style="
background:#1E293B;
padding:20px;
border-radius:15px;
text-align:center;
">

### 🤖 Machine Learning Model Successfully Evaluated

**Random Forest • Scikit-Learn • Streamlit • Python**

</div>
""", unsafe_allow_html=True)