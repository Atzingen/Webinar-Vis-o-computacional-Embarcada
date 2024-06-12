import cv2

# resolução alterada para caber na apresentação
# Altere (600, 400) para um valor adequado a sua tela e webcam.
cv2.namedWindow('imagem', cv2.WINDOW_NORMAL)
cv2.resizeWindow('imagem', (1280, 720)) 

vid = cv2.VideoCapture(0)
print("Iniciando webcam... \n aperte 'q' para sair \n ")

while True:
    _, frame1 = vid.read()
    _, frame2 = vid.read()

    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame = cv2.subtract(gray1, gray2)

    cv2.imshow('imagem', frame)     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()