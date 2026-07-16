import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils import style_fig


def render(filtered_df):
    """Renders the '📈 Performance' tab. Called from app.py with the filtered dataframe."""

    col_tree, col_candle = st.columns([1, 1])

    with col_tree:
        tree_data = filtered_df.groupby(['Country', 'Index_Name'])['Volume'].sum().reset_index()
        fig_tree = px.treemap(
            tree_data, path=[px.Constant("Global Markets"), 'Country', 'Index_Name'], values='Volume',
            color='Volume', color_continuous_scale='Teal'
        )
        fig_tree = style_fig(fig_tree, "🟩 Volume by Country & Index", height=440)
        st.plotly_chart(fig_tree, use_container_width=True)

    with col_candle:
        selected_index = st.selectbox("Select Index for OHLC Movement:", filtered_df['Index_Name'].unique())
        index_df = filtered_df[filtered_df['Index_Name'] == selected_index].sort_values('Date')

        if len(index_df) > 100:
            index_df = index_df.tail(100)

        fig_candle = go.Figure(data=[go.Candlestick(
            x=index_df['Date'],
            open=index_df['Open'], high=index_df['High'],
            low=index_df['Low'], close=index_df['Close'],
            increasing_line_color='#00C896', decreasing_line_color='#FF5C5C'
        )])
        fig_candle = style_fig(fig_candle, f"🕯️ OHLC Price Movement — {selected_index} (Last 100 Days)", height=440)
        fig_candle.update_layout(xaxis_rangeslider_visible=False)
        st.plotly_chart(fig_candle, use_container_width=True)

    st.write("")
    return_data = filtered_df.groupby('Country')['Daily_Return'].mean().reset_index().sort_values('Daily_Return')
    fig_bar = px.bar(
        return_data, x='Country', y='Daily_Return',
        color='Daily_Return', color_continuous_scale='RdYlGn'
    )
    fig_bar = style_fig(fig_bar, "📊 Average Daily Return (%) by Country", height=380)
    fig_bar.add_hline(y=0, line_width=2, line_dash="solid", line_color="#E6E9EC")
    st.plotly_chart(fig_bar, use_container_width=True)
