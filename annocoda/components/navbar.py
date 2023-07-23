import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

logo = "../assets/annocoda-logo.png"


search_bar = dbc.Form(
    dbc.Row(
        [
            dbc.Label("Manifest", width="auto"),
            dbc.Col(
                dbc.Input(id="manifest-input", placeholder="Enter URL"),
                className="me-3",
            ),
            dbc.Label("Search", width="auto"),
            dbc.Col(
                dbc.Input(id="search-input", placeholder="Enter keywords"),
                className="me-3",
            ),
            dbc.Col(dbc.Button("Submit", id="search-button", color="primary", n_clicks=0), width="auto"),
        ],
        className="g-2",
    )
)


image = (
    html.A(
        dbc.Row(
            [
                dbc.Col(html.Img(src=logo, height="30px", style={"padding-bottom": "5px"})),
            ],
            align="center",
            className="g-0",
        ),
        href="https://plotly.com",
        style={"textDecoration": "none"},
    ),
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.Div(children=image),
            html.Div(children=search_bar),
        ]
    ),
    color="white",
    dark=False,
)
