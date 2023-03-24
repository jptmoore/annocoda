import dash_bootstrap_components as dbc

def carousel(items):
    return (
        dbc.Carousel(
            id="carousel-data",
            items=items,
            style={"width": "100%"},
            controls=True,
            indicators=True,
            variant="dark"
        ),
    )