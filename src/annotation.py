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
            return result

    def get_items_target(self, json):
        try:
            jsonpath_expression = parse("items[*].target")
            result = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get annotation target: {repr(e)}")
            abort(400)
        else:
            return result

    def make_dict(self, json):
        keys = self.get_items_target(json)
        values = self.get_items_body_value(json)
        dictionary = dict(zip(keys, values))
        self.data = dictionary

    def make_result_data(self):
        values = self.data.values()
        result = map(lambda x: {"result": x}, values)
        return list(result)

    def default(self):
        return []

    def remove_frag_selector(self, target):
        res = target.split("#")
        match res:
            case [x, _]:
                return x
            case [x]:
                return x
            case _:
                raise ValueError("failed to match target")

    def make_target_list(self):
        keys = self.data.keys()
        targets = map(self.remove_frag_selector, keys)
        return targets

    def search_worker(self, data):
        try:
            json = data.json()
            self.make_dict(json)
        except Exception as e:
            self.logger.error(f"failed to process json: {repr(e)}")
            abort(400)
        else:
            result = self.make_result_data()
            return result

    def search(self, url):
        headers = self.basic_headers()
        try:
            response = requests.get(url, verify=False, headers=headers)
        except Exception as e:
            self.logger.error(f"failed to get annotation: {repr(e)}")
            abort(400)
        if response.status_code != 200:
            self.logger.error(f"failed to get annotation")
            abort(response.status_code)
        else:
            result = self.search_worker(response)
            return result
