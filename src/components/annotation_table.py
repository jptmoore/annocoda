from dash import dash_table


def annotation_table(data):
    return (
        dash_table.DataTable(
            id="annotation-data",
            data=data,
            style_header={"display": "none"},
            style_cell={"textAlign": "left"},
            style_data={"color": "black", "backgroundColor": "white", "whiteSpace": "normal", "height": "auto"},
            style_data_conditional=[
                {
                    "if": {"row_index": "odd"},
                    "backgroundColor": "rgb(220, 220, 220)",
                }
            ],
        ),
    )
