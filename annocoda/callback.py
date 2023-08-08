from dash import callback, State, Input, Output
from dash import no_update
from dash.exceptions import PreventUpdate


def setup_callbacks(controller):
    @callback(
        Output("image", "src"),
        Output("image-header", "children"),
        Input("annotation-button", "n_clicks"),
        State("carousel", "active_index"),
        State("carousel", "items"),
    )
    def display_image(n_clicks, active_index, items):
        if n_clicks:
            src = items[active_index].get("src")
            image = controller.polygon.get_image(src)
            return image, "header 1"
        else:
            raise PreventUpdate

    @callback(
        Output("annotation-table", "data"),
        Input("annotation-button", "n_clicks"),
        State("carousel", "active_index"),
        State("carousel", "items"),
    )
    def display_annotations(n_clicks, active_index, items):
        if n_clicks:
            target = items[active_index].get("key")
            annotations = controller.get_annotations(items, target)
            return annotations
        else:
            return no_update

    @callback(
        Output("tabs", "active_tab", allow_duplicate=True),
        Input("annotation-button", "n_clicks"),
        prevent_initial_call=True,
    )
    def annotation_button(n_clicks):
        if n_clicks:
            return "image-tab"
        else:
            raise no_update

    @callback(
        Output("tray", "is_open"),
        Input("annotation-button", "n_clicks"),
        State("tray", "is_open"),
    )
    def toggle_tray(n_clicks, is_open):
        if n_clicks:
            return not is_open
        return is_open

    @callback(
        Output("annotation-table", "selected_cells"),
        Output("annotation-table", "active_cell"),
        Input("tray", "is_open"),
    )
    def deselect_annotation(is_open):
        if is_open:
            return [], None
        else:
            raise PreventUpdate

    @callback(
        Output("tabs", "active_tab", allow_duplicate=True),
        Input("tray", "is_open"),
        State("tabs", "active_tab"),
        prevent_initial_call=True,
    )
    def switch_tab(is_open, tab):
        match tab:
            case "image-tab":
                if not is_open:
                    return "carousel-tab"
                else:
                    return no_update
            case _:
                return no_update

    @callback(
        Output("image", "src", allow_duplicate=True),
        Output("image-header", "children", allow_duplicate=True),
        Input("annotation-table", "active_cell"),
        State("annotation-table", "data"),
        State("carousel", "items"),
        prevent_initial_call=True,
    )
    def display_selected_annotation_image(active_cell, data, items):
        if active_cell:
            row = active_cell["row"]
            target = data[row]["key"]
            #rows = controller.get_rows(data, target)
            #box = rows[row]["frag_selector"]
            #src = rows[row]["src"]
            src,box = controller.get_image_details(items, target, row)
            image = controller.get_box(src, box)
            return image, "header 2"
        else:
            raise PreventUpdate

    @callback(
        Output("storage", "data"),
        Input("search-button", "n_clicks"),
        State("search-input", "value"),
        State("manifest-input", "value"),
    )
    def submit_button(n_clicks, search_value, manifest_value):
        if n_clicks and search_value != None and search_value != "":
            data = controller.query(search_value, manifest_value)
            print("storing data")
            return data
        else:
            raise PreventUpdate


    @callback(
        Output("tabs", "active_tab", allow_duplicate=True),
        Output("carousel", "items"),
        Input("storage", "data"),
        prevent_initial_call=True,
    )
    def submit_button_worker(data):
        count = controller.get_image_count(data)
        if count == 0:
            return "status-tab", no_update
        else:
            # we need remove dups in data model
            result = controller.get_carousel_items(data)
            return "carousel-tab", result
