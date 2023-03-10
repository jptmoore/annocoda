from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from data import Data
import logging

log_format = "%(asctime)s::%(levelname)s::%(message)s"
logging.basicConfig(level="INFO", format=log_format)
log = logging.getLogger()


class Context:
    pass


ctx = Context()

app = Dash(__name__)

ctx.logger = app.logger
data = Data(ctx)
result = []


app.layout = html.Div(
    children=[
        html.H1(children="Annocoder"),
        html.Div(children="Search"),
        dbc.Input(id="keywords", placeholder="keywords...", type="text"),
        html.Button("Submit", id="search-button", n_clicks=0),
        dash_table.DataTable(
            id="annotations",
            data=result,
            style_cell={"textAlign": "left"},
            style_data={"whiteSpace": "normal", "height": "auto", "lineHeight": "15px"},
        ),
    ]
)


@app.callback(
    Output("annotations", "data"),
    Input("search-button", "n_clicks"),
    State("keywords", "value"),
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        result = data.get_annotation(
            url=f"https://miiify.rocks/iiif/content/search?q={value}"
        )
        return result


if __name__ == "__main__":
    app.run_server(debug=True)
