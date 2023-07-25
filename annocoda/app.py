from dash import Dash
import dash_bootstrap_components as dbc
from view import View
from context import Context

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

ctx = Context(logger=app.logger)

app.layout = View(ctx).layout()
app.title = "Annocoda"

if __name__ == "__main__":
    app.run_server(debug=True)
