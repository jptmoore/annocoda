import pandas as pd


class Model:
    def __init__(self):
        self.model = None

    def merge_annotation(self, data):
        df = pd.DataFrame(data)
        result = pd.merge(self.model, df, how="inner", on=["key"])
        self.model = result

    def load_manifest(self, data):
        self.model = pd.DataFrame.from_records(data)

    def count(self):
        df = self.model.drop_duplicates(subset=["key"]) 
        result = len(df.index)
        return result

    def print(self):
        print(self.model)


    def filter_on_key(self, key):
         records = self.model.loc[self.model['key'] == key, ['key', 'value']]
         result = records.to_dict('records')
         return result

    def get_rows(self, target):
        records = self.model.loc[self.model['key'] == target]
        result = records.to_dict('records')
        return result
       

    def get_records(self):
        df = self.model.drop_duplicates(subset=["key"]) 
        result = df.to_dict('records')
        return result
    

