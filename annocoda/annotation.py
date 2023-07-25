from jsonpath_ng import parse


class Annotation:
    def __init__(self, ctx):
        self.data = {}
        self.logger = ctx.logger
        self.session = ctx.session

    def basic_headers(self):
        dict = {}
        return dict

    def get_items_body_value(self, json):
        try:
            # need to unwrap from array first
            jsonpath_expression = parse("[*].items[*].body.value")
            result = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get annotation text: {repr(e)}")
            return []
        else:
            return result

    def get_items_target(self, json):
        try:
            # need to unwrap from array first
            jsonpath_expression = parse("[*].items[*].target")
            result = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get annotation target: {repr(e)}")
            return []
        else:
            return result

    def make_dict(self, json):
        keys = self.get_items_target(json)
        values = self.get_items_body_value(json)
        dictionary = dict(zip(keys, values))
        self.data = dictionary

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

    def make_result_data(self, data):
        keys = data.keys()
        values = data.values()
        result = map(lambda k,v: {"key": self.remove_frag_selector(k), "value": v, "frag_selector": self.get_frag_selector_cords(k)}, keys,values)      
        return list(result)

    def default(self):
        return []

    def search_result(self, json):
        try:
            self.make_dict(json)
        except Exception as e:
            self.logger.error(f"failed to process json: {repr(e)}")
            return None
        else:
            result = self.make_result_data(self.data)
            return result

    def get_json(self, url):
        headers = self.basic_headers()
        try:
            response = self.session.get(url, headers=headers, verify=False)
        except Exception as e:
            self.logger.error(f"failed to get annotation: {repr(e)}")
            return None
        if response.status_code != 200:
            self.logger.error(f"failed to get annotation")
            return None
        else:
            result = response.json()
            return result

    def search_worker(self, acc, url):
        json = self.get_json(url)
        acc.append(json)
        if "next" in json:
            next = json["next"]
            self.search_worker(acc, next)

    def search(self, url):
        acc = []
        self.search_worker(acc, url)
        result = self.search_result(acc)
        return result
