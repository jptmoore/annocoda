import dash_bootstrap_components as dbc
from components.statusbar import statusbar
from dash import html


carousel = (
    dbc.Carousel(
        id="carousel",
        items=[],
        variant="dark",
        controls=True,
        indicators=True,
        interval=None,
    ),
    html.Div(statusbar),
)
