from model import Model
from manifest import Manifest
from annotation import Annotation
from polygon import Polygon
from parse import Parse


class Controller:
    def __init__(self, ctx):
        self.ctx = ctx
        self.model = Model()
        self.annotation = Annotation(ctx)
        self.polygon = Polygon(ctx)
        self.parse = Parse(ctx)
    
    def query(self, search_value, manifest_value):
        manifest_data = self.parse.run(url=manifest_value)
        self.model.load_manifest(manifest_data)
        annotation_data = self.annotation.search(
            url=f"https://miiify.rocks/iiif/content/search?q={search_value}"
        )
        self.model.merge_annotation(annotation_data)
        result = self.model.get_records()
        return result

    def get_image_count(self):
        return self.model.image_count()
    
    def get_annotation_count(self, target):
        return self.model.annotation_count(target)

    def get_annotations(self, key):
        return self.model.filter_on_key(key)

    def get_rows(self, target):
        return self.model.get_rows(target)
       
    # def get_records(self):
    #     return self.model.get_records()
    
    def get_image(self, src):
        return self.polygon.get_image(src)
    
    def get_box(self, url, xywh):
        return self.polygon.draw_bounding_box(url, xywh)