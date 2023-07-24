from dash import html
import dash_bootstrap_components as dbc
from components.annotation_table import annotation_table
from components.navbar import navbar
from components.tabs import tabs


layout = dbc.Container(
    [
        dbc.Row(html.Div(navbar)),
        dbc.Row(html.Div(tabs)),
        dbc.Row(dbc.Offcanvas(
            html.Div(annotation_table),
            id="offcanvas-scrollable",
            scrollable=True,
            title="Annotations",
            is_open=False,
            placement="bottom",
        )),
    ],
    style={
        "margin-top": "2%",
        "margin-bottom": "5%",
        "margin-left": "5%",
        "margin-right": "5%",
    },
    fluid="True",
)