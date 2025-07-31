import cv2
import time
import os

# Carregamento dos classificadores HaarCascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")  # Não há "mouth", "smile" é o mais próximo

# Lista de resoluções a testar
resolucoes = [
    (320, 240),
    (640, 480),
    (800, 600),
    (1280, 720)
]

# Lista de imagens para teste (você precisa ajustar com os arquivos reais)
imagens = [
    "images/oscar.jpg"
]

# Verifica se arquivos existem
for img_path in imagens:
    if not os.path.exists(img_path):
        print(f"[AVISO] Imagem não encontrada: {img_path}")

# Executar detecção em cada imagem e resolução
for imagem_nome in imagens:
    if not os.path.exists(imagem_nome):
        continue

    print(f"\n>> Imagem: {imagem_nome}")
    original = cv2.imread(imagem_nome)

    for largura, altura in resolucoes:
        img = cv2.resize(original, (largura, altura))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Início do cronômetro
        inicio = time.time()
        rostos = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        tempo_rostos = time.time() - inicio

        # Marcação dos rostos e partes
        for (x, y, w, h) in rostos:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            # Rosto
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Olhos
            olhos = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)
            olhos = sorted(olhos, key=lambda e: e[0])  # ordenar por X (esquerda → direita)
            for i, (ex, ey, ew, eh) in enumerate(olhos[:2]):
                color = (255, 0, 0) if i == 0 else (255, 255, 0)  # azul = olho direito, ciano = olho esquerdo
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), color, 2)

            # Boca (usando smile como aproximação)
            boca = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
            for (mx, my, mw, mh) in boca:
                if my > h // 2:  # apenas boca inferior (evita confusão com olhos)
                    cv2.rectangle(roi_color, (mx, my), (mx+mw, my+mh), (0, 0, 255), 2)
                    break

        # Mostra resultado
        label = f"{imagem_nome} - {largura}x{altura} - Tempo: {tempo_rostos:.4f}s"
        print(label)
        cv2.imwrite(f"resultado_{largura}x{altura}_{os.path.basename(imagem_nome)}", img)
        cv2.imshow(label, img)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
