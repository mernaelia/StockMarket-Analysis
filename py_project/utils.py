import streamlit as st

# ==========================================
# Design tokens (shared across all pages)
# ==========================================
PRIMARY = "#00C896"      # accent teal/green
BG_DARK = "#0E1117"
CARD_BG = "#161B22"
CARD_BORDER = "#242B36"
TEXT_MUTED = "#9AA4B2"

PLOTLY_TEMPLATE = "plotly_dark"
CHART_PAPER_BG = "rgba(0,0,0,0)"
CHART_PLOT_BG = "rgba(0,0,0,0)"


def inject_css():
    """Injects the global CSS design system. Call once, from the main file."""
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
        }}

        .stApp {{
            background: radial-gradient(circle at top left, #131722 0%, {BG_DARK} 55%);
        }}

        section[data-testid="stSidebar"] {{
            background-color: {CARD_BG};
            border-right: 1px solid {CARD_BORDER};
        }}
        section[data-testid="stSidebar"] .stMultiSelect label {{
            color: {TEXT_MUTED};
            font-weight: 600;
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.03em;
        }}

        .dashboard-header {{
            padding: 1.4rem 1.8rem;
            border-radius: 16px;
            background: linear-gradient(135deg, rgba(0,200,150,0.12), rgba(22,27,34,0.4));
            border: 1px solid {CARD_BORDER};
            margin-bottom: 1.2rem;
        }}
        .dashboard-header h1 {{
            margin: 0;
            font-size: 1.9rem;
            font-weight: 800;
            color: #F2F5F7;
        }}
        .dashboard-header p {{
            margin: 0.35rem 0 0 0;
            color: {TEXT_MUTED};
            font-size: 0.95rem;
        }}

        div[data-testid="metric-container"] {{
            background-color: {CARD_BG};
            border: 1px solid {CARD_BORDER};
            padding: 1.1rem 1.3rem;
            border-radius: 14px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.25);
            transition: transform 0.15s ease, border-color 0.15s ease;
        }}
        div[data-testid="metric-container"]:hover {{
            transform: translateY(-2px);
            border-color: {PRIMARY};
        }}
        div[data-testid="metric-container"] label {{
            color: {TEXT_MUTED} !important;
            font-weight: 600;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}
        div[data-testid="metric-container"] div[data-testid="stMetricValue"] {{
            color: #F2F5F7;
            font-weight: 700;
        }}

        button[data-baseweb="tab"] {{
            font-weight: 600;
            font-size: 0.95rem;
            color: {TEXT_MUTED};
        }}
        button[data-baseweb="tab"][aria-selected="true"] {{
            color: {PRIMARY};
        }}
        div[data-baseweb="tab-highlight"] {{
            background-color: {PRIMARY} !important;
        }}

        div[data-testid="stPlotlyChart"] {{
            background-color: {CARD_BG};
            border: 1px solid {CARD_BORDER};
            border-radius: 14px;
            padding: 0.6rem;
            box-shadow: 0 4px 14px rgba(0,0,0,0.2);
        }}

        div[data-baseweb="select"] > div {{
            background-color: {CARD_BG};
            border-color: {CARD_BORDER};
            border-radius: 10px;
        }}

        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        </style>
    """, unsafe_allow_html=True)


def style_fig(fig, title=None, height=None):
    """Apply a consistent, clean look to any Plotly figure. Used by every tab module."""
    fig.update_layout(
        template=PLOTLY_TEMPLATE,
        paper_bgcolor=CHART_PAPER_BG,
        plot_bgcolor=CHART_PLOT_BG,
        font=dict(family="Inter, sans-serif", color="#E6E9EC", size=13),
        title=dict(text=title, font=dict(size=16, family="Inter, sans-serif", color="#F2F5F7")) if title else fig.layout.title,
        margin=dict(l=10, r=10, t=50, b=10),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        colorway=[PRIMARY, "#4C9AFF", "#FFAB4C", "#FF6B6B", "#B084F5", "#4CD9C0"],
    )
    if height:
        fig.update_layout(height=height)
    return fig
