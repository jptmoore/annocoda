import cv2
import requests
from PIL import Image
import numpy as np

class Polygon:
    def __init__(self, ctx):
        self.image = None

    def load_image(self, url):
        resp = requests.get(url, stream=True).raw
        image = Image.open(resp)
        return image

    def draw_bounding_box_worker(self, image, xywh):
        data = np.asarray(image)
        color = (255, 0, 0)
        left,top,right,bottom = xywh
        label = 'annotated'
        imgHeight, imgWidth, _ = data.shape
        thick = int((imgHeight + imgWidth) // 900)
        cv2.rectangle(data,(left, top), (right, bottom), color, thick)
        cv2.putText(data, label, (left, top - 12), 0, 1e-3 * imgHeight, color, thick//3)
        return Image.fromarray(data)


    def draw_bounding_box(self, url, xywh):
        image = self.load_image(url)
        bounded_image = self.draw_bounding_box_worker(image, xywh)
        return {
             "key": "annotated",
             "src": bounded_image
        }