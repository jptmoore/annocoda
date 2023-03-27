import dash_bootstrap_components as dbc

def statusbar():
    return dbc.Badge(pill=True, color="primary", className="me-1", id="status-bar")
