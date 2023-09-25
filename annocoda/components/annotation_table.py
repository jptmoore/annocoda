from dash import dash_table


annotation_table = (
    dash_table.DataTable(
        id="annotation-table",
        data=[],
        columns=[
            {"name": "value", "id": "value", 'type': 'text', 'presentation': 'markdown'},
        ],
        style_header={"display": "none"},
        hidden_columns=["key"],
        css=[{"selector": ".show-hide", "rule": "display: none"}],
        style_cell={"textAlign": "left"},
        style_data={
            "color": "black",
            "backgroundColor": "white",
            "whiteSpace": "normal",
            "height": "auto",
        },
        style_data_conditional=[
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "rgb(220, 220, 220)",
            }
        ],
    ),
)
