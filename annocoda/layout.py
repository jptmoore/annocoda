import dash_bootstrap_components as dbc
from dash import dcc
from components.tray import tray
from components.navbar import navbar
from components.tabs import tabs


def setup_layout():
    return dbc.Container(
        [
            dcc.Location(id='url', refresh=False),
            dcc.Store(id='storage'),
            dbc.Row(navbar),
            dbc.Row(tabs),
            dbc.Row(tray),
        ],
        style={
            "margin-top": "2%",
            "margin-bottom": "5%",
            "margin-left": "5%",
            "margin-right": "5%",
        },
        fluid="True",
    )
