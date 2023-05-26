from dash import Dash
import dash_bootstrap_components as dbc
from annotation import Annotation
from manifest import Manifest
from polygon import Polygon
from callback import Callback
from layout import layout
from data import Data
import requests_cache

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


class Context:
    pass

ctx = Context()
ctx.logger = app.logger
ctx.session = requests_cache.CachedSession("image_cache")
ctx.datamodel = Data()

annotation = Annotation(ctx)
polygon = Polygon(ctx)

Callback(annotation, polygon, ctx).setup_callbacks()

app.layout = layout
app.title = "Annocoda"
if __name__ == "__main__":
    app.run_server(debug=True)
