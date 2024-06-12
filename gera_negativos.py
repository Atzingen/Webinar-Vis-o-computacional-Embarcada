import cv2
import time

# cap = cv2.VideoCapture(0)
folder_path = 'datasets/negativos'

for i in range(500):
    # ret, frame = cap.read()
    if i % 5 == 0:
        split = 'test'
    elif i % 3 == 1:
        split = 'valid'
    else:
        split = 'train'
    # cv2.imwrite(f"datasets/potatoes-2/{split}/images/negativos_{i}.png", frame)
    file_path = f"datasets/potatoes-2/{split}/labels/negativos_{i}.txt"
    with open(file_path, 'w') as file:
        pass
    # time.sleep(1)
    print(f"Frame {i} capturado")