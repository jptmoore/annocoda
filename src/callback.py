
from dash import callback, State, Input, Output
from search import Search


class Callback:
    def __init__(self, annotation, polygon, ctx):
        self.annotation = annotation
        self.polygon = polygon
        self.search = Search(ctx)


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
                result = self.search.filter_on_key(target)
                #result = self.annotation.filter_result_data([target])
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
                rows = self.search.get_rows(target)
                box = rows[row]['frag_selector']
                src = rows[row]['src']
                image = self.polygon.draw_bounding_box(src, box)
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
            if n_clicks > 0:
                result = self.search.query(value)
                message = f"{self.search.count()} images"
                return result, message
            else:
                return [], None