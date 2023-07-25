
from controller import Controller
from layout import setup_layout
from callback import setup_callbacks

class View:
    def __init__(self, ctx):
        setup_callbacks(Controller(ctx))

    def layout(self):
        return setup_layout()
    

