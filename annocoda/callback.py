from dash import callback, State, Input, Output
from dash import no_update
from dash.exceptions import PreventUpdate


def setup_callbacks(controller):

    @callback(
        Output("annotation-table", "data"),
        Input("annotation-button", "n_clicks"),
        State("carousel", "active_index"),
        State("carousel", "items"),
        State("storage", "data"),
    )
    def display_annotations(n_clicks, active_index, items, storage_data):
        if n_clicks:
            target = items[active_index].get("key")
            annotations = controller.get_annotations(storage_data, target)
            return annotations
        else:
            raise PreventUpdate

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
                    raise PreventUpdate
            case _:
                raise PreventUpdate

    @callback(
        Output("image", "src", allow_duplicate=True),
        Output("tabs", "active_tab", allow_duplicate=True),
        Output("status-message", "children", allow_duplicate=True),
        Input("annotation-table", "active_cell"),
        State("annotation-table", "data"),
        State("storage", "data"),
        prevent_initial_call=True,
    )
    def display_selected_annotation_image(active_cell, table_data, storage_data):
        if active_cell:
            row = active_cell["row"]
            target = table_data[row]["key"]
            src,frag_selector = controller.get_image_details(storage_data, target, row)
            if frag_selector == None:
                raise PreventUpdate
            else:
                image = controller.get_image_with_box(src, frag_selector)
                if image == None:
                    return image, "status-tab", "failed to load image"
                else:
                    return image, "image-tab", no_update
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
            result = controller.query(search_value, manifest_value)
            return result
        else:
            raise PreventUpdate


    @callback(
        Output("tabs", "active_tab", allow_duplicate=True),
        Output("status-message", "children"),
        Output("carousel", "items"),
        Input("storage", "data"),
        prevent_initial_call=True,
    )
    def submit_button_worker(storage_data):
        match storage_data:
            case {'error': message}:
                return "status-tab", message, no_update
            case []:
                return "status-tab", "The keywords you supplied did not provide any matches", no_update
            case [_, *_]:
                result = controller.get_carousel_items(storage_data)
                return "carousel-tab", no_update, result
