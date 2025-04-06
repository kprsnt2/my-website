# pages/about.py
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# Register this page with Dash
# path='/' makes it the home page
dash.register_page(__name__, path='/', name='About Me', order=0)

# Page layout
layout = dbc.Container([
    dbc.Row([
        # Add padding to the column content
        dbc.Col([
            html.H1("Hello, I'm Prashanth Kumar Kadasi"),
            html.P(
                "Welcome to my personal portfolio! I'm passionate about data, AI, web development] "
                "and leveraging technology to solve interesting problems."
            ),
            html.P(
                "This website showcases my skills, projects, and journey. It's built entirely in Python using Dash and Plotly, "
                "demonstrating my ability to create interactive web applications, data visualizations, and AI-powered tools like chatbots."
            ),
        ], width=12, className="p-3") # p-3 adds padding on all sides
    ])
], className="mt-4") # mt-4 adds margin top to the container for this page
