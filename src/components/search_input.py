import dash_bootstrap_components as dbc

search_input = (
    dbc.Input(
        id="search-input",
        placeholder="keywords...",
        type="text",
        style={"margin-top": "5px"},
    ),
)
