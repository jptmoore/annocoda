import dash_bootstrap_components as dbc
from dash import html

status = html.Div(
    dbc.Container(
        [
            html.H1("No results", className="display-3"),
            html.Hr(className="my-2"),
            html.P(
                id="status-message",
                className="lead",
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 rounded-3",
)