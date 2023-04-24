from ultralytics import YOLO
from os import path
import shutil

path_weightfile = ""
path_to_media = ""
destination_path = ""
saved_recognized_path = ""
model = YOLO(path_weightfile)


def change_yolo_output_path(uploaded_img_path:str) -> str:
    new_location = ""
    source_path = saved_recognized_path + uploaded_img_path.split("/")[-1]
    if path.exists(source_path):
        new_location = shutil.move(source_path, destination_path)
    shutil.rmtree(saved_recognized_path)
    return new_location


def detect_teeth_with_yolo(img_path: str) -> bool:
    full_path = path_to_media + img_path
    try:
        model.predict(full_path, save=True, imgsz=250, conf=0.7)
    except Exception as e:
        print(f"ERROR: {e}")
        return False
    if change_yolo_output_path(img_path):
        return True
    return False
