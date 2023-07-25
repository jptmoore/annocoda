from jsonpath_ng import parse
import dash_bootstrap_components as dbc


class Manifest:
    def __init__(self, ctx):
        self.data = {}
        self.current_targets = []
        self.logger = ctx.logger
        self.session = ctx.session

    def basic_headers(self):
        dict = {}
        return dict

    def get_image_links(self, json):
        try:
            # need to unwrap from array first
            jsonpath_expression = parse("[*].items[*].items[*].items[*].body.id")
            result = [match.value for match in jsonpath_expression.find(json)]
        except Exception as e:
            self.logger.error(f"failed to get image links: {repr(e)}")
            return []
        else:
            return result

    def get_targets(self, json):
        try:
            # need to unwrap from array first
            jsonpath_expression = parse("[*].items[*].items[*].items[*].target")
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

    def manifest_result(self, json):
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


    def load_worker(self, urls):
        acc = []
        for url in urls:
            json = self.get_json(url)
            acc.append(json)
        return acc

    def load(self, urls):
        acc = self.load_worker(urls)
        result = self.manifest_result(acc)
        return result