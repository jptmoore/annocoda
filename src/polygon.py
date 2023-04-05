import cv2
import requests
from PIL import Image
import numpy as np

class Polygon:
    def __init__(self, ctx):
        pass

    def load_image(self, url):
        resp = requests.get(url, stream=True).raw
        image = Image.open(resp)
        return image

    def draw_bounding_box_worker(self, image, xywh):
        data = np.asarray(image)
        color = (255, 0, 0)
        x,y,w,h = xywh
        height, width, _ = data.shape
        thick = int((height + width) // 900)
        cv2.rectangle(data,(x, y), (w, h), color, thick)
        return Image.fromarray(data)


    def draw_bounding_box(self, url, xywh):
        image = self.load_image(url)
        bounded_image = self.draw_bounding_box_worker(image, xywh)
        return {
             "key": "annotated",
             "src": bounded_image
        }