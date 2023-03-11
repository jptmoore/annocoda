import dash_bootstrap_components as dbc

search = dbc.Form(
    dbc.Row(
        [
            dbc.Col(
                dbc.Input(id="search-input", type="text", placeholder="keywords"),
                className="me-3",
            ),
            dbc.Col(
                dbc.Button("Search", id="search-button", color="primary", n_clicks=0),
                width="auto",
            ),
        ],
        className="g-2",
        style={"margin-top": "5px"},
    )
)
