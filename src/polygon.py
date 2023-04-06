import requests
from PIL import Image, ImageDraw


class Polygon:
    def __init__(self, ctx):
        pass

    def load_image(self, url):
        resp = requests.get(url, stream=True).raw
        image = Image.open(resp)
        return image

    def draw_bounding_box_worker(self, image, xywh):
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

    def draw_bounding_box(self, url, xywh):
        image = self.load_image(url)
        bounded_image = self.draw_bounding_box_worker(image, xywh)
        return {"key": "annotated", "src": bounded_image}
