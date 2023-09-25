from model import Model
from annotation_search import AnnotationSearch, AnnotationSearchError
from polygon import Polygon, PolygonError
from parse import Parse, ParseError
from pydantic import ValidationError
from highlight import Highlight

class Controller:
    def __init__(self, ctx):
        self.ctx = ctx
        self.model = Model()
    
    def query(self, search_value, manifest_value):
        try:
            annotation_search = AnnotationSearch(self.ctx)
            parse = Parse(self.ctx)
            search_service, data = parse.run(url=manifest_value)
            manifest = self.model.get_manifest(data)
            annotations = annotation_search.run(
                url=f"{search_service}?q={search_value}"
            )
            df = self.model.merge_annotation(manifest, annotations)
            result = self.model.get_records(df)
        except Exception as e:
            return {"error": repr(e)}        
        return result
    

    def get_carousel_items(self, data):
        return self.model.get_carousel_items(data)

    def get_annotations(self, items, target):
        return self.model.get_annotations(items, target)

    def get_image_details(self, items, target, row):
        return self.model.get_image_details(items, target, row)
    
    def get_image_with_box(self, url, xywh):
        try:
            polygon = Polygon(self.ctx)
            result = polygon.get_image_with_box(url, xywh)
        except Exception as e: 
            return None
        return result
    
    def highlight_annotations(self, search_value, annotations):
        highlight = Highlight()
        return highlight.run(search_value, annotations)