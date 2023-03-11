from dash import html

search_button = (
    html.Button(
        "Submit",
        id="search-button",
        n_clicks=0,
        style={"margin-top": "5px"},
    ),
)