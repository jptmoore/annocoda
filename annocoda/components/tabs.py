
import dash_bootstrap_components as dbc
from components.carousel import carousel
from components.cards import image_card
from components.splash import splash
from components.status import status


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
            image_card,
            tab_id="image-tab",
            disabled=True,
        ),
        dbc.Tab(
            status,
            tab_id="status-tab",
            disabled=True,
            style={"padding": "150px"}
        ),
    ],
    id="tabs",
    active_tab="splash-tab",
    style=tab_style,
)