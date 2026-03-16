# pages/resume.py
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Resume', order=3)

# Resume data
experiences = [
    {
        "company": "Black Piano",
        "role": "Data Analyst",
        "period": "Mar 2026 – Present",
        "location": "Remote",
        "highlights": [
            "Continuing work for the Pi Datametrics client after transition from previous employer.",
            "Maintaining and enhancing data pipelines, dashboards, and analytics reporting."
        ]
    },
    {
        "company": "Pi Software Solutions Pvt Ltd (Pi - Datametrics)",
        "role": "Data Analyst",
        "period": "Mar 2023 – Feb 2026",
        "location": "Remote",
        "highlights": [
            "Developed a Python package for Pi-API and deployed a web service on Render for one-click BigQuery uploads/downloads.",
            "Built AI/LLM reports and end-to-end data pipelines for analytics dashboards.",
            "Automated dashboards using Apps Script, BigQuery, Tableau, and Looker Studio.",
            "Conducted sentiment analysis on election datasets and built predictive models (ARIMA, LSTM).",
            "Created Brand reports & market analysis reports on industries like Insurance, Gambling, and E-commerce (Black Friday, Thanksgiving, Christmas trends, etc.) for the US & UK markets.",
            "Delivered 15+ dashboards and 30+ reports across elections, brands, and market analysis."
        ]
    }
]

projects = [
    {"name": "Fine-Tuned LLM (Mistral-7B, LoRA)", "tech": "Mistral 7b, Hugging Face, LoRA, Python", "desc": "Fine-tuned a quantized Mistral-7B model using QLoRA for philosophical Q&A"},
    {"name": "MolecuLearn AI", "tech": "Vercel, TypeScript, Gemini API", "desc": "Real-time drug alternative tool for general audience"},
    {"name": "AI Debate App", "tech": "Vercel, TypeScript, Gemini API", "desc": "Real-time debate generation platform"},
    {"name": "Terminal Portfolio", "tech": "Vercel, Vue.js", "desc": "Retro-style terminal portfolio"},
]

skills = {
    "Languages & Tools": "Python, SQL, BigQuery, JavaScript, HTML/CSS, Git, Excel",
    "AI & Frameworks": "OpenAI API, Gemini API, Streamlit, NLP, LSTM, ARIMA, Prompt Engineering",
    "Cloud & Deployment": "Google Cloud Run, Vercel, Render, AppScript Automation",
    "Visualization & BI": "Tableau, Looker Studio, Power BI, Plotly, Matplotlib",
    "Other": "ETL Pipelines, Ad-hoc Reporting, Sentiment Analysis, Predictive Analytics"
}

layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col([
            html.H2("Resume"),
            html.P("Data Analyst & AI Developer", className="hero-subtitle", style={'fontSize': '1.1rem', 'marginBottom': '0.5rem'}),
            html.Div([
                html.Span("📍 Hyderabad, India", style={'marginRight': '1.5rem'}),
            ], style={'color': '#a0a0b0', 'marginBottom': '2rem'}),
        ], width=12)
    ]),
    
    # Summary
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("📋 Summary"),
                dbc.CardBody([
                    html.P(
                        "Data Analyst & AI Developer with hands-on experience in LLM fine-tuning, model deployment, "
                        "prompt engineering, and lightweight on-device inference. Skilled in Python, SQL, data engineering, "
                        "and building AI-powered applications with OpenAI, Gemini, HuggingFace, and custom fine-tuned models. "
                        "Passionate about applying AI to real-world products, automation, and intelligent systems."
                    )
                ])
            ])
        ], width=12, className="mb-4")
    ]),
    
    # Experience
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("💼 Experience"),
                dbc.CardBody([
                    html.Div([
                        # Render each experience entry
                        html.Div([
                            html.Div([
                                html.H5(exp["company"], style={'marginBottom': '0.25rem'}),
                                html.Div([
                                    html.Span(exp["role"], style={'fontWeight': '600', 'color': '#667eea'}),
                                    html.Span(f" | {exp['period']} | {exp['location']}", style={'color': '#a0a0b0'})
                                ], style={'marginBottom': '1rem'}),
                                html.Ul([
                                    html.Li(highlight, style={'marginBottom': '0.5rem', 'color': '#c0c0d0'})
                                    for highlight in exp["highlights"]
                                ], style={'paddingLeft': '1.25rem'})
                            ], style={'marginBottom': '2rem'} if i < len(experiences) - 1 else {})
                        ])
                        for i, exp in enumerate(experiences)
                    ])
                ])
            ])
        ], width=12, className="mb-4")
    ]),
    
    # Skills
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("🛠️ Technical Skills"),
                dbc.CardBody([
                    html.Div([
                        html.Div([
                            html.Strong(category + ": ", style={'color': '#667eea'}),
                            html.Span(items, style={'color': '#c0c0d0'})
                        ], style={'marginBottom': '0.75rem'})
                        for category, items in skills.items()
                    ])
                ])
            ])
        ], width=12, className="mb-4")
    ]),
    
    # Portfolio Projects
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("🚀 Portfolio Projects"),
                dbc.CardBody([
                    html.Div([
                        html.Div([
                            html.Strong(project["name"], style={'color': '#fff'}),
                            html.Span(f" | {project['tech']}", style={'color': '#667eea', 'fontSize': '0.9rem'}),
                            html.P(project["desc"], style={'color': '#a0a0b0', 'marginBottom': '0.75rem', 'marginTop': '0.25rem'})
                        ])
                        for project in projects
                    ])
                ])
            ])
        ], width=12, className="mb-4")
    ]),
    
    # Education
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("🎓 Education"),
                dbc.CardBody([
                    html.Div([
                        html.H5("Anurag Group of Institutions", style={'marginBottom': '0.25rem'}),
                        html.P("M. Pharmacy - Pharmaceutical Analysis and Quality Assurance", style={'color': '#a0a0b0', 'marginBottom': '0'}),
                        html.Span("JNTUH | May 2012", style={'color': '#667eea', 'fontSize': '0.9rem'})
                    ])
                ])
            ])
        ], width=12, className="mb-4")
    ]),
    
], className="mt-4")
