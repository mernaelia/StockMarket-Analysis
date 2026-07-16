import streamlit as st
import plotly.express as px
from utils import style_fig


def render(filtered_df):
    """Renders the '⚠️ Risk & Volume' tab. Called from app.py with the filtered dataframe."""

    col_scatter1, col_scatter2 = st.columns(2)

    risk_data = filtered_df.groupby('Index_Name').agg({
        'Volatility': 'mean',
        'Daily_Return': 'mean',
        'Volume': 'sum',
        'Country': 'first'
    }).reset_index()

    with col_scatter1:
        fig_risk = px.scatter(
            risk_data, x="Volatility", y="Daily_Return", size="Volume", color="Index_Name",
            hover_name="Index_Name", text="Index_Name", size_max=50
        )
        fig_risk = style_fig(fig_risk, "⚖️ Risk vs Return", height=440)
        fig_risk.update_traces(textposition='top center')
        fig_risk.add_hline(y=0, line_dash="dash", line_color="#555")
        fig_risk.add_vline(x=risk_data['Volatility'].mean(), line_dash="dash", line_color="#555")
        st.plotly_chart(fig_risk, use_container_width=True)

    with col_scatter2:
        fig_vol = px.scatter(
            risk_data, x="Volume", y="Daily_Return", size="Volatility", color="Index_Name",
            hover_name="Index_Name", text="Index_Name", size_max=50
        )
        fig_vol = style_fig(fig_vol, "🔄 Trading Volume vs Market Performance", height=440)
        fig_vol.update_traces(textposition='top center')
        fig_vol.add_hline(y=0, line_dash="dash", line_color="#555")
        st.plotly_chart(fig_vol, use_container_width=True)
