import cv2
from ultralytics import YOLO
import supervision as sv

import cv2

cv2.namedWindow('imagem', cv2.WINDOW_NORMAL)
cv2.resizeWindow('imagem', (1280, 720))
vid = cv2.VideoCapture(0)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# modelos: "yolov8n.pt", "yolov5s.pt", "yolov5m.pt", "yolov5l.pt", "yolov5x.pt"
model = YOLO("models/yolo_batata.pt")

# box_annotator = sv.BoxAnnotator(
#     thickness=2,
#     text_thickness=2,
#     text_scale=1
# )

while True:
    ret, frame = cap.read()
    result = model(frame, agnostic_nms=True)[0]
    frame = result.plot()
    # detections = sv.Detections.from_yolov8(result)
    # labels = [
    #     f"{model.model.names[class_id]} {confidence:0.2f}"
    #     for _, _, confidence, class_id, _
    #     in detections
    # ]
    # frame = box_annotator.annotate(
    #     scene=frame, 
    #     detections=detections, 
    #     labels=labels
    # ) 
    
    cv2.imshow("imagem", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()