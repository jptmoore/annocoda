from data import Data
from manifest import Manifest
from annotation import Annotation

class Search:
    def __init__(self, ctx):
        self.datamodel = ctx.datamodel
        self.manifest = Manifest(ctx)
        self.annotation = Annotation(ctx)
    
    def query(self, value):
        manifest_data = self.manifest.load(urls=["https://miiify.rocks/manifest/diamond_jubilee_of_the_metro", "https://miiify.rocks/manifest/rustic_walking_routes"])
        self.datamodel.load_manifest(manifest_data)
        annotation_data = self.annotation.search(
            url=f"https://miiify.rocks/iiif/content/search?q={value}"
        )
        self.datamodel.merge_annotation(annotation_data)
        result = self.datamodel.to_dict()
        print(self.datamodel.print())
        return result

    def count(self):
        result = self.datamodel.count()
        return result      

    