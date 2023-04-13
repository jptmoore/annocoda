from dash import Dash
import dash_bootstrap_components as dbc
from annotation import Annotation
from manifest import Manifest
from polygon import Polygon
from callback import Callback
from layout import layout
import requests_cache

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


class Context:
    pass

ctx = Context()
ctx.logger = app.logger
ctx.session = requests_cache.CachedSession("image_cache")

annotation = Annotation(ctx)
manifest = Manifest(ctx)
polygon = Polygon(ctx)

Callback(annotation, manifest, polygon).setup_callbacks()
manifest.load(url="https://miiify.rocks/manifest/diamond_jubilee_of_the_metro")

app.layout = layout
app.title = "Annocoda"
if __name__ == "__main__":
    app.run_server(debug=True)
