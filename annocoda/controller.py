from manifest import Manifest
from model import Model
from annotation import Annotation, AnnotationError
from polygon import Polygon
from parse import Parse, ParseError

class Controller:
    def __init__(self, ctx):
        self.ctx = ctx
        self.annotation = Annotation(ctx)
        self.polygon = Polygon(ctx)
        self.model = Model()
        self.parse = Parse(ctx)
    
    def query(self, search_value, manifest_value):
        try:
            data = self.parse.run(url=manifest_value)
        except ParseError as e: return {"error": repr(e)}
        manifest = self.model.get_manifest(data)
        try:
            annotations = self.annotation.search(
                url=f"https://miiify.rocks/iiif/content/search?q={search_value}"
            )
        except AnnotationError as e: return {"error": repr(e)}        
        df = self.model.merge_annotation(manifest, annotations)
        result = self.model.get_records(df)
        return result
    

    def get_carousel_items(self, data):
        return self.model.get_carousel_items(data)

    def get_annotations(self, items, target):
        return self.model.get_annotations(items, target)

    def get_image_details(self, items, target, row):
        return self.model.get_image_details(items, target, row)
    
    def get_image(self, src):
        return self.polygon.get_image(src)
    
    def get_image_with_box(self, url, xywh):
        return self.polygon.get_image_with_box(url, xywh)