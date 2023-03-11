import dash_bootstrap_components as dbc

carousel = (
    dbc.Carousel(
        id="carousel",
        style={"width": "100%"},
        controls=True,
        indicators=True,
        items=[
            {
                "key": "foo",
                "src": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Fat_cat%2C_asleep_%28319313958%29.jpg",
                "img_style": {"height": "10%", "width": "10%"},
            },
            {
                "key": "bar",
                "src": "https://upload.wikimedia.org/wikipedia/commons/9/90/Crimean_Tom.jpg",
                "img_style": {"height": "10%", "width": "10%"},
            },
            {
                "key": "baz",
                "src": "https://upload.wikimedia.org/wikipedia/commons/1/16/Stationmaster_NITAMA_20110105.jpg",
                "img_style": {"height": "10%", "width": "10%"},
            },
        ],
    ),
)