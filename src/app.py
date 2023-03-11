from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from data import Data
import logging

log_format = "%(asctime)s::%(levelname)s::%(message)s"
logging.basicConfig(level="INFO", format=log_format)
log = logging.getLogger()


class Context:
    pass


ctx = Context()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

ctx.logger = app.logger
data = Data(ctx)
result = []

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

annotation_data = (
    dash_table.DataTable(
        id="annotation-data",
        data=result,
        style_header={"display": "none"},
        style_cell={"textAlign": "left"},
        style_data={"whiteSpace": "normal", "height": "auto", "lineHeight": "15px"},
    ),
)


search_input = (
    dbc.Input(
        id="search-input",
        placeholder="keywords...",
        type="text",
        style={"margin-top": "5px"}
    ),
)

search_button = (
    html.Button(
        "Submit",
        id="search-button",
        n_clicks=0,
        style={"margin-top": "5px"},
    ),
)

app.layout = html.Div(
    className="p-5",
    style={"margin-left": "20%", "margin-right": "20%"},
    children=[
        html.Div(children=carousel),
        html.Div(children=search_input), 
        html.Div(children=search_button),
        html.Div(children=annotation_data),
    ],
)

@app.callback(
    Output("annotation-data", "data"),
    Input("search-button", "n_clicks"),
    State("search-input", "value"),
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        result = data.get_annotation(
            url=f"https://miiify.rocks/iiif/content/search?q={value}"
        )
        return result


if __name__ == "__main__":
    app.run_server(debug=True)
