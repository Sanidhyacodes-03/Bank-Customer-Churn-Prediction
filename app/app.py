import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


from views import dashboard
from views import prediction
from views import eda
from views import model_performance
from views import about

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Bank Customer Churn Prediction Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "processed_bank.csv"
MODEL_PATH = BASE_DIR / "models" / "random_forest_model.pkl"

# --------------------------------------------------
# LOAD CSS
# --------------------------------------------------

CSS_PATH = Path(__file__).parent / "styles.css"

if CSS_PATH.exists():
    with open(CSS_PATH) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

df = load_data()
model = load_model()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------


st.sidebar.markdown(
    """
    <h2 style='text-align:center;'>
    🏦 Churn Dashboard
    </h2>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🔮 Prediction",
        "📊 EDA",
        "📈 Model Performance",
        "ℹ️ About"
    ]
)

st.sidebar.markdown("---")



# --------------------------------------------------
# ROUTING
# --------------------------------------------------

if page == "🏠 Dashboard":
    dashboard.show(df, BASE_DIR)

elif page == "🔮 Prediction":
    prediction.show(model)

elif page == "📊 EDA":
    eda.show(BASE_DIR)

elif page == "📈 Model Performance":
    model_performance.show(BASE_DIR)

elif page == "ℹ️ About":
    about.show()