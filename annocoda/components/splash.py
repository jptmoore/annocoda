import dash_bootstrap_components as dbc
from dash import html, DiskcacheManager

splash = html.Div(
    dbc.Container(
        [
            html.H1("Getting started", className="display-3"),
            html.P(
                "Try searching the IIIF manifests referenced in the examples below:",
                className="lead",
            ),
            dbc.ListGroup(
                [
                    dbc.ListGroupItem(
                        [
                            html.Div(
                                [
                                    html.H5(
                                        "Women war workers on the Metropolitan Railway",
                                        className="mb-1",
                                    ),
                                    html.Small("\U0001F680", className="text-success"),
                                ],
                                className="d-flex w-100 justify-content-between",
                            ),
                            html.A(
                                "https://annocoda.onrender.com/?manifest=https://miiify.rocks/manifest/diamond_jubilee_of_the_metro&search=women%20war",
                                href="?manifest=https://miiify.rocks/manifest/diamond_jubilee_of_the_metro&search=women%20war",
                            ),
                        ]
                    ),
                    dbc.ListGroupItem(
                        [
                            html.Div(
                                [
                                    html.H5(
                                        "Mentions of Pinner in Rustic walking routes from within the twelve-mile radius of Charing Cross",
                                        className="mb-1",
                                    ),
                                    html.Small("\U0001F680", className="text-success"),
                                ],
                                className="d-flex w-100 justify-content-between",
                            ),
                            html.A(
                                "https://annocoda.onrender.com/?manifest=https://miiify.rocks/manifest/rustic_walking_routes&search=pinner",
                                href="?manifest=https://miiify.rocks/manifest/rustic_walking_routes&search=pinner",
                            ),
                        ]
                    ),
                    dbc.ListGroupItem(
                        [
                            html.Div(
                                [
                                    html.H5(
                                        "Monasteries within an Introduction to the Valor Ecclesiasticus",
                                        className="mb-1",
                                    ),
                                    html.Small("\U0001F680", className="text-success"),
                                ],
                                className="d-flex w-100 justify-content-between",
                            ),
                            html.A(
                                "https://annocoda.onrender.com/?manifest=https://miiify.rocks/manifest/intro_valor_ecclesiasticus&search=monasteries",
                                href="?manifest=https://miiify.rocks/manifest/intro_valor_ecclesiasticus&search=monasteries",
                            ),
                        ]
                    ),
                    dbc.ListGroupItem(
                        [
                            html.Div(
                                [
                                    html.H5(
                                        "Greece in the works of the British poets",
                                        className="mb-1",
                                    ),
                                    html.Small("\U0001F680", className="text-success"),
                                ],
                                className="d-flex w-100 justify-content-between",
                            ),
                            html.A(
                                "https://annocoda.onrender.com/?manifest=https://miiify.rocks/manifest/british_poets_1759_1834&search=greece",
                                href="?manifest=https://miiify.rocks/manifest/british_poets_1759_1834&search=greece",
                            ),
                        ]
                    ),
                ]
            ),
            html.P(),
            html.P(
                dbc.Button(
                    "Learn more",
                    color="primary",
                    href="https://github.com/jptmoore/annocoda",
                ),
                className="lead",
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 rounded-3",
)
