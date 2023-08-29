import dash_bootstrap_components as dbc
from dash import html

splash = html.Div(
    dbc.Container(
        [
            html.H1("Getting started", className="display-3"),
            html.P(
                "Try some of the examples below",
                className="lead",
            ),
            dbc.ListGroup(
                [
                    dbc.ListGroupItem(
                        "Women war workers on the Metropolitan Railway",
                        href="?manifest=https://miiify.rocks/manifest/diamond_jubilee_of_the_metro&search=women%20war",
                    ),
                    dbc.ListGroupItem(
                        "Mentions of Pinner in Rustic walking routes from within the twelve-mile radius of Charing Cross",
                        href="?manifest=https://miiify.rocks/manifest/rustic_walking_routes&search=pinner",
                    ),
                    dbc.ListGroupItem(
                        "Monasteries within an Introduction to the Valor Ecclesiasticus",
                        href="?manifest=https://miiify.rocks/manifest/intro_valor_ecclesiasticus&search=monasteries",
                    ),
                    dbc.ListGroupItem(
                        "Greece in The works of the British poets",
                        href="?manifest=https://miiify.rocks/manifest/british_poets_1759_1834&search=greece",
                    ),                             
                ]
            ),
            html.P(),
            html.P(dbc.Button("Learn more", color="primary"), className="lead"),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 rounded-3",
)
