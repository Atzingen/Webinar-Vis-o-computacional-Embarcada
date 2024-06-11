import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics import YOLOWorld

cv2.namedWindow('imagem', cv2.WINDOW_NORMAL)
cv2.resizeWindow('imagem', (1280, 720))
vid = cv2.VideoCapture(0)

# modelos: "yolov8n.pt", "yolov5s.pt", "yolov5m.pt"
# model = YOLO("models/yolo_batata.pt")
model = YOLO("models/yolov8m.pt")
# model = YOLOWorld("yolov8s-world.pt")
# model.set_classes(["remote controller", "controller"])


while True:
    ret, frame = vid.read()
    results = model.track(frame, conf=0.1, persist=True)
    frame = results[0].plot()
    cv2.imshow('imagem', frame)
    if cv2.waitKey(1) == ord('q') or not ret:
        break
        
vid.release()
cv2.destroyAllWindows()