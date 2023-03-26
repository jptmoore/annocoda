import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

PLOTLY_LOGO = (
    "../assets/annocoda-high-resolution-logo-color-on-transparent-background.png"
)


search_bar = dbc.Form(
    dbc.Row(
        [
            dbc.Col(
                dbc.Input(id="search-input", type="search", placeholder="keywords"),
                className="me-3",
            ),
            dbc.Col(
                dbc.Button("Search", id="search-button", color="primary", n_clicks=0),
                width="auto",
            ),
        ],
        className="g-2",
    )
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="80px")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            html.Div(children=search_bar),
        ]
    ),
    color="white",
    dark=False,
)
