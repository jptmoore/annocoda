
from dash import Dash, dash_table
from data import Data
import logging

log_format = "%(asctime)s::%(levelname)s::%(message)s"
logging.basicConfig(level='INFO', format=log_format)
log = logging.getLogger()

class Context:
    pass

ctx = Context()

app = Dash(__name__)

ctx.logger = app.logger
data = Data(ctx)
result = data.get_annotation(url="https://miiify.rocks/iiif/content/search?q=robinson")
app.layout = dash_table.DataTable(result)


if __name__ == '__main__':
    app.run_server(debug=True)
