import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def show(model):

    # ==========================================
    # PAGE HEADER
    # ==========================================

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#4F46E5,#7C3AED);
    padding:30px;
    border-radius:20px;
    color:white;
    margin-bottom:25px;
    box-shadow:0px 12px 25px rgba(0,0,0,.25);
    ">

    <h1>🔮 Customer Churn Prediction</h1>

    <p style="font-size:18px;">
    Predict whether a customer is likely to churn using our
    <b>Random Forest Machine Learning Model.</b>
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.info(
        "Fill in the customer information below and click Predict."
    )

    st.divider()

    st.markdown("## 👤 Customer Information")

    left, right = st.columns(2)

    # ==========================================
    # LEFT COLUMN
    # ==========================================

    with left:

        st.markdown("### 💳 Financial Details")

        credit_score = st.slider(
            "Credit Score",
            300,
            900,
            650
        )

        balance = st.number_input(
            "Account Balance",
            min_value=0.0,
            value=50000.0
        )

        estimated_salary = st.number_input(
            "Estimated Salary",
            min_value=0.0,
            value=50000.0
        )

        tenure = st.slider(
            "Tenure",
            0,
            10,
            5
        )

        num_products = st.selectbox(
            "Number of Products",
            [1,2,3,4]
        )

    # ==========================================
    # RIGHT COLUMN
    # ==========================================

    with right:

        st.markdown("### 👥 Personal Details")

        age = st.slider(
            "Age",
            18,
            100,
            35
        )

        geography = st.selectbox(
            "Geography",
            [
                "France",
                "Germany",
                "Spain"
            ]
        )

        gender = st.radio(
            "Gender",
            [
                "Female",
                "Male"
            ],
            horizontal=True
        )

        has_card = st.radio(
            "Credit Card",
            [
                "Yes",
                "No"
            ],
            horizontal=True
        )

        active_member = st.radio(
            "Active Member",
            [
                "Yes",
                "No"
            ],
            horizontal=True
        )

    st.divider()

    predict = st.button(
        "🚀 Predict Customer Churn",
        use_container_width=True
    )
        # ==========================================
    # PREDICTION
    # ==========================================

    if predict:

        with st.spinner("🔍 Analyzing customer data..."):

            # Save original values for display
            selected_geography = geography
            selected_gender = gender

            # Encode categorical variables
            geography = {
                "France": 0,
                "Germany": 1,
                "Spain": 2
            }[geography]

            gender = {
                "Female": 0,
                "Male": 1
            }[gender]

            has_card = 1 if has_card == "Yes" else 0
            active_member = 1 if active_member == "Yes" else 0

            # Create dataframe
            input_data = pd.DataFrame({
                "CreditScore": [credit_score],
                "Geography": [geography],
                "Gender": [gender],
                "Age": [age],
                "Tenure": [tenure],
                "Balance": [balance],
                "NumOfProducts": [num_products],
                "HasCrCard": [has_card],
                "IsActiveMember": [active_member],
                "EstimatedSalary": [estimated_salary]
            })

            # Model prediction
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]

        # ==========================================
        # RESULT
        # ==========================================

        st.divider()

        st.markdown("## 🎯 Prediction Result")

        if prediction == 1:
            st.error("🚨 Customer is likely to CHURN")
        else:
            st.success("✅ Customer is likely to STAY")

        # Risk level
        if probability < 0.30:
            risk = "🟢 Low Risk"
            gauge_color = "#22C55E"

        elif probability < 0.70:
            risk = "🟠 Medium Risk"
            gauge_color = "#F59E0B"

        else:
            risk = "🔴 High Risk"
            gauge_color = "#EF4444"

            st.divider()

        left_col, right_col = st.columns([1.2, 1])

        # ==========================================
        # CHURN PROBABILITY GAUGE
        # ==========================================

        with left_col:

            st.markdown("### 📊 Churn Probability")

            fig = go.Figure(go.Indicator(

                mode="gauge+number",

                value=probability * 100,

                number={
                    "suffix": "%",
                    "font": {"size": 40}
                },

                title={
                    "text": "Probability"
                },

                gauge={

                    "axis": {
                        "range": [0, 100]
                    },

                    "bar": {
                        "color": gauge_color
                    },

                    "steps": [

                        {
                            "range": [0, 30],
                            "color": "#22C55E"
                        },

                        {
                            "range": [30, 70],
                            "color": "#F59E0B"
                        },

                        {
                            "range": [70, 100],
                            "color": "#EF4444"
                        }

                    ]

                }

            ))

            fig.update_layout(

                height=380,

                margin=dict(
                    l=20,
                    r=20,
                    t=60,
                    b=20
                ),

                paper_bgcolor="rgba(0,0,0,0)",

                font=dict(size=18)

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.markdown(
                f"### Risk Level: **:{'green' if probability < 0.30 else 'orange' if probability < 0.70 else 'red'}[{risk}]**"
            )

        # ==========================================
        # CUSTOMER SUMMARY
        # ==========================================

        with right_col:

            st.markdown("### 👤 Customer Summary")

            st.info(f"""
**Age:** {age}

**Credit Score:** {credit_score}

**Balance:** ₹{balance:,.0f}

**Products:** {num_products}

**Geography:** {selected_geography}

**Gender:** {selected_gender}

**Tenure:** {tenure} Years

**Estimated Salary:** ₹{estimated_salary:,.0f}

**Credit Card:** {"Yes" if has_card else "No"}

**Active Member:** {"Yes" if active_member else "No"}
""")
        st.divider()

        # ==========================================
        # BUSINESS RECOMMENDATIONS
        # ==========================================

        st.markdown("## 💡 Business Recommendations")

        if probability >= 0.70:

            st.error("""
### 🔴 High Churn Risk

The customer has a **high probability of churn**.

**Recommended Actions**
- 🎁 Offer cashback or personalized discounts.
- 👨‍💼 Assign a dedicated relationship manager.
- 📞 Contact the customer proactively.
- ⭐ Launch a loyalty rewards campaign.
- 💳 Recommend premium banking services.
""")

        elif probability >= 0.30:

            st.warning("""
### 🟠 Medium Churn Risk

The customer has a **moderate churn risk**.

**Recommended Actions**
- 📧 Send personalized email campaigns.
- 💰 Recommend suitable banking products.
- 🎯 Provide reward points.
- 😊 Improve customer engagement.
""")

        else:

            st.success("""
### 🟢 Low Churn Risk

The customer is likely to remain with the bank.

**Recommended Actions**
- ❤️ Maintain service quality.
- 🎉 Reward customer loyalty.
- 💳 Cross-sell banking products.
- 🌟 Continue customer engagement.
""")

        st.divider()

        # ==========================================
        # MODEL SUMMARY
        # ==========================================

        st.markdown("## 🤖 Prediction Summary")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Prediction",
                "CHURN" if prediction == 1 else "STAY"
            )

        with c2:
            st.metric(
                "Probability",
                f"{probability*100:.2f}%"
            )

        with c3:
            st.metric(
                "Risk",
                risk
            )

        st.divider()

        # ==========================================
        # CUSTOMER SNAPSHOT
        # ==========================================

        st.markdown("## 📋 Customer Snapshot")

        snapshot = pd.DataFrame({

            "Feature":[
                "Credit Score",
                "Age",
                "Balance",
                "Products",
                "Geography",
                "Gender",
                "Tenure",
                "Estimated Salary",
                "Credit Card",
                "Active Member"
            ],

            "Value":[
                credit_score,
                age,
                f"₹{balance:,.0f}",
                num_products,
                selected_geography,
                selected_gender,
                f"{tenure} Years",
                f"₹{estimated_salary:,.0f}",
                "Yes" if has_card else "No",
                "Yes" if active_member else "No"
            ]

        })

        st.dataframe(
            snapshot,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "📄 Download Prediction Report",
            snapshot.to_csv(index=False),
            file_name="Prediction_Report.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.divider()

        st.success("✅ Prediction completed successfully!")