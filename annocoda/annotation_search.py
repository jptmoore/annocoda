from iiif_prezi3 import (
    Annotation,
    AnnotationPage,
    AnnotationPageRef,
)

class AnnotationSearchError(Exception):
    def __init__(self, message):
        super().__init__(message)


class AnnotationSearch:
    def __init__(self, ctx):
        self.data = {}
        self.logger = ctx.logger
        self.session = ctx.session
        self.data = []

    def basic_headers(self):
        dict = {}
        return dict

    def get_frag_selector_cords(self, target):
        res = target.split("#xywh=")
        match res:
            case [_, y]:
                result = tuple(map(int, y.split(",")))
                return result
            case [_]:
                return None
            case _:
                raise AnnotationSearchError("failed to match target")

    def remove_frag_selector(self, target):
        res = target.split("#")
        match res:
            case [x, _]:
                return x
            case [x]:
                return x
            case _:
                raise AnnotationSearchError("failed to match target")

    def make_result(self, xs):
        result = map(
            lambda tup: {
                "key": self.remove_frag_selector(tup[0]),
                "value": tup[1],
                "frag_selector": self.get_frag_selector_cords(tup[0]),
            },
            xs,
        )
        return list(result)

    def __get_json(self, url):
        headers = self.basic_headers()
        try:
            response = self.session.get(url, headers=headers, verify=False)
        except Exception as e:
            raise AnnotationSearchError(f"failed to get annotation: {repr(e)}")
        if response.status_code != 200:
            raise AnnotationSearchError(f"failed to get annotation")
        else:
            try:
                result = response.json()
            except Exception as e:
                raise AnnotationSearchError(f"failed to parse json: {repr(e)}")
            else:
                return result

    def __handle_body_as_list(self, target, body):
        for item in body:
            if "value" in item:
                self.data.append((target, item["value"]))

    def __handle_body_as_object(self, target, body):
        self.data.append((target, body.value))

    def __match_w3c_annotation_item(self, x):
        match x:
            case Annotation(
                target=target, body=body, motivation=motivation
            ) if motivation in [
                "commenting",
                "supplementing",
                "tagging",
            ]:
                if type(body) is list:
                    self.__handle_body_as_list(target, body)
                else:
                    self.__handle_body_as_object(target, body)
            case _:
                raise AnnotationSearchError("failed to find annotation")

    def __match_wc3_annotations(self, x):
        match x:
            case []:
                raise AnnotationSearchError("no W3C annotations to process")
            case [*xs]:
                for x in xs:
                    self.__match_w3c_annotation_item(x)

    def __get_annotation_page_content(self, url):
        json = self.__get_json(url)
        try:
            ap = AnnotationPage(**json)
        except AnnotationSearchError:
            raise AnnotationSearchError("Could not validate AnnotationPage")
        return ap

    def __match_annotation_content_item(self, x):
        match x:
            case AnnotationPage(id=id, type="AnnotationPage", items=items):
                match items:
                    case []:
                        pass
                    case [*xs]:
                        self.__match_wc3_annotations(xs)
            case AnnotationPageRef(id=id):
                ap = self.__get_annotation_page_content(id)
                self.__match_annotation_content_item(ap)
            case _:
                raise AnnotationSearchError("failed to find annotation page")

    def run_worker(self, url):
        json = self.__get_json(url)
        ap = AnnotationPage(**json)
        self.__match_annotation_content_item(ap)
        if "next" in json:
            next = json["next"]
            self.run_worker(next)

    def run(self, url):
        self.run_worker(url)
        result = self.make_result(self.data)
        return result


# a = AnnotationSearch()
# res = a.search(url="https://miiify.rocks/iiif/content/search?q=eastcote")
# print(res)
