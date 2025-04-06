# pages/skills.py
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Skills', order=1)
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Technical Skills"),
            dbc.ListGroup([
                dbc.ListGroupItem("Python: Pandas, NumPy, AutoARIMA"),
                dbc.ListGroupItem("Data Visualization: Plotly, Matplotlib, Seaborn"),
                dbc.ListGroupItem("Web Development: Dash, Flask, Streamlit, Vue.js, HTML, CSS, JavaScript"),
                dbc.ListGroupItem("Cloud Platforms: Google Cloud Platform (Cloud Run, etc.), Vercel, Render"),
                dbc.ListGroupItem("Databases: SQL, BigQuery, MongoDB"),
                dbc.ListGroupItem("AI & Machine Learning: LLMs on cloud(Gemma3) deployment"),
                dbc.ListGroupItem("Containerization & DevOps: Docker, Git, GitHub"),
            ]),
        ], width=12, className="p-3")
    ])
], className="mt-4")
