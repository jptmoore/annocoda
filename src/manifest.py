import requests
from flask import abort
from jsonpath_ng import parse


class Manifest:
    def __init__(self, ctx):
        self.logger = ctx.logger
        self.data = {}

    def get_image_links(self, json):
        try:
            jsonpath_expression = parse("items[*].items[*].items[*].body.id")
            result = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get image links: {repr(e)}")
            abort(400)
        else:
            return list(result)

    def get_image_count(self, json):
        return len(self.__get_image_links__(json))

    def get_targets(self, json):
        try:
            jsonpath_expression = parse("items[*].items[*].items[*].target")
            result = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get targets: {repr(e)}")
            abort(400)
        else:
            return list(result)

    def make_dict(self, json):
        keys = self.get_targets(json)
        values = self.get_image_links(json)
        dictionary = dict(zip(keys, values))
        self.data = dictionary

    def carousel_data_template(self, key, value):
        return {
            "key": key,
            "src": value,
            "img_style": {"height": "10%", "width": "10%"},
        }

    def make_carousel_data(self, data):
        result = []
        for key, value in data.items():
            result.append(self.carousel_data_template(key, value))
        return result

    def default(self):
        item = self.carousel_data_template(
            key="logo",
            value="../assets/annocoda-high-resolution-logo-color-on-transparent-background.png",
        )
        return [item]

    def load_worker(self, data):
        try:
            json = data.json()
            self.make_dict(json)
        except Exception as e:
            self.logger.error(f"failed to process json: {repr(e)}")
            abort(400)
        else:
            result = self.make_carousel_data(self.data)
            return result



    def filter(self, annotation):
        dict1 = self.data
        dict2 = annotation.data
        res_dict = {i: dict1[i] for i in set(dict1.keys()).intersection(set(dict2.keys()))}
        result = self.make_carousel_data(res_dict)
        return result



    def load(self, url):
        try:
            response = requests.get(url, verify=False)
        except Exception as e:
            self.logger.error(f"failed to get manifest: {repr(e)}")
            abort(400)
        if response.status_code != 200:
            self.logger.error(f"failed to get manifest")
            abort(response.status_code)
        else:
            result = self.load_worker(response)
            return result
