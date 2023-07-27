
import dash_bootstrap_components as dbc
from components.carousel import carousel
from components.cards import card_1
from components.splash import splash
from components.inform import inform


tab_style = {"border": "0", "display": "none"}
tabs = dbc.Tabs(
    [
        dbc.Tab(
            splash,
            tab_id="splash-tab",
            disabled=True,
            style={"padding": "50px"}
        ),
        dbc.Tab(
            carousel,
            tab_id="carousel-tab",
            disabled=True,
        ),
        dbc.Tab(
            card_1,
            tab_id="image-tab",
            disabled=True,
        ),
        dbc.Tab(
            inform,
            tab_id="status-tab",
            disabled=True,
            style={"padding": "150px"}
        ),
    ],
    id="tabs",
    active_tab="splash-tab",
    style=tab_style,
)