import dash_bootstrap_components as dbc


card_1 = dbc.Card(
    [
        dbc.CardHeader(id="card-1"),
        dbc.CardImg(id="unbounded-image"),
    ]
)

card_2 = dbc.Card(
    [
        dbc.CardHeader(id="card-2"),
        dbc.CardImg(id="bounded-image"),
    ]
)