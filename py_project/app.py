import streamlit as st
import pandas as pd

from utils import inject_css
import tab_overview
import tab_performance
import tab_risk

# ==========================================
# 1. Page Configuration & Styling
# ==========================================
st.set_page_config(
    page_title="Global Stock Market Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_css()


# ==========================================
# 2. Load Data
# ==========================================
@st.cache_data
def load_data():
    df = pd.read_excel('data.xlsx')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# ==========================================
# 3. Sidebar (Filters)
# ==========================================
st.sidebar.markdown("## Filters")
st.sidebar.markdown("---")
selected_country = st.sidebar.multiselect("Country", df['Country'].unique(), default=df['Country'].unique())
selected_year = st.sidebar.multiselect("Year", df['Year'].unique(), default=df['Year'].unique())

filtered_df = df[(df['Country'].isin(selected_country)) & (df['Year'].isin(selected_year))]

# ==========================================
# 4. Main Dashboard Header
# ==========================================
st.markdown("""
    <div class="dashboard-header">
        <h1>📊 Global Stock Market Overview Dashboard</h1>
        <p>Explore how trading volume, market returns, and volatility interact to uncover patterns.</p>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 5. Dashboard Tabs — each tab's content lives in its own module
# ==========================================
tab1, tab2, tab3 = st.tabs(["📌  Overview", "📈  Performance", "⚠️  Risk & Volume"])

with tab1:
    tab_overview.render(filtered_df)

with tab2:
    tab_performance.render(filtered_df)

with tab3:
    tab_risk.render(filtered_df)
