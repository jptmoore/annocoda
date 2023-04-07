from PIL import Image, ImageDraw

class Polygon:
    def __init__(self, ctx):
        self.session = ctx.session

    def load_image(self, url):
        resp = self.session.get(url, stream=True).raw
        print(f'From cache: {resp}')
        image = Image.open(resp)
        return image
    
    def get_image(self, url):
        image = self.load_image(url)
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
        return bounded_image
