
from dash import Dash, html
from data import Data
import logging

log_format = "%(asctime)s::%(levelname)s::%(message)s"
logging.basicConfig(level='INFO', format=log_format)
log = logging.getLogger()

class Context:
    pass

ctx = Context()

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

app = Dash(__name__)

ctx.logger = app.logger
data = Data(ctx)
df = data.get_annotation(url="https://miiify.rocks/iiif/content/search?q=eastcote")

app.layout = html.Div([
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])


if __name__ == '__main__':
    app.run_server(debug=True)
