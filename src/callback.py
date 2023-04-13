
from dash import callback, State, Input, Output


class Callback:
    def __init__(self, annotation, manifest, polygon):
        self.annotation = annotation
        self.manifest = manifest
        self.polygon = polygon


    def setup_callbacks(self):
        @callback(
            Output("tabs", "active_tab"),
            Output("unbounded-image", "src"),
            Input("offcanvas-scrollable", "is_open"),
            State("carousel", "active_index"),
            State("carousel", "items"),
        )
        def selectTab(is_open, active_index, items):
            if is_open:
                src = items[active_index].get("src")
                image = self.polygon.get_image(src)
                return "tab-2", image
                # item = items[active_index]
                # return "tab-2", [item]
            else:
                return "tab-1", None


        # open tray
        @callback(
            Output("offcanvas-scrollable", "is_open"),
            Output("table", "data"),
            Output("card-1", "children"),
            Input("status-bar", "n_clicks"),
            State("offcanvas-scrollable", "is_open"),
            State("carousel", "active_index"),
            State("carousel", "items"),
        )
        def toggle_offcanvas_scrollable(n_clicks, is_open, active_index, items):
            if n_clicks:
                print(items[active_index])
                target = items[active_index].get("key")
                result = self.annotation.filter_result_data([target])
                return not is_open, result, "test header 1"
            else:
                return is_open, items, None


        @callback(
            Output("table", "selected_cells"),
            Input("offcanvas-scrollable", "is_open"),
        )
        def deselectRows(is_open):
            return []


        @callback(
            Output("carousel", "active_index"),
            Output("table", "active_cell"),
            Output("tabs", "active_tab", allow_duplicate=True),
            Output("bounded-image", "src"),
            Output("card-2", "children"),
            Input("carousel", "items"),
            Input("table", "active_cell"),
            State("table", "data"),
            prevent_initial_call=True,
        )
        def getActiveCell(items, active_cell, data):
            if active_cell:
                row = active_cell["row"]
                target = data[row]["key"]
                box = self.manifest.get_frag_selector_cords(target)
                index = self.manifest.index_of_target(target)
                src = items[index].get("src")
                image = self.polygon.draw_bounding_box(src, box)
                print("box:", box, "src:", src)
                return index, None, "tab-3", image, "test header 2"
            else:
                return 0, active_cell, "tab-1", None, None


        @callback(
            Output("carousel", "items"),
            Output("status-bar", "children"),
            Input("search-button", "n_clicks"),
            State("search-input", "value"),
        )
        def update_output(n_clicks, value):
            if n_clicks > 0:
                annotation_data = self.annotation.search(
                    url=f"https://miiify.rocks/iiif/content/search?q={value}"
                )
                annotation_targets = self.annotation.make_target_list()
                manifest_data = self.manifest.filter_result_data(annotation_targets)
                manifest_targets = self.manifest.make_target_list()
                annotation_data = self.annotation.filter_result_data(manifest_targets)
                count = len(annotation_data)
                message = f"{count} annotations"
                return manifest_data, message
            else:
                return self.manifest.default(), None