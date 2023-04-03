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
manifest_data = manifest.load(
    url="https://miiify.rocks/manifest/diamond_jubilee_of_the_metro"
)


tabs = dbc.Tabs(
    [
        dbc.Tab(html.Div(carousel(items=manifest.default())), label="Tab 1", tab_id="tab-1"),
        dbc.Tab(html.P("This is tab 2!"), label="Tab 2", tab_id="tab-2"),
    ],
    id="tabs",
)

app.layout = dbc.Container(
    [
        dbc.Row(html.Div(navbar)),
        dbc.Row(html.P()),
        dbc.Row(html.Div(tabs)),
        dbc.Offcanvas(
            dbc.Row(html.Div(annotation_table(data=annotation.default()))),
            id="offcanvas-scrollable",
            scrollable=True,
            title="Annotations",
            is_open=False,
            placement="bottom",
        ),
        dbc.Row(html.Div(statusbar, style={"text-align": "center"})),
    ],
    style={
        "margin-top": "2%",
        "margin-bottom": "5%",
        "margin-left": "5%",
        "margin-right": "5%",
    },
    fluid="True",
)


@app.callback(
    Output("offcanvas-scrollable", "is_open"),
    Output("table", "data"),
    Input("status-bar", "n_clicks"),
    State("offcanvas-scrollable", "is_open"),
    State("carousel", "active_index"),
    State("carousel", "items"),
)
def toggle_offcanvas_scrollable(n_clicks, is_open, active_index, items):
    if n_clicks:
        target = items[active_index].get("key")
        result = annotation.filter_result_data([target])
        return not is_open, result
    else:
        return is_open, items


@app.callback(
    Output("table", "selected_cells"),
    Input("offcanvas-scrollable", "is_open"),
)
def deselectRows(selected_cells):
    return []


@app.callback(
    Output("carousel", "active_index"),
    Output("table", "active_cell"),
    Output("carousel", "items", allow_duplicate=True),
    Input("carousel", "items"),
    Input("table", "active_cell"),
    State("table", "data"),
    prevent_initial_call=True,
)
def getActiveCell(items, active_cell, data):
    if active_cell:
        row = active_cell["row"]
        target = data[row]["key"]
        box = manifest.get_frag_selector_cords(target)
        index = manifest.index_of_target(target)
        src = items[index].get("src")
        print("box:", box, "src:", src)
        return index, None, items
    else:
        return 0, active_cell, items


@app.callback(
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
        message = f"{count} annotations"
        return manifest_data, message
    else:
        return manifest.default(), None


app.title = "Annocoda"

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=True)
