# pages/visualizations.py
import dash
from dash import dcc, html, Input, Output, callback # Input, Output, callback for interactivity
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Visualization Skills', order=3)

# --- Sample Data ---
# Example 1: Scatter plot data
df_scatter = pd.DataFrame({
    'x': range(1, 11),
    'y': [2, 1, 4, 3, 6, 5, 8, 7, 9, 10],
    'category': ['A']*5 + ['B']*5,
    'size': [10, 20, 15, 25, 30, 10, 20, 15, 25, 30]
})

# Example 2: Bar chart data
df_bar = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes'],
    'Amount': [4, 1, 2, 2],
    'City': ['SF', 'SF', 'Montreal', 'Montreal']
})

# Example 3: Line chart data (time series)
dates = pd.date_range('2023-01-01', periods=10)
df_line = pd.DataFrame({
    'Date': dates,
    'Value_A': pd.Series(range(10)) * 1.5 + 5,
    'Value_B': pd.Series(range(10)) * 0.8 + 12
})

# --- Create Figures ---
fig_scatter = px.scatter(df_scatter, x='x', y='y', color='category', size='size',
                         title="Interactive Scatter Plot",
                         labels={'x': 'X Axis Label', 'y': 'Y Axis Label'},
                         hover_data=['category'])
fig_scatter.update_layout(transition_duration=500) # Smooth transitions

fig_bar = px.bar(df_bar, x='Fruit', y='Amount', color='City', barmode='group',
                 title="Grouped Bar Chart")

fig_line = px.line(df_line, x='Date', y=['Value_A', 'Value_B'],
                   title="Simple Time Series Line Chart", markers=True)


# --- Layout ---
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Data Visualization Showcase"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.P("Here are some examples of interactive plots created using Plotly within a Dash application:"),
        ], width=12)
    ]),

    # Visualization 1: Scatter Plot
    dbc.Row([
        dbc.Col([
            html.H4("Scatter Plot Example"),
            dcc.Graph(id='scatter-plot', figure=fig_scatter)
        ], width=12, lg=6, className="mb-4") # Takes half width on large screens
    ]),

    # Visualization 2: Bar Chart
    dbc.Row([
         dbc.Col([
            html.H4("Bar Chart Example"),
            dcc.Graph(id='bar-chart', figure=fig_bar)
        ], width=12, lg=6, className="mb-4")
    ]),

    # Visualization 3: Line Chart
    dbc.Row([
         dbc.Col([
            html.H4("Line Chart Example"),
            dcc.Graph(id='line-chart', figure=fig_line)
        ], width=12, lg=6, className="mb-4")
    ]),

    # Placeholder for CSV Plotter Integration
    dbc.Row([
        dbc.Col([
            html.H3("Interactive CSV Plotter (Coming Soon!)"),
            html.P("This section will allow you to upload your own CSV data and generate plots."),
            # Add dcc.Upload component and callbacks here later
        ], width=12)
    ]),

])

# --- Callbacks (for future interactivity, e.g., CSV plotter) ---
# Example:
# @callback(
#     Output('some-output-div', 'children'),
#     Input('some-input-component', 'value')
# )
# def update_output(value):
#     # Process input and return updated component/data
#     return f'You entered: {value}'