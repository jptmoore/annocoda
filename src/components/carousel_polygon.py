import dash_bootstrap_components as dbc

def carousel_polygon(items):
    return (
        dbc.Carousel(
            id="carousel-polygon",
            items=items,
            variant="dark",
            controls=True,
            indicators=True,
            interval=None,
        ),
    )