import cv2
import requests
from PIL import Image

class Polygon:
    def __init__(self, ctx):
        self.image = None

    def load_image(self, url):
        resp = requests.get(url, stream=True).raw
        image = Image.open(resp)
        return image

    def draw_bounding_box_worker(self, image, xywh):
        color = (255, 0, 0)
        left,top,right,bottom = xywh
        label = 'annotated'
        imgHeight, imgWidth, _ = image.shape
        thick = int((imgHeight + imgWidth) // 900)
        cv2.rectangle(image,(left, top), (right, bottom), color, thick)
        cv2.putText(image, label, (left, top - 12), 0, 1e-3 * imgHeight, color, thick//3)
        return image


    def draw_bounding_box(self, url, xywh):
        image = self.load_image(url)
        return {
             "key": "annotated",
             "src": image
        }