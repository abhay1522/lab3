"""
Eco-Green Botanical Chemistry Theme for Streamlit.
Natural forest green, sage, warm earthy background, soft rounded glass cards.
Call apply_eco_green_theme() once, near the top of app.py.
"""

import streamlit as st

ECO_GREEN_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap');

/* ---------- Global Page Styling ---------- */
.stApp {
    background-color: #0f1c15;
    background-image:
        radial-gradient(at 10% 20%, rgba(46, 117, 89, 0.15) 0px, transparent 50%),
        radial-gradient(at 90% 80%, rgba(26, 77, 46, 0.2) 0px, transparent 50%),
        linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 32px 32px, 32px 32px;
}

/* ---------- Top Navbar Glow ---------- */
[data-testid="stHeader"] {
    background: rgba(15, 28, 21, 0.75);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(74, 159, 112, 0.2);
}

/* ---------- Main Content Container: Soft Eco Glass Panel ---------- */
.block-container {
    background: rgba(21, 38, 29, 0.75);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(74, 159, 112, 0.25);
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.45);
    padding: 2.5rem 3rem !important;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
}

/* ---------- Typography ---------- */
.stApp p, .stApp label, .stApp li, .stApp input, .stApp textarea,
.stApp [data-testid="stMarkdownContainer"], .stApp [data-testid="stCaptionContainer"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: #e2ece9;
    font-size: 1rem;
}

h1, h2, h3, h4, .main-title, .section-title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}

h1, .main-title {
    background: linear-gradient(135deg, #a3e635 0%, #4ade80 50%, #10b981 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.3rem !important;
    text-shadow: 0 0 30px rgba(74, 222, 128, 0.25);
}

h2 {
    color: #4ade80 !important;
    font-size: 1.55rem !important;
    border-bottom: 1px solid rgba(74, 222, 128, 0.2);
    padding-bottom: 8px;
}

h3 {
    color: #86efac !important;
    font-size: 1.25rem !important;
}

h4 {
    color: #bef264 !important;
    font-size: 1.05rem !important;
}

.mc-subtitle {
    text-align: center;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 1.3rem;
    color: #a3e635;
    font-weight: 500;
}

code, pre, .stApp code {
    font-family: 'Fira Code', monospace !important;
    background: rgba(11, 22, 16, 0.85) !important;
    border: 1px solid rgba(74, 222, 128, 0.25) !important;
    border-radius: 8px;
    color: #86efac !important;
}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] {
    background-color: rgba(12, 23, 17, 0.9);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(74, 159, 112, 0.2);
}

/* ---------- Custom Botanical Buttons ---------- */
.stButton > button, .stDownloadButton > button, [data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #2e7d32 0%, #1b5e20 100%);
    color: #ffffff !important;
    border: 1px solid rgba(134, 239, 172, 0.4);
    border-radius: 10px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 600;
    padding: 0.6rem 1.4rem;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 14px rgba(27, 94, 32, 0.35);
}

.stButton > button:hover, .stDownloadButton > button:hover {
    background: linear-gradient(135deg, #388e3c 0%, #2e7d32 100%);
    border-color: #4ade80;
    box-shadow: 0 0 20px rgba(74, 222, 128, 0.4);
    transform: translateY(-2px);
}

.stButton > button p, .stDownloadButton > button p {
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* ---------- Inputs & Controls ---------- */
.stTextInput input, .stTextArea textarea, .stNumberInput input {
    background: rgba(11, 22, 16, 0.75) !important;
    color: #f0fdf4 !important;
    border: 1px solid rgba(74, 159, 112, 0.3) !important;
    border-radius: 10px !important;
    backdrop-filter: blur(6px);
}

.stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus {
    border-color: #4ade80 !important;
    box-shadow: 0 0 12px rgba(74, 222, 128, 0.3) !important;
}

[data-baseweb="select"] > div {
    background: rgba(11, 22, 16, 0.75) !important;
    border: 1px solid rgba(74, 159, 112, 0.3) !important;
    border-radius: 10px !important;
}

/* ---------- Metrics Cards ---------- */
[data-testid="stMetric"] {
    background: rgba(22, 45, 33, 0.65);
    border: 1px solid rgba(74, 222, 128, 0.25);
    border-radius: 14px;
    padding: 16px 20px;
    backdrop-filter: blur(8px);
}

[data-testid="stMetricLabel"] {
    color: #a7f3d0 !important;
    font-size: 0.85rem !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

[data-testid="stMetricValue"] {
    color: #4ade80 !important;
    font-family: 'Fira Code', monospace !important;
    font-size: 1.5rem !important;
}

/* ---------- Alerts ---------- */
[data-testid="stAlert"] {
    border-radius: 10px !important;
    border: 1px solid rgba(74, 222, 128, 0.3) !important;
    background-color: rgba(16, 37, 26, 0.85) !important;
}

/* ---------- Tables & Misc ---------- */
[data-testid="stDataFrame"] {
    border: 1px solid rgba(74, 159, 112, 0.3);
    border-radius: 10px;
    overflow: hidden;
}

hr {
    border: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(74, 222, 128, 0.4), transparent);
    margin: 1.8rem 0;
}

[data-baseweb="tab"] {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600;
}
</style>
"""


def apply_eco_green_theme():
    """Inject the Eco-Green Botanical CSS into the page."""
    st.markdown(ECO_GREEN_CSS, unsafe_allow_html=True)
