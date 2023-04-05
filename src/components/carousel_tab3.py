import dash_bootstrap_components as dbc

def carousel_tab3(items):
    return (
        dbc.Carousel(
            id="carousel-tab3",
            items=items,
            variant="dark",
            controls=True,
            indicators=True,
            interval=None,
        ),
    )