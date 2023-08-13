import pandas as pd


class Model:
    def __init__(self):
        pass

    def merge_annotation(self, manifest_df, annotation_data):
        # no search matches means empty dataframe
        if annotation_data == []:
            return pd.DataFrame()
        else:
            annotation_df = pd.DataFrame(annotation_data)
            result = pd.merge(manifest_df, annotation_df, how="inner", on=["key"])
            return result

    def get_manifest(self, data):
        return pd.DataFrame.from_records(data)

    def get_annotations(self, data, key):
        model = pd.DataFrame.from_records(data)
        records = model.loc[model["key"] == key, ["key", "value"]]
        result = records.to_dict("records")
        return result

    def get_image_details(self, data, target, row):
        model = pd.DataFrame.from_records(data)
        records = model.loc[model["key"] == target, ["src", "frag_selector"]]
        src = records.iloc[row]['src']
        frag_selector = records.iloc[row]['frag_selector']
        result = (src, frag_selector)
        return result
    
    def get_carousel_items(self, data):
        model = pd.DataFrame.from_records(data)
        df = model.drop_duplicates(subset=["key"])
        result = df[['key', 'src']].to_dict("records")
        return result        

    def get_records(self, model):
        if model.empty:
            return []
        else:
            # df = model.drop_duplicates(subset=["key"])
            # result = df.to_dict('records')
            result = model.to_dict("records")
            return result
