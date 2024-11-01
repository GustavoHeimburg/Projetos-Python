import cv2
from deepface import DeepFace

# Acessa a webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Erro ao capturar o frame da câmera.")
        break

    # Analisa o rosto para idade e emoções
    try:
        analysis = DeepFace.analyze(frame, actions=['age', 'emotion'], enforce_detection=False)

        # Extrai idade e emoção principal
        idade = analysis['age']
        emocao = analysis['dominant_emotion']

        # Adiciona retângulo e texto na imagem
        cv2.putText(frame, f"Idade: {int(idade)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Emoção: {emocao}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    except Exception as e:
        print("Erro na análise:", e)

    # Exibe a imagem com os dados
    cv2.imshow('Análise de Idade e Emoção', frame)

    # Pressione 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
cap.release()
cv2.destroyAllWindows()
