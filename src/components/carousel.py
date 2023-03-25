import dash_bootstrap_components as dbc

def carousel(items):
    return (
        dbc.Carousel(
            id="carousel-data",
            items=items,
            style={"width": "100%"},
            variant="dark",
            controls=False,
            indicators=False,
            interval=None,
        ),
    )