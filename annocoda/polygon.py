from PIL import Image, ImageDraw

class PolygonError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Polygon:
    def __init__(self, ctx):
        self.session = ctx.session
        self.logger = ctx.logger

    def load_image(self, url):
        try:
            resp = self.session.get(url, stream=True, verify=False).raw
            image = Image.open(resp)
        except Exception as e:
            raise PolygonError(f"failed to load image: {repr(e)}")
        return image
    
    def get_image(self, url):
        image = self.load_image(url)
        return image

    def __get_image_with_box_worker(self, image, xywh):
        x, y, w, h = xywh
        draw = ImageDraw.Draw(image)
        padding = 10
        draw.rectangle(
            (x - padding, y - padding, x + w + padding, y + h + padding),
            fill=None,
            outline=(0, 0, 255),
            width=5,
        )
        return image

    def get_image_with_box(self, url, xywh):
        image = self.load_image(url)
        bounded_image = self.__get_image_with_box_worker(image, xywh)
        return bounded_image
