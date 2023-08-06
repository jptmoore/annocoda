from manifest import Manifest
from model import Model
from annotation import Annotation
from polygon import Polygon
from parse import Parse

class Controller:
    def __init__(self, ctx):
        self.ctx = ctx
        self.annotation = Annotation(ctx)
        self.polygon = Polygon(ctx)
        self.model = Model()
        self.parse = Parse(ctx)
    
    def query(self, search_value, manifest_value):
        manifest_data = self.parse.run(url=manifest_value)
        manifest_df = self.model.load_manifest(manifest_data)
        annotation_data = self.annotation.search(
            url=f"https://miiify.rocks/iiif/content/search?q={search_value}"
        )
        result_df = self.model.merge_annotation(manifest_df, annotation_data)
        result = self.model.get_records(result_df)
        return result

    def get_image_count(self, items):
        return len(items)
        #return self.model.image_count(items)
    
    def get_annotation_count(self, items, target):
        return self.model.annotation_count(items, target)

    def get_annotations(self, items, target):
        return self.model.filter_annotations(items, target)
        #return self.model.filter_on_key(items, key)

    def get_image_details(self, items, target, index):
        return self.model.filter_image_details(items, target, index)
        #return self.model.filter_on_key(items, key)

    def get_rows(self, items, target):
        return self.model.get_rows(items, target)
       
    # def get_records(self):
    #     return model.get_records()
    
    def get_image(self, src):
        return self.polygon.get_image(src)
    
    def get_box(self, url, xywh):
        return self.polygon.draw_bounding_box(url, xywh)