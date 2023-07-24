from dash import html
import dash_bootstrap_components as dbc
from components.tray import tray
from components.navbar import navbar
from components.tabs import tabs


layout = dbc.Container(
    [
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