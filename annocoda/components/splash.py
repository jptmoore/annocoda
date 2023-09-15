import dash_bootstrap_components as dbc
from dash import html

splash = html.Div(
    dbc.Container(
        [
            html.H1("Getting started", className="display-3"),
            html.P(
                "Try searching the IIIF manifests referenced in the examples below:",
                className="lead",
            ),
            html.Div(
                [
                    html.H5(
                        "Women war workers on the Metropolitan Railway",
                        className="mb-1",
                    ),
                    html.A(
                        [
                            html.Img(
                                src="https://iiif.io/assets/images/logos/logo-sm.png",
                                style={"height": "20px", "width": "20px"},
                            )
                        ],
                        href="https://miiify.rocks/manifest/diamond_jubilee_of_the_metro",
                    ),
                ],
                className="d-flex w-100 justify-content-between",
            ),
            html.A(
                "https://annocoda.onrender.com/?manifest=https://miiify.rocks/manifest/diamond_jubilee_of_the_metro&search=women%20war",
                href="?manifest=https://miiify.rocks/manifest/diamond_jubilee_of_the_metro&search=women%20war",
            ),
            html.Pre(),
            html.Div(
                [
                    html.H5(
                        "Mentions of Pinner in Rustic walking routes from within the twelve-mile radius of Charing Cross",
                        className="mb-1",
                    ),
                    html.A(
                        [
                            html.Img(
                                src="https://iiif.io/assets/images/logos/logo-sm.png",
                                style={"height": "20px", "width": "20px"},
                            )
                        ],
                        href="https://miiify.rocks/manifest/rustic_walking_routes",
                    ),
                ],
                className="d-flex w-100 justify-content-between",
            ),
            html.A(
                "https://annocoda.onrender.com/?manifest=https://miiify.rocks/manifest/rustic_walking_routes&search=pinner",
                href="?manifest=https://miiify.rocks/manifest/rustic_walking_routes&search=pinner",
            ),
            html.Pre(),
            html.Div(
                [
                    html.H5(
                        "Monasteries within an Introduction to the Valor Ecclesiasticus",
                        className="mb-1",
                    ),
                    html.A(
                        [
                            html.Img(
                                src="https://iiif.io/assets/images/logos/logo-sm.png",
                                style={"height": "20px", "width": "20px"},
                            )
                        ],
                        href="https://miiify.rocks/manifest/intro_valor_ecclesiasticus",
                    ),
                ],
                className="d-flex w-100 justify-content-between",
            ),
            html.A(
                "https://annocoda.onrender.com/?manifest=https://miiify.rocks/manifest/intro_valor_ecclesiasticus&search=monasteries",
                href="?manifest=https://miiify.rocks/manifest/intro_valor_ecclesiasticus&search=monasteries",
            ),
            html.Pre(),
            html.Div(
                [
                    html.H5(
                        "Greece in the works of the British poets",
                        className="mb-1",
                    ),
                    html.A(
                        [
                            html.Img(
                                src="https://iiif.io/assets/images/logos/logo-sm.png",
                                style={"height": "20px", "width": "20px"},
                            )
                        ],
                        href="https://miiify.rocks/manifest/british_poets_1759_1834",
                    ),
                ],
                className="d-flex w-100 justify-content-between",
            ),
            html.A(
                "https://annocoda.onrender.com/?manifest=https://miiify.rocks/manifest/british_poets_1759_1834&search=greece",
                href="?manifest=https://miiify.rocks/manifest/british_poets_1759_1834&search=greece",
            ),
            html.Pre(),
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
