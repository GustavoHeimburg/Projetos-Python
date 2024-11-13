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

    try:

        analysis = DeepFace.analyze(frame, actions=['age', 'emotion'], enforce_detection=False)

        if isinstance(analysis, dict) and 'age' in analysis and 'dominant_emotion' in analysis:
            idade = analysis['age']
            emocao = analysis['dominant_emotion']

            cv2.putText(frame, f"Idade: {int(idade)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Emoção: {emocao}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            print("Nenhum rosto detectado ou múltiplos rostos na imagem.")

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
