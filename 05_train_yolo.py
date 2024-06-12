from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model.train(data="datasets/potatoes-2/data.yaml", 
                      epochs=30, 
                      imgsz=640)