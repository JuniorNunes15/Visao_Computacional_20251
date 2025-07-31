import cv2
import time
import os
import numpy as np
import matplotlib.pyplot as plt

# Carrega classificador HaarCascade para rosto frontal
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Caminho da imagem base (troque pelo seu arquivo)
imagem_original = cv2.imread("images/oscar.jpg")  # substitua pelo nome da sua imagem
if imagem_original is None:
    raise FileNotFoundError("Imagem não encontrada.")

# Resoluções a serem testadas
resolucoes = [
    (320, 240),
    (640, 480),
    (800, 600),
    (1280, 720),
    (1920, 1080)
]

# Armazena tempos de execução
resultados = []

# Loop sobre resoluções
for largura, altura in resolucoes:
    img = cv2.resize(imagem_original, (largura, altura))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Inicia contagem de tempo
    inicio = time.time()
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    fim = time.time()

    tempo = fim - inicio
    resultados.append((f"{largura}x{altura}", tempo, len(faces)))

    # Desenha rostos
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostra imagem redimensionada com rostos detectados
    cv2.imwrite(f"resultado_{largura}x{altura}.jpg", img)
    cv2.imshow(f"Resolução: {largura}x{altura}", img)
    cv2.waitKey(1000)  # espera 1 segundo por imagem
    cv2.destroyAllWindows()

# Mostra a tabela com os tempos
print("\nTabela de Execução:")
print(f"{'Resolução':<12} | {'Tempo (s)':>10} | {'Rostos':>7}")
print("-" * 36)
for res, tempo, n_faces in resultados:
    print(f"{res:<12} | {tempo:>10.4f} | {n_faces:>7}")
