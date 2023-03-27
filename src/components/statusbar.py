import dash_bootstrap_components as dbc
from dash import html


statusbar = html.H3(
    dbc.Badge(pill=True, color="primary", className="me-1", id="status-bar")
)
