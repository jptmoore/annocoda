from dash import Dash
import dash_bootstrap_components as dbc
from view import View
import requests_cache

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

class Context:
    pass

ctx = Context()
ctx.logger = app.logger
ctx.session = requests_cache.CachedSession("image_cache")

view = View(ctx)

app.layout = view.layout()
app.title = "Annocoda"

if __name__ == "__main__":
    app.run_server(debug=True)
