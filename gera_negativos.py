import cv2
import time

cap = cv2.VideoCapture(0)
folder_path = 'datasets/negativos'

for i in range(300):
    ret, frame = cap.read()
    cv2.imwrite(f"negativos/{i}.png", frame)
    time.sleep(5)
    print(f"Frame {i} capturado")