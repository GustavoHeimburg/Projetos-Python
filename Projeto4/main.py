import cv2
from deepface import DeepFace
from markdown_it.rules_inline import image
from pasta.base.scope import analyze

image = cv2.imread('testefacial.jpg')

resultado = deepface.analyze(image, actions (""))