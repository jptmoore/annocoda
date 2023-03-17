import requests
from flask import abort
from jsonpath_ng import parse


class Manifest:
        
    def __init__(self, ctx):
        self.logger = ctx.logger

    def get_manifest(self, url):
        try:
            response = requests.get(url)
        except Exception as e:
            self.logger.error(f"failed to get manifest: {repr(e)}")
            abort(400)
        if response.status_code != 200:
            self.logger.error(f"failed to get manifest: {repr(e)}")
            abort(response.status_code)
        else:
            content = response.json()
            return content

    def get_image_links(self, json):
        try:
            jsonpath_expression = parse("items[*].items[*].items[*].body.id")
            lis = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get image links: {repr(e)}")
            abort(400)
        else:
            return lis

    def get_image_count(self, json):
        return len(self.__get_image_links__(json))
    

    def get_targets(self, json):
        try:
            jsonpath_expression = parse("items[*].items[*].items[*].target")
            lis = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
             self.logger.error(f"failed to get targets: {repr(e)}")
             abort(400)
        else:
            return lis

    def enumerated_data(self, json):
        manifest_image_links = self.get_image_links(json)
        manifest_targets = self.get_targets(json)
        return enumerate(zip(manifest_image_links, manifest_targets))