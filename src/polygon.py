import cv2
import numpy as np
import requests


class Polygon:
    def __init__(self, ctx):
        self.image = None

    def load_image(self, url):
        resp = requests.get(url, stream=True).raw
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        self.image = image
        return {
            "key": "loaded",
            "src": self.image,
        }

    def draw_bounding_box(self, xywh):
        image = self.image
        color = (255, 0, 0)
        left,top,right,bottom = xywh
        label = 'annotated'
        imgHeight, imgWidth, _ = image.shape
        thick = int((imgHeight + imgWidth) // 900)
        cv2.rectangle(image,(left, top), (right, bottom), color, thick)
        cv2.putText(image, label, (left, top - 12), 0, 1e-3 * imgHeight, color, thick//3)
        self.image = image

    def get_image(self, xywh):
        self.draw_bounding_box(xywh)
        return {
            "key": "annotated",
            "src": self.image,
        }
