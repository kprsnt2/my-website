# pages/projects.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Projects', order=2)

# Project data - organized by category
projects = [
    # Featured Projects
    {
        "title": "MyLocalCLI - AI Coding Assistant",
        "description": "A Claude Code alternative with 6 AI providers, 26 tools, 5 agents, and 22 skills. Works with local LLMs and free cloud APIs. Private, local, yours.",
        "url": "https://mlc.kprsnt.in",
        "color": "success",
        "featured": True,
        "tags": ["Node.js", "CLI", "AI", "LLM"]
    },
    {
        "title": "AI Health Pro - Health Advisor",
        "description": "AI-powered health advisor providing symptom analysis, drug recommendations, and personalized health insights with user profiles.",
        "url": "https://aihealth-pro.vercel.app",
        "color": "danger",
        "featured": True,
        "tags": ["React", "AI", "Healthcare", "Vercel"]
    },
    {
        "title": "PharmGenesisAI - Drug Discovery",
        "description": "AI-powered drug discovery tool for Pharma R&D. Accelerate research with intelligent compound analysis.",
        "url": "https://pharmgenai.kprsnt.in/",
        "github": "https://github.com/kprsnt2/PharmaGenesisAI",
        "color": "danger",
        "featured": True,
        "tags": ["Pharma", "R&D", "AI", "Drug Discovery"]
    },
    
    # AI & Chat Projects
    {
        "title": "PersonaAI - Multi-Personality Chat",
        "description": "Chat with 3 different AI personalities: Teen, Child, and Infant. Each has unique response characteristics.",
        "url": "https://per-ai.vercel.app/",
        "github": "https://github.com/kprsnt2/PersonaAI",
        "color": "info",
        "featured": False,
        "tags": ["React", "AI", "Personalities", "Vercel"]
    },
    {
        "title": "AI Debate Platform",
        "description": "Real-time AI debate generation and discussion platform. Vibe-coded on mobile using Firebase Studio.",
        "url": "https://aidebate.kprsnt.in",
        "color": "info",
        "featured": False,
        "tags": ["Firebase", "AI", "Mobile"]
    },
    {
        "title": "Local AI/LLM Chatbot",
        "description": "AI chatbot powered by Gemma3 model, hosted via Ollama and Open WebUI on Google Cloud Run. (Discontinued)",
        "url": "https://chat.kprsnt.in",
        "color": "secondary",
        "featured": False,
        "tags": ["Ollama", "GCP", "Gemma3", "Discontinued"]
    },
    
    # Learning & Education
    {
        "title": "ChessKids - Interactive Chess",
        "description": "Interactive kids chess learning game with toy icons like car/bus. Learn chess with AI assistance!",
        "url": "https://chess.kprsnt.in/",
        "github": "https://github.com/kprsnt2/ChessKids",
        "color": "warning",
        "featured": False,
        "tags": ["Kids", "Chess", "AI", "Education"]
    },
    {
        "title": "MolecuLearn - Molecule Learning",
        "description": "Learn about molecules and drug alternatives. Real-time drug alternative tool for general audience.",
        "url": "https://moleculearn.kprsnt.in",
        "github": "https://github.com/kprsnt2/MolecuLearn",
        "color": "info",
        "featured": False,
        "tags": ["Education", "Chemistry", "Gemini API"]
    },
    {
        "title": "Phonics App - Kids Learning",
        "description": "Kids phonics learning application. Interactive way to learn letter sounds and pronunciation.",
        "url": "https://phonics.kprsnt.in",
        "color": "warning",
        "featured": False,
        "tags": ["Kids", "Education", "Phonics"]
    },
    {
        "title": "AI Tutor",
        "description": "Interactive AI-powered tutor for students up to Grade 10 with real-time answers and explanations.",
        "url": "https://aitutor.streamlit.app/",
        "color": "info",
        "featured": False,
        "tags": ["Streamlit", "Education", "AI"]
    },
    {
        "title": "AI Story Teller",
        "description": "Generates creative short stories for kids using Gemini API with text and audio output.",
        "url": "https://storygemini.streamlit.app",
        "color": "info",
        "featured": False,
        "tags": ["Streamlit", "LLM", "Creative", "Kids"]
    },
    
    # Data & Dashboards
    {
        "title": "Brand Dashboards",
        "description": "Brand analytics dashboards with market analysis and SEO insights. Built for business intelligence.",
        "url": "https://dashboard.kprsnt.in",
        "github": "https://github.com/kprsnt2/dashboard_site",
        "color": "info",
        "featured": False,
        "tags": ["Dashboard", "Analytics", "BI"]
    },
    {
        "title": "CSV Data Plotter",
        "description": "Upload CSV files and explore interactive visualizations. Supports various chart types.",
        "url": "https://plotcharts.streamlit.app",
        "color": "info",
        "featured": False,
        "tags": ["Streamlit", "Data Viz", "Python"]
    },
    
    # Portfolio Sites
    {
        "title": "Terminal Website Interface",
        "description": "Retro-style terminal interface with Vue.js. A hacker-themed shell that's fully responsive.",
        "url": "https://terminal.kprsnt.in",
        "color": "info",
        "featured": False,
        "tags": ["Vue.js", "UI/UX", "Terminal"]
    },
    {
        "title": "Next.js Developer Site",
        "description": "Modern personal website using Next.js with UI concepts from v0.dev. Deployed on Vercel.",
        "url": "https://vercel.kprsnt.in",
        "color": "info",
        "featured": False,
        "tags": ["Next.js", "Vercel", "v0.dev"]
    },
]

def create_project_card(project):
    """Create a project card with optional featured badge, tags, and GitHub link."""
    
    # Buttons row
    buttons = [
        dbc.Button("Visit Site →", href=project["url"], target="_blank", color=project["color"], className="me-2")
    ]
    if project.get("github"):
        buttons.append(
            dbc.Button("GitHub", href=project["github"], target="_blank", color="dark", outline=True)
        )
    
    card_content = [
        dbc.CardHeader([
            project["title"],
            html.Span("⭐ Featured", className="featured-badge") if project.get("featured") else None
        ], style={"position": "relative"}),
        dbc.CardBody([
            html.P(project["description"]),
            html.Div([
                html.Span(tag, style={
                    'display': 'inline-block',
                    'background': 'rgba(102, 126, 234, 0.2)',
                    'color': '#667eea',
                    'padding': '0.2rem 0.6rem',
                    'borderRadius': '12px',
                    'fontSize': '0.75rem',
                    'marginRight': '0.5rem',
                    'marginBottom': '0.5rem',
                })
                for tag in project.get("tags", [])
            ], style={'marginBottom': '1rem'}),
            html.Div(buttons),
        ])
    ]
    
    return dbc.Col(
        dbc.Card(card_content, className="shadow-sm h-100"),
        width=12, md=6, lg=4, className="mb-4"
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("My Projects"),
            html.P(
                "A collection of web applications, AI tools, dashboards, and educational apps I've built.",
                className="mb-4"
            ),
        ], width=12),
    ]),
    dbc.Row([
        create_project_card(project) for project in projects
    ], className="mt-3"),
])
