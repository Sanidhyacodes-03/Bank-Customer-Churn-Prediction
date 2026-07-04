import streamlit as st


def show(df, BASE_DIR):

    total_customers = len(df)
    churned = int(df["Exited"].sum())
    retained = total_customers - churned
    churn_rate = (churned / total_customers) * 100
    avg_balance = df["Balance"].mean()
    avg_age = df["Age"].mean()

    # ============================
    # HERO
    # ============================

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#4F46E5,#7C3AED);
    padding:35px;
    border-radius:20px;
    color:white;
    margin-bottom:25px;
    box-shadow:0 15px 40px rgba(0,0,0,.35);
    ">

    <h1 style="margin-bottom:5px;">
    🏦 Bank Customer Churn Prediction Dashboard
    </h1>

    <p style="font-size:18px;">
    AI-Powered Customer Retention Dashboard
    </p>

    <p>
    Analyze customer behaviour, identify churn risks,
    and make smarter business decisions using a
    <b>Random Forest Machine Learning Model.</b>
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ============================
    # KPI CARDS
    # ============================

    c1,c2,c3,c4 = st.columns(4)

    with c1:

        st.markdown(f"""
        <div style="
        background:#1E293B;
        padding:25px;
        border-radius:18px;
        text-align:center;
        border:1px solid rgba(255,255,255,.08);
        ">

        <h4>👥 Customers</h4>

        <h2>{total_customers:,}</h2>

        </div>
        """,unsafe_allow_html=True)

    with c2:

        st.markdown(f"""
        <div style="
        background:#1E293B;
        padding:25px;
        border-radius:18px;
        text-align:center;
        border:1px solid rgba(255,255,255,.08);
        ">

        <h4>📉 Churn Rate</h4>

        <h2>{churn_rate:.2f}%</h2>

        </div>
        """,unsafe_allow_html=True)

    with c3:

        st.markdown(f"""
        <div style="
        background:#1E293B;
        padding:25px;
        border-radius:18px;
        text-align:center;
        border:1px solid rgba(255,255,255,.08);
        ">

        <h4>💰 Avg Balance</h4>

        <h2>₹{avg_balance:,.0f}</h2>

        </div>
        """,unsafe_allow_html=True)

    with c4:

        st.markdown("""
        <div style="
        background:#1E293B;
        padding:25px;
        border-radius:18px;
        text-align:center;
        border:1px solid rgba(255,255,255,.08);
        ">

        <h4>🤖 Model</h4>

        <h2>Random Forest</h2>

        </div>
        """,unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    # ============================
    # QUICK INSIGHTS
    # ============================

    left,right = st.columns([2,1])

    with left:

        st.markdown("""
        ### 📈 Business Summary

        This dashboard helps banks identify customers
        likely to churn using Machine Learning.

        Use the Prediction page to estimate churn risk,
        analyze customer behaviour in EDA,
        and evaluate model performance using ROC Curve,
        Precision-Recall Curve and Feature Importance.
        """)

    with right:

        st.info(f"""
### Dataset

👥 Customers : {total_customers:,}

📉 Churned : {churned}

✅ Retained : {retained}

🎯 Average Age : {avg_age:.1f}
""")

    st.divider()

    st.subheader("📊 Customer Insights")

    # ==================================================
    # CHARTS
    # ==================================================

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📉 Customer Churn Distribution")
        st.write("Shows the number of customers who stayed and churned.")

        st.image(
            str(BASE_DIR / "outputs" / "figures" / "churn_distribution.png"),
            use_container_width=True
        )

    with col2:
        st.markdown("### 🌍 Churn by Geography")
        st.write("Shows churn distribution across different regions.")

        st.image(
            str(BASE_DIR / "outputs" / "figures" / "churn_by_geography.png"),
            use_container_width=True
        )

    st.divider()

    # ==================================================
    # SECOND ROW
    # ==================================================

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👥 Age vs Churn")

        st.image(
            str(BASE_DIR / "outputs" / "figures" / "age_distribution_by_churn.png"),
            use_container_width=True
        )

    with col2:
        st.markdown("### 🚻 Gender vs Churn")

        st.image(
            str(BASE_DIR / "outputs" / "figures" / "gender_vs_churn.png"),
            use_container_width=True
        )

    st.divider()

    # ==================================================
    # HEATMAP
    # ==================================================

    st.markdown("## 🔥 Feature Correlation")

    st.image(
        str(BASE_DIR / "outputs" / "figures" / "correlation_heatmap.png"),
        use_container_width=True
    )

    st.divider()

    # ==================================================
    # BUSINESS INSIGHTS
    # ==================================================

    st.markdown("## 💡 Business Insights")

    left, right = st.columns(2)

    with left:

        st.success("""
**Customer Retention**

• Majority of customers stay with the bank.

• Active members are more loyal.

• Customers with multiple products churn less.
""")

    with right:

        st.warning("""
**Churn Risk**

• Older customers are more likely to churn.

• Geography has a noticeable impact.

• Balance alone does not guarantee retention.
""")

    st.divider()
