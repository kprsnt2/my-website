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
        # Local AI Chatbot
        dbc.Col(dbc.Card([
            dbc.CardHeader("Local AI/LLM Chatbot"),
            dbc.CardBody([
                html.P("An AI chatbot powered by Google's Gemma3 model, hosted locally and deployed via Ollama and Open WebUI on Google Cloud Run."),
                dbc.Button("Visit Chat", href="https://chat.kprsnt.in", target="_blank", color="info", className="me-1"),
            ])
        ], className="shadow-sm h-100"), width=12, md=6, lg=4, className="mb-4"),

        # CSV Data Plotter
        dbc.Col(dbc.Card([
            dbc.CardHeader("CSV Data Plotter"),
            dbc.CardBody([
                html.P("Upload a CSV file and explore interactive visualizations using Streamlit. Supports various chart types."),
                dbc.Button("Visit Here", href="https://plotcharts.streamlit.app", target="_blank", color="info", className="me-1"),
            ])
        ], className="shadow-sm h-100"), width=12, md=6, lg=4, className="mb-4"),

        # Python Website
        dbc.Col(dbc.Card([
            dbc.CardHeader("Python Portfolio Website - This one"),
            dbc.CardBody([
                html.P("A personal portfolio website fully built with Python and deployed on Render. Showcases projects and skills."),
                dbc.Button("Visit Site", href="https://kprsnt.in", target="_blank", color="info", className="me-1"),
            ])
        ], className="shadow-sm h-100"), width=12, md=6, lg=4, className="mb-4"),

        # Terminal Website
        dbc.Col(dbc.Card([
            dbc.CardHeader("Terminal Website Interface"),
            dbc.CardBody([
                html.P("A retro-style terminal interface built using Vue.js, simulating a hacker-themed shell. Fully responsive and deployed online."),
                dbc.Button("Visit Site", href="https://terminal.kprsnt.in", target="_blank", color="info", className="me-1"),
            ])
        ], className="shadow-sm h-100"), width=12, md=6, lg=4, className="mb-4"),

        # Next.js Website
        dbc.Col(dbc.Card([
            dbc.CardHeader("Next.js Developer Site"),
            dbc.CardBody([
                html.P("A work-in-progress personal website created using Next.js with modern UI concepts from v0.dev. Deployed on Vercel."),
                dbc.Button("Visit Site", href="https://vercel.kprsnt.in", target="_blank", color="info", className="me-1"),
            ])
        ], className="shadow-sm h-100"), width=12, md=6, lg=4, className="mb-4"),

        # AI Story Teller
        dbc.Col(dbc.Card([
            dbc.CardHeader("AI Story Teller"),
            dbc.CardBody([
                html.P("Generates creative short stories based on user prompts using large language models. Built with Streamlit."),
                dbc.Button("Visit Here", href="https://storygemini.streamlit.app", target="_blank", color="info", className="me-1"),
            ])
        ], className="shadow-sm h-100"), width=12, md=6, lg=4, className="mb-4"),

        # AI Tutor
        dbc.Col(dbc.Card([
            dbc.CardHeader("AI Tutor"),
            dbc.CardBody([
                html.P("An interactive AI-powered tutor for students up to Grade 10. Provides real-time answers and explanations."),
                dbc.Button("Visit Here", href="https://aitutor.streamlit.app/", target="_blank", color="info", className="me-1"),
            ])
        ], className="shadow-sm h-100"), width=12, md=6, lg=4, className="mb-4"),


    ], className="mt-3"),
])
