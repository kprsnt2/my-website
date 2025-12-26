# pages/about.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# Register this page with Dash
dash.register_page(__name__, path='/', name='About Me', order=0)

# Page layout with Hero Section
layout = dbc.Container([
    # Hero Section
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H1("Prashanth Kumar Kadasi", className="hero-title"),
                html.P(
                    "Data Analyst • AI Developer • Data Engineering",
                    className="hero-subtitle"
                ),
                html.P(
                    "I build intelligent applications that solve real-world problems. "
                    "From AI-powered health advisors to local CLI tools, I love turning ideas into reality.",
                    style={'fontSize': '1.1rem', 'maxWidth': '600px', 'margin': '0 auto 2rem'}
                ),
                # Social Links
                html.Div([
                    html.A([
                        html.I(className="fab fa-github"),
                        " GitHub"
                    ], href="https://github.com/kprsnt2", target="_blank", className="social-btn"),
                    html.A([
                        html.I(className="fab fa-linkedin"),
                        " LinkedIn"
                    ], href="https://www.linkedin.com/in/prashanth-kumar-kadasi-b5281765/", target="_blank", className="social-btn"),
                    html.A([
                        html.I(className="fab fa-x-twitter"),
                        " 𝕏"
                    ], href="https://x.com/prashanth_29", target="_blank", className="social-btn"),
                    html.A([
                        html.I(className="fas fa-envelope"),
                        " Email"
                    ], href="mailto:kprsnt@gmail.com", className="social-btn"),
                ], style={'marginBottom': '2rem'}),
            ], className="hero-section")
        ], width=12)
    ]),
    
    # About Cards
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("🚀 What I Do"),
                dbc.CardBody([
                    html.P(
                        "I specialize in building AI-powered applications, data visualizations, "
                        "and web platforms. Whether it's deploying LLMs locally or creating "
                        "interactive dashboards, I enjoy every step of the development process."
                    )
                ])
            ])
        ], width=12, md=6, className="mb-4"),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("🛠️ Tech Stack"),
                dbc.CardBody([
                    html.P(
                        "Python • JavaScript • React • Next.js • Node.js • "
                        "Dash • Flask • Docker • GCP • Vercel • MongoDB • "
                        "LLMs (Gemma, Ollama, OpenRouter)"
                    )
                ])
            ])
        ], width=12, md=6, className="mb-4"),
    ]),
    
    # Featured Projects Preview
    dbc.Row([
        dbc.Col([
            html.H3("Featured Projects", style={'marginTop': '2rem', 'marginBottom': '1.5rem'}),
        ], width=12),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("⚡ MyLocalCLI"),
                dbc.CardBody([
                    html.P("A Claude Code alternative with 6 providers, 26 tools, and full privacy."),
                    dbc.Button("Explore →", href="/projects", color="info", size="sm")
                ])
            ])
        ], width=12, md=4, className="mb-4"),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("🩺 AI Health Pro"),
                dbc.CardBody([
                    html.P("AI-powered health advisor with symptom analysis and drug recommendations."),
                    dbc.Button("Explore →", href="/projects", color="info", size="sm")
                ])
            ])
        ], width=12, md=4, className="mb-4"),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("💬 Local AI Chat"),
                dbc.CardBody([
                    html.P("Self-hosted LLM chatbot running on Google Cloud with Ollama."),
                    dbc.Button("Explore →", href="/projects", color="info", size="sm")
                ])
            ])
        ], width=12, md=4, className="mb-4"),
    ]),
    
], className="mt-4", fluid=True)
