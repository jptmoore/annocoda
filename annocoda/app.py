from dash import Dash, DiskcacheManager
import dash_bootstrap_components as dbc
from view import View
from context import Context

import diskcache
cache = diskcache.Cache("./callback_cache")
background_callback_manager = DiskcacheManager(cache)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], background_callback_manager=background_callback_manager)

ctx = Context(logger=app.logger)

app.layout = View(ctx).layout()
app.title = "Annocoda"

server = app.server

if __name__ == "__main__":
    app.run(host='0.0.0.0')
