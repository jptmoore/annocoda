from data import Data
from manifest import Manifest

class Search:
    def __init__(self, ctx):
        self.dm = ctx.datamodel
        self.manifest = Manifest(ctx)
    
    def run(self):
        collection = self.manifest.load(urls=["https://miiify.rocks/manifest/diamond_jubilee_of_the_metro", "https://miiify.rocks/manifest/rustic_walking_routes"])
        self.dm.load_manifest(collection)
        return self.dm.to_dict()        

    