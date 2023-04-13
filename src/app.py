from dash import Dash, html
import dash_bootstrap_components as dbc
from components.annotation_table import annotation_table
from components.navbar import navbar
from components.statusbar import statusbar
from components.tabs import tabs
from annotation import Annotation
from manifest import Manifest
from polygon import Polygon
from callback import Callback
import requests_cache

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container(
    [
        dbc.Row(html.Div(navbar)),
        dbc.Row(html.P()),
        dbc.Row(html.Div(tabs)),
        dbc.Offcanvas(
            dbc.Row(html.Div(annotation_table)),
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


class Context:
    pass

ctx = Context()
ctx.logger = app.logger
ctx.session = requests_cache.CachedSession("image_cache")

annotation = Annotation(ctx)
manifest = Manifest(ctx)
polygon = Polygon(ctx)

annotation_data = annotation.default()
manifest_data = manifest.load(
    url="https://miiify.rocks/manifest/diamond_jubilee_of_the_metro"
)

Callback(annotation, manifest, polygon).setup_callbacks()

app.title = "Annocoda"
if __name__ == "__main__":
    app.run_server(debug=True)
