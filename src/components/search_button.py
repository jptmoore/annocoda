import dash_bootstrap_components as dbc

search_button = dbc.Button(
    "Search",
    id="search-button",
    color="primary",
    className="me-1",
    n_clicks=0,
    style={"margin-top": "5px"}
)
