# app.py
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Use Dash Bootstrap Components theme
# Find more themes here: https://bootswatch.com/
APP_THEME = dbc.themes.LUX

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[APP_THEME], suppress_callback_exceptions=True)
server = app.server # Expose server variable for Procfile/Gunicorn

# --- Navigation Bar ---
navbar = dbc.NavbarSimple(
    children=[
        # Use dcc.Link for multi-page navigation
        dbc.NavItem(dbc.NavLink(page['name'], href=page['relative_path']))
        for page in dash.page_registry.values() # Automatically iterates through pages in the 'pages' folder
        # Add external links if needed
        # dbc.NavItem(dbc.NavLink("My GitHub", href="YOUR_GITHUB_LINK", external_link=True, target="_blank")),
    ],
    brand="Prashanth Kadasi", # Your Brand Name
    brand_href="/",    # Link brand name to home page
    color="primary",
    dark=True,
    className="mb-4", # Margin bottom for spacing
)

# --- Main Layout ---
app.layout = dbc.Container([
    navbar,
    # Add vertical padding to the page container area
    html.Div(dash.page_container, className="py-4") # py-4 adds padding top and bottom
], fluid=True)


# --- Run the App ---
if __name__ == '__main__':
    # Use app.run() instead of app.run_server()
    app.run(debug=True) # debug=True for development (auto-reloads)