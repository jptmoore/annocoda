from dash import dash_table

def annotation_table(result):
    return (
        dash_table.DataTable(
            id="annotation-data",
            data=result,
            style_header={"display": "none"},
            style_cell={"textAlign": "left"},
            style_data={"whiteSpace": "normal", "height": "auto", "lineHeight": "15px"},
        ),
    )