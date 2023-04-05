import dash_bootstrap_components as dbc

def carousel_tab2(items):
    return (
        dbc.Carousel(
            id="carousel-tab2",
            items=items,
            variant="dark",
            controls=True,
            indicators=True,
            interval=None,
        ),
    )