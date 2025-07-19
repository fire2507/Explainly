from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # lightweight model

def detect_objects(image_path):
    results = model(image_path)
    names = model.names
    labels = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            labels.append(names[cls])
    return list(set(labels))  # unique objects detected
