from dash import Dash, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from annotation import Annotation
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
anno = Annotation(ctx)
result = []


app.layout = html.Div(
    className="p-5",
    style={"margin-left": "20%", "margin-right": "20%"},
    children=[
        html.Div(children=carousel),
        html.Div(children=search),
        html.Div(children=annotation_table(result)),
    ],
)


@app.callback(
    Output("annotation-data", "data"),
    Input("search-button", "n_clicks"),
    State("search-input", "value"),
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        result = anno.search(
            url=f"https://miiify.rocks/iiif/content/search?q={value}"
        )
        return result


if __name__ == "__main__":
    app.run_server(debug=True)
