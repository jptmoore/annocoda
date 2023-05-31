from model import Model
from manifest import Manifest
from annotation import Annotation
from polygon import Polygon


class Controller:
    def __init__(self, ctx):
        self.model = Model()
        self.manifest = Manifest(ctx)
        self.annotation = Annotation(ctx)
        self.polygon = Polygon(ctx)
    
    def query(self, value):
        manifest_data = self.manifest.load(urls=["https://miiify.rocks/manifest/diamond_jubilee_of_the_metro", "https://miiify.rocks/manifest/rustic_walking_routes"])
        self.model.load_manifest(manifest_data)
        annotation_data = self.annotation.search(
            url=f"https://miiify.rocks/iiif/content/search?q={value}"
        )
        self.model.merge_annotation(annotation_data)
        result = self.model.get_records()
        return result

    def count(self):
        return self.model.count()

    def filter_on_key(self, key):
        return self.model.filter_on_key(key)

    def get_rows(self, target):
        return self.model.get_rows(target)
       
    def get_records(self):
        return self.model.get_records()
    
    def get_image(self, src):
        return self.polygon.get_image(src)
    
    def draw_bounding_box(self, url, xywh):
        return self.draw_bounding_box(url, xywh)