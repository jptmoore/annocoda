
from dash import callback, State, Input, Output
from controller import Controller
from layout import layout

class View:
    def __init__(self, ctx):
        self.controller = Controller(ctx)
        self.callbacks()

    def layout(self):
        return layout

    def callbacks(self):
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
                image = self.controller.polygon.get_image(src)
                return "tab-2", image
                # item = items[active_index]
                # return "tab-2", [item]
            else:
                return "tab-1", None


        # open tray
        @callback(
            Output("offcanvas-scrollable", "is_open"),
            Output("carousel", "active_index"),
            Output("table", "data"),
            Output("card-1", "children"),
            Input("status-bar", "n_clicks"),
            State("offcanvas-scrollable", "is_open"),
            State("carousel", "active_index"),
            State("carousel", "items"),
        )
        def toggle_offcanvas_scrollable(n_clicks, is_open, active_index, items):
            if n_clicks:
                target = items[active_index].get("key")
                result = self.controller.get_annotations(target)
                return not is_open, active_index, result, "test header 1"
            else:
                return is_open, 0, items, None


        @callback(
            Output("table", "selected_cells"),
            Input("offcanvas-scrollable", "is_open"),
        )
        def deselectRows(is_open):
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
        def getActiveCell(active_cell, data):
            if active_cell:
                row = active_cell["row"]
                target = data[row]["key"]
                rows = self.controller.get_rows(target)
                box = rows[row]['frag_selector']
                src = rows[row]['src']
                image = self.controller.get_box(src, box)
                return None, "tab-3", image, "test header 2"
            else:
                return active_cell, "tab-1", None, None


        @callback(
            Output("carousel", "items"),
            Output("status-bar", "children"),
            Input("search-button", "n_clicks"),
            State("search-input", "value"),
        )
        def search(n_clicks, value):
            if n_clicks > 0 and value != None:
                result = self.controller.query(value)
                message = f"{self.controller.get_image_count()} images"
                return result, message
            else:
                return [], None