import requests
from flask import abort
from jsonpath_ng import parse


class Annotation:
        
    def __init__(self, ctx):
        self.logger = ctx.logger

    def basic_headers(self):
        dict = {}
        return dict

    def get_items_body_value(self, json):
        try:
            jsonpath_expression = parse("items[*].body.value")
            lis = [match.value for match in jsonpath_expression.find(json)]
            res_lis = map(lambda x: {'result': x}, lis)
        except Exception as e:
            self.logger.error(f"failed to get annotation text: {repr(e)}")
            abort(400)
        else:
            return list(res_lis)


    def parse(self, data):
        try:
            json = data.json()
            annotations = self.get_items_body_value(json)
        except Exception as e:
            self.logger.error(f"failed to convert to json: {repr(e)}")
            abort(400)
        else:
            return annotations

    def get_annotation(self, url):
        headers = self.basic_headers()
        try:
            response = requests.get(url, verify=False, headers=headers)
        except Exception as e:
            self.logger.error(f"failed to get annotation: {repr(e)}")
            abort(400)
        if response.status_code != 200:
            self.logger.error(f"failed to get annotation: {repr(e)}")
            abort(response.status_code)
        else:
            content = self.parse(response)
            return content
