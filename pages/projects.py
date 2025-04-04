# pages/projects.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Projects', order=2)

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("My Projects"), width=12),
    ]),
    dbc.Row([
        # Project 1: Terminal Website
        dbc.Col(dbc.Card([
            dbc.CardHeader("Terminal Website Interface"),
            dbc.CardBody([
                html.P("A retro terminal-style web interface built with Vue.js."),
                dbc.Button("Visit Site", href="https://terminal.kprsnt.in", target="_blank", color="info", className="me-1"),
                
                # Optional: Link to GitHub repo if public
                # dbc.Button("View Code", href="#", target="_blank", color="secondary"),
            ])
        # Add shadow-sm for subtle shadow, h-100 to make cards in a row equal height
        ], className="shadow-sm h-100"),
        width=12, md=6, lg=4, className="mb-4"), # mb-4 adds margin bottom

        # Project 2: Gemma3 Chatbot
        dbc.Col(dbc.Card([
            dbc.CardHeader("Local AI/LLM Chatbot"),
            dbc.CardBody([
                html.P("An interactive local model which hosted online using Google's Gemma3 model, served via Ollama and Open WebUI on Google Cloud Run."),
                dbc.Button("Visit Chat", href="chat.kprsnt.in", target="_blank", color="info", className="me-1"),
            ])
        # Add shadow-sm for subtle shadow, h-100 to make cards in a row equal height
        ], className="shadow-sm h-100"),
        width=12, md=6, lg=4, className="mb-4"), # mb-4 adds margin bottom

        # Project 3: AI Story Teller (Placeholder)
        dbc.Col(dbc.Card([
            dbc.CardHeader("AI Story Teller"),
            dbc.CardBody([
                html.P("Generates short stories based on user prompts using AI models. (Details coming soon!)"),
                dbc.Button("Visit Chat", href="https://storygemini.streamlit.app", target="_blank", color="info", className="me-1"),
            ])
        # Add shadow-sm for subtle shadow, h-100 to make cards in a row equal height
        ], className="shadow-sm h-100"),
        width=12, md=6, lg=4, className="mb-4"), # mb-4 adds margin bottom

        # Project 4: AI Tutor (Placeholder)
        dbc.Col(dbc.Card([
            dbc.CardHeader("AI Tutor"),
            dbc.CardBody([
                html.P("An interactive AI tutor for specific subjects. (Till Grade 10)"),
                dbc.Button("Visit Chat", href="https://aitutor.streamlit.app/", target="_blank", color="info", className="me-1"),
            ])
        # Add shadow-sm for subtle shadow, h-100 to make cards in a row equal height
        ], className="shadow-sm h-100"),
        width=12, md=6, lg=4, className="mb-4"), # mb-4 adds margin bottom

        # Project 5: CSV Plotter (Placeholder - could be integrated into Visualizations page)
        dbc.Col(dbc.Card([
            dbc.CardHeader("CSV Data Plotter"),
            dbc.CardBody([
                html.P("Upload a CSV file and generate various plots interactively."),
                dbc.Button("Visit Chat", href="https://plotcharts.streamlit.app", target="_blank", color="info", className="me-1"),
            ])
        # Add shadow-sm for subtle shadow, h-100 to make cards in a row equal height
        ], className="shadow-sm h-100"),
        width=12, md=6, lg=4, className="mb-4"), # mb-4 adds margin bottom

        # Add more projects as needed

    ], className="mt-3"), # Margin top for spacing
])
