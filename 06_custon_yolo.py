import cv2
import numpy as np
from ultralytics import YOLO
import supervision as sv
from collections import defaultdict

cv2.namedWindow('imagem', cv2.WINDOW_NORMAL)
cv2.resizeWindow('imagem', (1280, 720))
cap = cv2.VideoCapture(0)

# modelos: "yolov8n.pt", "yolov5s.pt", "yolov5m.pt", "yolov5l.pt", "yolov5x.pt"
model = YOLO("models/yolov9c-potato-best.pt")
track_history = defaultdict(lambda: [])

while True:
    ret, frame = cap.read()
    results = model.track(frame, conf=0.1, persist=True)
    # frame = result.plot()
    if results[0].boxes is None or results[0].boxes.id is None:
        frame = cv2.resize(frame, (1280, 720))
        cv2.imshow('imagem', frame)
    else:
        boxes = results[0].boxes.xywh.cpu()
        track_ids = results[0].boxes.id.int().cpu().tolist()
        annotated_frame = results[0].plot()
        for box, track_id in zip(boxes, track_ids):
            x, y, w, h = box
            track = track_history[track_id]
            track.append((float(x), float(y)))
            if len(track) > 30:
                track.pop(0)
            points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
            cv2.polylines(annotated_frame, [points], isClosed=False, color=(230, 0, 0), thickness=3)
        annotated_frame = cv2.resize(annotated_frame, (1280, 720))
        cv2.imshow('imagem', annotated_frame)
    if cv2.waitKey(1) == ord('q') or not ret:
        break
        
cap.release()
cv2.destroyAllWindows()