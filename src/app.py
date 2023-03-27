from dash import Dash, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from annotation import Annotation
from manifest import Manifest
from components.carousel import carousel
from components.annotation_table import annotation_table
from components.navbar import navbar
from components.statusbar import statusbar

class Context:
    pass


ctx = Context()

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
ctx.logger = app.logger

annotation = Annotation(ctx)
manifest = Manifest(ctx)

annotation_data = annotation.default()
manifest_data = manifest.load(url="https://miiify.rocks/manifest/diamond_jubilee_of_the_metro")


app.layout = dbc.Container(
    [
        dbc.Stack(html.Div(navbar)),
        html.P(),
        dbc.Stack(
            [
                html.Div(carousel(items=manifest.default())),
                html.Div(annotation_table(data=annotation.default())),
                html.Div(statusbar()),
            ],
        ),
    ],
    style={"margin-bottom": "5%", "margin-left": "5%", "margin-right": "5%"},
    fluid="True"
)


@app.callback(
    Output("table", "selected_cells"),
    Output("table", "active_cell"),
    Input("search-button", "n_clicks"),
)
def clear(n_clicks):
    return [], None


@app.callback(
    Output("carousel", "active_index"),
    Input("table", "active_cell"),
    State("table", "data"),
)
def getActiveCell(active_cell, data):
    if active_cell:
        row = active_cell["row"]
        target = data[row]["key"]
        index = manifest.index_of_target(target)
        return index
    else:
        return 0


@app.callback(
    Output("table", "data"),
    Output("carousel", "items"),
    Output("status-bar", "children"),
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
        count = len(annotation_data)
        message = f"{count} records"
        return annotation_data, manifest_data, message
    else:
        return annotation.default(), manifest.default(), None

app.title = 'Annocoda'

if __name__ == "__main__":
    app.run_server(debug=True)
