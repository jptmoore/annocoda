
import dash_bootstrap_components as dbc
from dash import html
from components.carousel import carousel
from components.cards import card_1, card_2
from components.splash import splash
from components.inform import inform


tab_style = {"border": "0", "display": "none"}
tabs = dbc.Tabs(
    [
        dbc.Tab(
            splash,
            tab_id="tab-0",
            disabled=True,
            style={"padding": "50px"}
        ),
        dbc.Tab(
            carousel,
            tab_id="tab-1",
            disabled=True,
        ),
        dbc.Tab(
            card_1,
            tab_id="tab-2",
            disabled=True,
        ),
        dbc.Tab(
            card_2,
            tab_id="tab-3",
            disabled=True,
        ),
        dbc.Tab(
            inform,
            tab_id="tab-4",
            disabled=True,
            style={"padding": "150px"}
        ),
    ],
    id="tabs",
    active_tab="tab-0",
    style=tab_style,
)