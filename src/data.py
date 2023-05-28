import pandas as pd


class Data:
    def __init__(self):
        self.model = None

    def merge_annotation(self, data):
        df = pd.DataFrame(data)
        result = pd.merge(self.model, df, how="inner", on=["key"])
        self.model = result

    def load_manifest(self, data):
        self.model = pd.DataFrame.from_records(data)

    def count(self):
        result = len(self.model.index)
        return result

    def print(self):
        print(self.model)

    def filter(self, key):
         records = self.model.loc[self.model['key'] == key, ['value']]
         result = records.to_dict('records')
         return result

    def to_dict(self):
        result = self.model.to_dict('records')
        return result
