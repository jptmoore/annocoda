from dash import Dash, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from annotation import Annotation
from manifest import Manifest
from components.carousel import carousel
from components.annotation_table import annotation_table
from components.search import search


class Context:
    pass


ctx = Context()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
ctx.logger = app.logger

annotation = Annotation(ctx)
manifest = Manifest(ctx)

annotation_data = annotation.default()
manifest_data = manifest.load(url="https://miiify.rocks/manifest/rustic_walking_routes")

app.layout = html.Div(
    className="p-5",
    style={"margin-left": "20%", "margin-right": "20%"},
    children=[
        html.Div(children=carousel(items=manifest.default())),
        html.Div(children=search),
        html.Div(id="status-bar"),
        html.Div(children=annotation_table(data=annotation.default())),
    ],
)


@app.callback(
    Output("status-bar", "children"),
    Input("table-data", "active_cell"),
    State("table-data", "data"),
)
def getActiveCell(active_cell, data):
    if active_cell:
        row = active_cell["row"]
        target = data[row]["key"]
        index = manifest.index_of_target(target)
        return html.P(f"{index}")
    else:
        return html.P("")


@app.callback(
    Output("table-data", "data"),
    Output("carousel-data", "items"),
    Input("search-button", "n_clicks"),
    State("search-input", "value"),
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        annotation_data = annotation.search(
            url=f"https://miiify.rocks/iiif/content/search?q={value}"
        )
        annotation_targets = annotation.make_target_list()
        manifest_data = manifest.filter_result_data(annotation_targets)
        manifest_targets = manifest.make_target_list()
        annotation_data = annotation.filter_result_data(manifest_targets)
        return annotation_data, manifest_data
    else:
        return annotation.default(), manifest.default()


if __name__ == "__main__":
    app.run_server(debug=True)
