# pages/skills.py
import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Skills', order=1)

# Skill categories with badges
skills_data = {
    "Languages": [
        ("Python", "python"),
        ("JavaScript", "js"),
        ("TypeScript", "js"),
        ("SQL", "python"),
        ("HTML/CSS", "js"),
    ],
    "Frameworks & Libraries": [
        ("React", "js"),
        ("Next.js", "js"),
        ("Vue.js", "js"),
        ("Dash", "python"),
        ("Flask", "python"),
        ("Streamlit", "python"),
        ("Node.js", "js"),
    ],
    "Cloud & DevOps": [
        ("Google Cloud", "cloud"),
        ("Vercel", "cloud"),
        ("Render", "cloud"),
        ("Docker", "cloud"),
        ("Git/GitHub", "cloud"),
    ],
    "AI & Data": [
        ("LLMs (Gemma, Ollama)", "ai"),
        ("OpenRouter", "ai"),
        ("Pandas", "python"),
        ("NumPy", "python"),
        ("Plotly", "python"),
        ("BigQuery", "ai"),
        ("MongoDB", "ai"),
    ],
}

def create_skill_section(title, skills):
    return dbc.Card([
        dbc.CardHeader(title),
        dbc.CardBody([
            html.Div([
                html.Span(skill[0], className=f"skill-badge {skill[1]}")
                for skill in skills
            ])
        ])
    ], className="mb-4")

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Technical Skills"),
            html.P(
                "A diverse toolkit spanning full-stack development, cloud infrastructure, and AI/ML.",
                className="mb-4"
            ),
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            create_skill_section("💻 Languages", skills_data["Languages"]),
        ], width=12, md=6),
        dbc.Col([
            create_skill_section("⚡ Frameworks & Libraries", skills_data["Frameworks & Libraries"]),
        ], width=12, md=6),
    ]),
    dbc.Row([
        dbc.Col([
            create_skill_section("☁️ Cloud & DevOps", skills_data["Cloud & DevOps"]),
        ], width=12, md=6),
        dbc.Col([
            create_skill_section("🤖 AI & Data", skills_data["AI & Data"]),
        ], width=12, md=6),
    ]),
], className="mt-4")
