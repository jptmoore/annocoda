import dash_bootstrap_components as dbc
from dash import html


carousel = (
    dbc.Carousel(
        id="carousel",
        items=[],
        active_index=0,
        variant="dark",
        controls=True,
        indicators=True,
        interval=None,
    ),
    html.Div(
        dbc.Button(
            "view annotations",
            color="primary",
            id="annotation-button",
            outline=True,
            n_clicks=0,
            className="d-grid gap-2 col-6 mx-auto",
        )
    ),
)
