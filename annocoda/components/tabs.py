
import dash_bootstrap_components as dbc
from dash import html
from components.carousel import carousel
from components.cards import card_1, card_2


tab_style = {"border": "0", "display": "none"}
tabs = dbc.Tabs(
    [
        dbc.Tab(
            html.Div(carousel),
            tab_id="tab-1",
            disabled=True,
            active_tab_style=tab_style,
            active_label_style=tab_style,
        ),
        dbc.Tab(
            card_1,
            tab_id="tab-2",
            disabled=True,
            active_tab_style=tab_style,
            active_label_style=tab_style,
        ),
        dbc.Tab(
            card_2,
            tab_id="tab-3",
            disabled=True,
            active_tab_style=tab_style,
            active_label_style=tab_style,
        ),
    ],
    id="tabs",
    active_tab="tab-1",
    style=tab_style,
)