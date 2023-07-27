import dash_bootstrap_components as dbc


image_card = dbc.Card(
    [
        dbc.CardHeader(id="image-header"),
        dbc.CardImg(id="image"),
    ]
)
