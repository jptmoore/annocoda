import dash_bootstrap_components as dbc
from dash import html


statusbar = html.H3(
    dbc.Badge(color="primary", id="status-bar", n_clicks=0, className="me-1")
)
