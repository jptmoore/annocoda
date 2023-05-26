import pandas as pd


class Data:
    def __init__(self):
        self.model = None

    def merge_annotation(self, data):
        df = pd.DataFrame(data)
        result = pd.merge(self.model, df, how="left", on=["key"])
        self.model = result

    def load_manifest(self, data):
        self.model = pd.DataFrame(data)

    def count(self):
        result = len(self.model.index)
        return result

    def print(self):
        print(self.model)
