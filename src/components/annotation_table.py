from dash import dash_table

def annotation_table(data):
    return (
        dash_table.DataTable(
            id="annotation-data",
            data=data,
            style_header={"display": "none"},
            style_cell={"textAlign": "left"},
            style_data={"whiteSpace": "normal", "height": "auto", "lineHeight": "15px"},
        ),
    )
