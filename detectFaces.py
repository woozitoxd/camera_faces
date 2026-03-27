import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#carga el clasificador Haar para detección de caras. Es un modelo de IA entrenado para esto

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Error: no se pudo abrir la cámara. Verifica el dispositivo o el índice (0, 1, ...).')
    cap.release()
    cv2.destroyAllWindows()
    raise SystemExit(1)

while True: # Lee un frame de la cámara
    ret, frame = cap.read()
    if not ret:
        print('Error: no se recibieron frames de la cámara (cap.read() falló).')
        break
    # Convertir el frame a escala de grises para mejorar la detección de caras
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces: # Dibuja un rectángulo alrededor de cada cara detectada
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Deteccion de Caras', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # Libera la cámara
cv2.destroyAllWindows()