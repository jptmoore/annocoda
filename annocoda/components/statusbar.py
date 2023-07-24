import dash_bootstrap_components as dbc
from dash import html


statusbar = html.H3(
    dbc.Badge(color="primary", id="status-bar", n_clicks=0, className="d-grid gap-2 col-6 mx-auto")
)
