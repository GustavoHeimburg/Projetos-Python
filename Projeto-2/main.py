import cv2
from deepface import DeepFace

image = cv2.imread("testefacial.jpeg")

resultado =  DeepFace.analyze(image, actions=("age", "race", "emotion"))

print(resultado)
