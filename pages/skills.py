# pages/skills.py
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Skills', order=1)

layout = dbc.Container([
    dbc.Row([
        # Add padding to the column content
        dbc.Col([
            html.H2("Technical Skills"),
            html.Ul([
                html.Li("Python (Pandas, NumPy, Scikit-learn, TensorFlow/PyTorch)"),
                html.Li("Data Visualization (Plotly, Matplotlib, Seaborn)"),
                html.Li("Web Frameworks (Dash, Flask, Streamlit)"),
                html.Li("Frontend (Vue.js, HTML, CSS, JavaScript) - Mentioned from previous context"),
                html.Li("Cloud Platforms (Google Cloud Platform - Cloud Run, etc.)"),
                html.Li("Databases (SQL, NoSQL - specify if applicable)"),
                html.Li("AI/ML (LLMs - Gemma3, Ollama, Model Deployment)"),
                html.Li("Containerization (Docker)"),
                html.Li("Version Control (Git, GitHub/GitLab)"),
                # Add more skills
            ]),
            # You could also use dbc.ListGroup for styling
        ], width=12, className="p-3") # p-3 adds padding on all sides
    ])
], className="mt-4") # mt-4 adds margin top to the container for this page