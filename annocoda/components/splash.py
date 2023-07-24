import dash_bootstrap_components as dbc
from dash import html

splash = html.Div(
    dbc.Container(
        [
            html.H1("Getting started", className="display-3"),
            html.P(
                "Some blurb",
                className="lead",
            ),
            html.Hr(className="my-2"),
            html.P(
                "blurb blurb blurb blurb blurb blurb"
            ),
            html.P(
                dbc.Button("Learn more", color="primary"), className="lead"
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 rounded-3",
)

