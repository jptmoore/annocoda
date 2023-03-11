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

app.layout = html.Div(
    className="p-5",
    style={"margin-left": "100px", "margin-right": "100px"},
    children=[
        html.Div(children=carousel),
        html.Div(
            style={"margin-top": "15px"},
            children=[
                dbc.Input(
                    id="keywords",
                    placeholder="keywords...",
                    type="text",
                ),
                html.Button(
                    "Submit",
                    id="search-button",
                    n_clicks=0,
                    style={"margin-top": "5px"},
                ),
            ],
        ),
        dash_table.DataTable(
            id="annotations",
            data=result,
            style_header={"display": "none"},
            style_cell={"textAlign": "left"},
            style_data={"whiteSpace": "normal", "height": "auto", "lineHeight": "15px"},
        ),
    ],
)


@app.callback(
    Output("annotations", "data"),
    Input("search-button", "n_clicks"),
    State("keywords", "value"),
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        result = data.get_annotation(
            url=f"https://miiify.rocks/iiif/content/search?q={value}"
        )
        return result


if __name__ == "__main__":
    app.run_server(debug=True)
