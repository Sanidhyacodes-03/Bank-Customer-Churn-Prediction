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

    <h1>📊 Exploratory Data Analysis</h1>

    <p style="font-size:18px;">
    Explore customer behaviour, identify churn patterns,
    and discover valuable business insights using visual analytics.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.info(
        "The charts below provide insights into customer demographics, banking behaviour, and factors influencing customer churn."
    )

    st.divider()

        # ==========================================
    # CUSTOMER OVERVIEW
    # ==========================================

    st.markdown("## 👥 Customer Overview")

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            str(figures / "churn_distribution.png"),
            use_container_width=True
        )

        st.success("""
**Business Insight**

• Most customers remain with the bank.

• A significant percentage still churn, highlighting the importance of customer retention strategies.
""")

    with col2:

        st.image(
            str(figures / "churn_percentage_pie.png"),
            use_container_width=True
        )

        st.success("""
**Business Insight**

• The pie chart clearly shows the proportion of retained and churned customers.

• Although churn is lower than retention, reducing it can significantly improve profitability.
""")

    st.divider()

    # ==========================================
    # CUSTOMER DEMOGRAPHICS
    # ==========================================

    st.markdown("## 🌍 Customer Demographics")

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            str(figures / "gender_distribution.png"),
            use_container_width=True
        )

        st.info("""
**Insight**

Customer distribution across genders is relatively balanced, providing a fair dataset for analysis.
""")

    with col2:

        st.image(
            str(figures / "geography_distribution.png"),
            use_container_width=True
        )

        st.info("""
**Insight**

Customer distribution varies by country, indicating different regional customer bases and market sizes.
""")

    st.divider()

        # ==========================================
    # CUSTOMER & FINANCIAL ANALYSIS
    # ==========================================

    st.markdown("## 📈 Customer & Financial Analysis")

    # -------- Row 1 --------

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            str(figures / "age_distribution.png"),
            use_container_width=True
        )

        st.info("""
**Business Insight**

• Customers are spread across different age groups.

• Age plays an important role in customer churn behaviour.
""")

    with col2:

        st.image(
            str(figures / "credit_score_distribution.png"),
            use_container_width=True
        )

        st.info("""
**Business Insight**

• Most customers have average to good credit scores.

• Credit score alone is not enough to determine churn.
""")

    st.divider()

    # -------- Row 2 --------

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            str(figures / "balance_distribution.png"),
            use_container_width=True
        )

        st.info("""
**Business Insight**

• Customer account balances vary significantly.

• High balances do not necessarily indicate customer loyalty.
""")

    with col2:

        st.image(
            str(figures / "estimated_salary_distribution.png"),
            use_container_width=True
        )

        st.info("""
**Business Insight**

• Salary is widely distributed.

• Customer income shows little direct relationship with churn.
""")

    st.divider()

    # -------- Row 3 --------

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            str(figures / "tenure_distribution.png"),
            use_container_width=True
        )

        st.info("""
**Business Insight**

• Customers have varying lengths of relationship with the bank.

• Long tenure does not always guarantee retention.
""")

    with col2:

        st.image(
            str(figures / "num_of_products_distribution.png"),
            use_container_width=True
        )

        st.info("""
**Business Insight**

• Most customers own one or two banking products.

• Customers with multiple products generally show stronger engagement.
""")

    st.divider()

        # ==========================================
    # CUSTOMER BEHAVIOUR
    # ==========================================

    st.markdown("## 🏦 Customer Behaviour Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            str(figures / "gender_vs_churn.png"),
            use_container_width=True
        )

        st.info("""
### 🚻 Gender vs Churn

Customer churn is fairly similar across genders with only minor differences.
""")

    with col2:

        st.image(
            str(figures / "churn_by_geography.png"),
            use_container_width=True
        )

        st.info("""
### 🌍 Geography vs Churn

Customer churn differs across countries, suggesting regional behaviour impacts retention.
""")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            str(figures / "tenure_vs_churn.png"),
            use_container_width=True
        )

        st.info("""
### ⏳ Tenure vs Churn

Longer customer relationships generally improve retention, although exceptions exist.
""")

    with col2:

        st.image(
            str(figures / "num_of_products_vs_churn.png"),
            use_container_width=True
        )

        st.info("""
### 📦 Products vs Churn

Customers with more banking products are generally less likely to leave the bank.
""")

    st.divider()

    # ==========================================
    # FINAL SUMMARY
    # ==========================================

    st.markdown("## 📋 Overall EDA Summary")

    st.success("""
### Key Findings

- 📊 Most customers remain with the bank, but churn is still significant.
- 👥 Older customers have a higher probability of churn.
- 🌍 Geography has a noticeable impact on customer retention.
- 💳 Credit score and salary alone are weak churn indicators.
- 📦 Customers with more products are generally more loyal.
- 🤖 Multiple customer attributes together improve churn prediction, making Machine Learning an effective solution.
""")