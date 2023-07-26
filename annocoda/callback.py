from dash import callback, State, Input, Output

def setup_callbacks(controller):

    @callback(
        Output("tabs", "active_tab"),
        Output("unbounded-image", "src"),
        Input("offcanvas-scrollable", "is_open"),
        State("carousel", "active_index"),
        State("carousel", "items"),
        State("tabs", "active_tab"),
    )
    def select_tab(is_open, active_index, items, active_tab):
        match active_tab:
            case "tab-0":
                return active_tab, None
            case "tab-1":
                if is_open:
                    src = items[active_index].get("src")
                    image = controller.polygon.get_image(src)
                    return "tab-2", image
            case "tab-2":
                return "tab-1", None
            case "tab-3":
                return "tab-1", None

    # open tray
    @callback(
        Output("offcanvas-scrollable", "is_open"),
        Output("carousel", "active_index"),
        Output("table", "data"),
        Output("card-1", "children"),
        Input("annotation-button", "n_clicks"),
        State("offcanvas-scrollable", "is_open"),
        State("carousel", "active_index"),
        State("carousel", "items"),
    )
    def toggle_tray(n_clicks, is_open, active_index, items):
        if n_clicks:
            target = items[active_index].get("key")
            annotations = controller.get_annotations(target)
            return not is_open, active_index, annotations, "test header 1"
        else:
            return is_open, 0, items, None

    @callback(
        Output("table", "selected_cells"),
        Input("offcanvas-scrollable", "is_open"),
    )
    def deselect_annotation(is_open):
        return []

    @callback(
        Output("table", "active_cell"),
        Output("tabs", "active_tab", allow_duplicate=True),
        Output("bounded-image", "src"),
        Output("card-2", "children"),
        Input("table", "active_cell"),
        State("table", "data"),
        prevent_initial_call=True,
    )
    def get_annotation_data(active_cell, data):
        if active_cell:
            row = active_cell["row"]
            target = data[row]["key"]
            rows = controller.get_rows(target)
            box = rows[row]["frag_selector"]
            src = rows[row]["src"]
            image = controller.get_box(src, box)
            return None, "tab-3", image, "test header 2"

    @callback(
        Output("tabs", "active_tab", allow_duplicate=True),
        Output("carousel", "items"),
        Input("search-button", "n_clicks"),
        State("search-input", "value"),
        State("manifest-input", "value"),
        prevent_initial_call=True,
    )
    def search(n_clicks, search_value, manifest_value):
        if n_clicks > 0 and search_value != None:
            result = controller.query(search_value, manifest_value)
            count = controller.get_image_count()
            if count == 0:
                return "tab-4", []
            else:
                return "tab-1", result
        else:
            return "tab-0", []
