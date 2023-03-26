import dash_bootstrap_components as dbc

def carousel(items):
    return (
        dbc.Carousel(
            id="carousel",
            items=items,
            variant="dark",
            controls=False,
            indicators=False,
            interval=None,
        ),
    )