import dash_bootstrap_components as dbc
from dash import html

from components.annotation_table import annotation_table


tray = dbc.Offcanvas(
    html.Div(annotation_table),
    id="tray",
    scrollable=True,
    title="Annotations",
    is_open=False,
    placement="bottom",
    backdrop="static",
    keyboard=False
)
