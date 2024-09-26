import cv2

# Tente acessar a webcam do DroidCam (0 ou 1 dependendo do dispositivo)
cap = cv2.VideoCapture(0)  # ou cv2.VideoCapture(1) se necessário

if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

# Carregar o classificador Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()

    if not ret:
        print("Erro ao capturar o frame da câmera.")
        break

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenha um quadrado ao redor de cada rosto detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibe a imagem com os quadrados
    cv2.imshow('Detecção de Rosto', frame)

    # Sai do loop ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
