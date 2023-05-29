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


    def filter_on_key(self, key):
         records = self.model.loc[self.model['key'] == key, ['key', 'value']]
         result = records.to_dict('records')
         return result

# need to refactor this!

    def get_frag_selector(self, key):
        records = self.model.loc[self.model['key'] == key, ['frag_selector']]
        return records.loc[0]['frag_selector']
    
    def get_src(self, key):
        records = self.model.loc[self.model['key'] == key, ['src']]
        return records.loc[0]['src']    

    def get_records(self):
        df = self.model.drop_duplicates(subset=["key"]) 
        result = df.to_dict('records')
        print(result)
        return result
