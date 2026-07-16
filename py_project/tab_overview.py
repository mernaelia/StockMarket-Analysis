import streamlit as st
import plotly.express as px
from utils import style_fig, PRIMARY


def render(filtered_df):

    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    total_volume = filtered_df['Volume'].sum()
    avg_change = filtered_df['Daily_Change_Percent'].mean()

    index_returns = filtered_df.groupby('Index_Name')['Daily_Return'].mean()
    top_gainer = index_returns.idxmax()
    top_loser = index_returns.idxmin()

    col1.metric("Total Volume", f"{total_volume / 1e9:.2f}B", "Overall Traded")
    col2.metric("Avg Daily Change", f"{avg_change:.2f}%", f"{avg_change:.2f}%")
    col3.metric("Top Gainer", top_gainer, f"{index_returns.max():.2f}%")
    col4.metric("Top Loser", top_loser, f"{index_returns.min():.2f}%", delta_color="inverse")

    st.write("")  # Spacer

    col_map, col_trend = st.columns([1.5, 1])
    with col_map:
        country_data = filtered_df.groupby('Country')['Close'].mean().reset_index()
        fig_map = px.choropleth(
            country_data, locations="Country", locationmode="country names",
            color="Close", hover_name="Country",
            color_continuous_scale="Teal",
        )
        fig_map = style_fig(fig_map, "🌍 Average Market Close by Country", height=420)
        fig_map.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)', lakecolor='#121212'))
        st.plotly_chart(fig_map, use_container_width=True)

    with col_trend:
        trend_data = filtered_df.groupby('Date')['Volume'].sum().reset_index()
        fig_trend = px.area(
            trend_data, x="Date", y="Volume",
            color_discrete_sequence=[PRIMARY]
        )
        fig_trend = style_fig(fig_trend, "📉 Volume Trend Over Time", height=420)
        fig_trend.update_xaxes(showgrid=False)
        fig_trend.update_yaxes(showgrid=True, gridcolor='#242B36')
        fig_trend.update_traces(fillcolor='rgba(0,200,150,0.15)')
        st.plotly_chart(fig_trend, use_container_width=True)
