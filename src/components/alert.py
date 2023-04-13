import dash_bootstrap_components as dbc
from dash import html


alert = (
    dbc.Alert(
        id="alert",
        color="danger",
        dismissable=True,
        is_open=False,
    ),
)
