from iiif_prezi3 import (
    Manifest,
    ManifestRef,
    CollectionRef,
    Collection,
    Canvas,
    CanvasRef,
    Annotation,
    AnnotationPage,
    ServiceItem
)
from pydantic import Extra, ValidationError
Annotation.Config.extra = Extra.allow

class ParseError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Parse:
    def __init__(self, ctx):
        self.session = ctx.session
        self.data = []

    def __data_template(self, key, value):
        return {"key": key, "src": value}

    def __get_data(self):
        result = []
        for key, value in self.data:
            result.append(self.__data_template(key, value))
        return result

    def __basic_headers(self):
        dict = {}
        return dict

    def __get_json(self, url):
        headers = self.__basic_headers()
        try:
            response = self.session.get(url, headers=headers, verify=False)
        except Exception as e:
            raise ParseError(f"failed to fetch json: {repr(e)}")
        if response.status_code != 200:
            raise ParseError("failed to get a 200 response code")
        else:
            try:
                result = response.json()
            except Exception as e:
                raise ParseError(f"failed to parse json: {repr(e)}")
            else:
                return result

    def __handle_body_as_list(self, target, body):
        for item in body:
            if "value" in item:
                self.data.append((target, item["value"]))

    def __handle_body_as_object(self, target, body):
        self.data.append((target, body.id))


    def __match_annotation(self, x):
        match x:
            case Annotation(target=target, body=body, motivation=motivation) if motivation in ["painting"]:
                if type(body) is list:
                    self.__handle_body_as_list(target, body)
                else:
                    self.__handle_body_as_object(target, body)
            case _:
                raise ParseError("failed to find annotation")


    def __match_annotation_page_items(self, x):
        match x:
            case []:
                pass
            case [*xs]:
                for x in xs:
                    self.__match_annotation(x)
            case _:
                raise ParseError("failed to find annotation page items")

    def __match_annotation_page(self, x):
        match x:
            case AnnotationPage(items=items):
                self.__match_annotation_page_items(items)
            case _:
                raise ParseError("failed to find annotation")

    def __match_canvas_items(self, x):
        match x:
            case []:
                pass
            case [*xs]:
                for x in xs:
                    self.__match_annotation_page(x)
            case _:
                raise ParseError("failed to find annotations")

    def __get_canvas_content(self, url):
        json = self.__get_json(url)
        cc = Canvas(**json)
        return cc

    def __match_manifest_item(self, x):
        match x:
            case Canvas(items=items):
                self.__match_canvas_items(items)
            case CanvasRef(id=id):
                cc = self.__get_canvas_content(id)
                self.__match_manifest_item(cc)
            case _:
                raise ParseError("failed to find canvas annotations")

    def __get_collection_content(self, url):
        json = self.__get_json(url)
        collection = Collection(**json)
        return collection

    def __get_manifest_content(self, url):
        json = self.__get_json(url)
        manifest = Manifest(**json)
        return manifest

    def __match_collection_item(self, x):
        match x:
            case ManifestRef(id=id):
                manifest = self.__get_manifest_content(id)
                self.__match_collection_item(manifest)
            case Manifest(id=id):
                self.__match_manifest(x)
            case CollectionRef(id=id):
                collection = self.__get_collection_content(id)
                self.__match_collection_item(collection)
            case Collection(id=id):
                self.__match_collection(x)
            case _:
                raise ParseError(
                    "only supports Manifest, ManifestRef", "CollectionRef", "Collection"
                )

    def __match_manifest(self, x):
        match x:
            case Manifest(items=items):
                for item in items:
                    self.__match_manifest_item(item)
            case _:
                raise ParseError("failed to find manifest items")

    def __match_collection(self, x):
        match x:
            case Collection(items=items):
                for item in items:
                    self.__match_collection_item(item)
            case _:
                raise ParseError("failed to find collection items")


    def __match_service_item(self, x):
        match x:
            case ServiceItem(id=id, type='SearchService2'):
                return id
            case _:
                return None


    def __match_service(self, x):
        result = []
        match x.service:
            case [*xs]:
                for x in xs:
                    service = self.__match_service_item(x)
                    if service != None: result.append(service)
            case _:
                raise ParseError("requires a v2 search service defined at manifest or collection level")
        match result:
            case [x]:
                return x
            case [*xs]:
                raise ParseError("only supports a single v2 search service per manifest or collection")


    def __run_collection(self, json):
        collection = Collection(**json)
        search_service = self.__match_service(collection)
        self.__match_collection(collection)
        return search_service

    def __run_manifest(self, json):
        manifest = Manifest(**json)
        search_service = self.__match_service(manifest)
        self.__match_manifest(manifest)
        return search_service

    def __run_worker(self, url):
        self.data = []
        json = self.__get_json(url)
        match json["type"]:
            case "Collection":
                return self.__run_collection(json)
            case "Manifest":
                return self.__run_manifest(json)
            case _:
                raise ParseError("failed to find collection or manifest")


    def run(self, url: str) -> (str, list[dict]):
        search_service = self.__run_worker(url)
        data = self.__get_data()
        return search_service, data

# p = Parse(ctx)
# result = p.run(url="https://miiify.rocks/manifest/diamond_jubilee_of_the_metro")
# print(result)

