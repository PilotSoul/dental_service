import io
from PIL import Image as im
import torch


path_hubconfig = "ultralytics/yolov8"
path_weightfile = "yolo/best.pt"

model = torch.hub.load(path_hubconfig, 'custom',
                       path=path_weightfile, source='local')


def detect_teeth_with_yolo(img):
    results = model(img, size=250)
    results.render()
    for img in results.imgs:
        img_base64 = im.fromarray(img)
        img_base64.save("media/yolo_out/image0.jpg", format="JPEG")

    inference_img = "/media/yolo_out/image0.jpg"
    return inference_img