import dash_bootstrap_components as dbc
from dash import html


statusbar = html.Div(
    dbc.Button(color="primary", id="status-bar", outline=True, n_clicks=0, className="d-grid gap-2 col-6 mx-auto")
)
