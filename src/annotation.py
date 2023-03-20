import requests
from flask import abort
from jsonpath_ng import parse


class Annotation:
        
    def __init__(self, ctx):
        self.logger = ctx.logger
        self.data = {}

    def basic_headers(self):
        dict = {}
        return dict

    def get_items_body_value(self, json):
        try:
            jsonpath_expression = parse("items[*].body.value")
            result = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get annotation text: {repr(e)}")
            abort(400)
        else:
            return list(result)
        
    def get_items_target(self, json):
        try:
            jsonpath_expression = parse("items[*].target")
            result = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get annotation target: {repr(e)}")
            abort(400)
        else:
            return list(result) 
    
    def make_dict(self, json):
        keys = self.get_items_target(json)
        values = self.get_items_body_value(json)
        dictionary = dict(zip(keys, values))
        self.data = dictionary

    def make_table_data(self):
        values = self.data.values()
        result = map(lambda x: {'result': x}, values)
        return list(result)

    def search_worker(self, data):
        try:
            json = data.json()
            self.make_dict(json)
        except Exception as e:
            self.logger.error(f"failed to process json: {repr(e)}")
            abort(400)
        else:
            result = self.make_table_data()
            return result

    def search(self, url):
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
            result = self.search_worker(response)
            return result
