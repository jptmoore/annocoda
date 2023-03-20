import dash_bootstrap_components as dbc

def carousel(items):
    return (
        dbc.Carousel(
            id="carousel",
            style={"width": "100%"},
            controls=True,
            indicators=True,
            items=items,
        ),
    )