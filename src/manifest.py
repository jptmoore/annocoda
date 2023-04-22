import requests
from jsonpath_ng import parse
import dash_bootstrap_components as dbc


class Manifest:
    def __init__(self, ctx):
        self.data = {}
        self.current_targets = []
        self.logger = ctx.logger

    def get_image_links(self, json):
        try:
            jsonpath_expression = parse("items[*].items[*].items[*].body.id")
            result = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get image links: {repr(e)}")
            return []
        else:
            return result

    def get_image_count(self, json):
        return len(self.__get_image_links__(json))

    def get_targets(self, json):
        try:
            jsonpath_expression = parse("items[*].items[*].items[*].target")
            result = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get targets: {repr(e)}")
            return []
        else:
            return result

    def make_dict(self, json):
        keys = self.get_targets(json)
        values = self.get_image_links(json)
        dictionary = dict(zip(keys, values))
        self.data = dictionary

    def carousel_data_template(self, key, value):
        return {
            "key": key,
            "src": value,
            #"img_style": {"height": "10%", "width": "10%"},
        }

    def default(self):
        item = self.carousel_data_template(
            key="splash",
            value="../assets/splash.jpeg",
        )
        return [item]
    
    def nothing_found(self):
        dbc.Alert("This is a primary alert", color="primary")
        item = self.carousel_data_template(
            key="nothing",
            value="../assets/nothing.jpeg",
        )
        return [item]

    def make_result_data(self, data):
        result = []
        for key, value in data.items():
            result.append(self.carousel_data_template(key, value))
        if result == []:
            return self.nothing_found()
        else:
            return result

    def make_target_list(self):
        targets = self.data.keys()
        return targets

    def get_frag_selector_cords_worker(self, frag):
        res = frag.split(',')
        match res: 
            case [_, x, y, w, h]:
                return (x,y,w,h)
            case _:
                raise ValueError("failed to match cords")

    def get_frag_selector_cords(self, target):
        res = target.split('#xywh=')
        match res: 
            case [_, y]:
                result = tuple(map(int, y.split(',')))
                return result
            case [_]:
                return None
            case _:
                raise ValueError("failed to match target")


    def remove_frag_selector(self, target):
        res = target.split("#")
        match res: 
            case [x, _]:
                return x
            case [x]:
                return x
            case _:
                raise ValueError("failed to match target")

    def index_of_target(self, target):
        k = self.remove_frag_selector(target)
        try:
            result = self.current_targets.index(k)
        except ValueError as e:
            self.logger.error(f"failed to find target: {repr(e)}")
            return None        
        return result


    def filter_result_data(self, annotation_targets):
        data = self.data
        filtered_data = dict((k, data[k]) for k in annotation_targets if k in data)
        self.current_targets = list(filtered_data.keys())
        result = self.make_result_data(filtered_data)
        return result

    def load_worker(self, data):
        try:
            json = data.json()
            self.make_dict(json)
        except Exception as e:
            self.logger.error(f"failed to process json: {repr(e)}")
            return None
        else:
            result = self.make_result_data(self.data)
            return result

    def load(self, url):
        try:
            response = requests.get(url, verify=False)
        except Exception as e:
            self.logger.error(f"failed to get manifest: {repr(e)}")
            return None
        if response.status_code != 200:
            self.logger.error(f"failed to get manifest")
            return None
        else:
            result = self.load_worker(response)
            return result
