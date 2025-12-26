# app.py
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

# Dark theme for modern aesthetic
APP_THEME = dbc.themes.DARKLY

# Google Fonts for premium typography
GOOGLE_FONTS = "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap"

# Font Awesome for icons
FONT_AWESOME = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"

app = dash.Dash(
    __name__, 
    use_pages=True, 
    external_stylesheets=[APP_THEME, GOOGLE_FONTS, FONT_AWESOME], 
    suppress_callback_exceptions=True,
    title="Prashanth Kumar Kadasi | Portfolio",
    update_title="Loading...",
    url_base_pathname='/'  # Explicitly set base pathname
)

# Custom favicon (PK initials)
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect fill='%23667eea' rx='20' width='100' height='100'/><text x='50' y='65' font-family='Arial' font-size='45' font-weight='bold' fill='white' text-anchor='middle'>PK</text></svg>">
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# --- Navigation Bar ---
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(page['name'], href=page['relative_path']))
        for page in dash.page_registry.values()
    ],
    brand="Prashanth Kadasi",
    brand_href="/",
    color="primary",
    dark=True,
    className="mb-4",
)

# --- Main Layout ---
app.layout = dbc.Container([
    navbar,
    html.Div(dash.page_container, className="py-4")
], fluid=True)

# CRITICAL: Expose the Flask server for Vercel
server = app.server

# This is important - remove the if __name__ == '__main__' block
# or keep it but don't use app.run()
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)