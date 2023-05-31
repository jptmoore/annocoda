from data import Data
from manifest import Manifest
from annotation import Annotation
from polygon import Polygon


class Search:
    def __init__(self, ctx):
        self.datamodel = Data()
        self.manifest = Manifest(ctx)
        self.annotation = Annotation(ctx)
        self.polygon = Polygon(ctx)
    
    def query(self, value):
        manifest_data = self.manifest.load(urls=["https://miiify.rocks/manifest/diamond_jubilee_of_the_metro", "https://miiify.rocks/manifest/rustic_walking_routes"])
        self.datamodel.load_manifest(manifest_data)
        annotation_data = self.annotation.search(
            url=f"https://miiify.rocks/iiif/content/search?q={value}"
        )
        self.datamodel.merge_annotation(annotation_data)
        result = self.datamodel.get_records()
        return result

    def count(self):
        return self.datamodel.count()

    def filter_on_key(self, key):
        return self.datamodel.filter_on_key(key)

    def get_rows(self, target):
        return self.datamodel.get_rows(target)
       
    def get_records(self):
        return self.datamodel.get_records()
    
    def get_image(self, src):
        return self.polygon.get_image(src)
    
    def draw_bounding_box(self, url, xywh):
        return self.draw_bounding_box(url, xywh)