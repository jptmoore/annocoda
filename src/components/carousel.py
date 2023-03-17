import dash_bootstrap_components as dbc

carousel = (
    dbc.Carousel(
        id="carousel",
        style={"width": "100%"},
        controls=True,
        indicators=True,
        items=[
            {
                "key": "logo",
                "src": "../assets/annocoda-high-resolution-logo-color-on-transparent-background.png",
                "img_style": {"height": "10%", "width": "10%"},
            },
            {
                "key": "1",
                "src": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Fat_cat%2C_asleep_%28319313958%29.jpg",
                "img_style": {"height": "10%", "width": "10%"},
            },
            {
                "key": "2",
                "src": "https://upload.wikimedia.org/wikipedia/commons/9/90/Crimean_Tom.jpg",
                "img_style": {"height": "10%", "width": "10%"},
            },
            {
                "key": "19",
                "src": "https://upload.wikimedia.org/wikipedia/commons/1/18/Socks_the_Cat_Explores.jpg",
                "img_style": {"height": "10%", "width": "10%"},
            },
        ],
    ),
)