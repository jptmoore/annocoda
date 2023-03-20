from dash import Dash, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from annotation import Annotation
from manifest import Manifest
from components.carousel import carousel
from components.annotation_table import annotation_table
from components.search import search

import logging

log_format = "%(asctime)s::%(levelname)s::%(message)s"
logging.basicConfig(level="INFO", format=log_format)
log = logging.getLogger()


class Context:
    pass


ctx = Context()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

ctx.logger = app.logger

annotation = Annotation(ctx)
manifest = Manifest(ctx)

table_data = []
carousel_data = manifest.load(url="https://miiify.rocks/manifest/cats")

app.layout = html.Div(
    className="p-5",
    style={"margin-left": "20%", "margin-right": "20%"},
    children=[
        html.Div(children=carousel(carousel_data)),
        html.Div(children=search),
        html.Div(children=annotation_table(table_data)),
    ],
)


@app.callback(
    Output("annotation-data", "data"),
    Input("search-button", "n_clicks"),
    State("search-input", "value"),
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        table_data = annotation.search(
            url=f"https://miiify.rocks/iiif/content/search?q={value}"
        )
        return table_data


if __name__ == "__main__":
    app.run_server(debug=True)
