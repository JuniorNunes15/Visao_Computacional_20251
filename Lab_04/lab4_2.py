import cv2
import numpy as np
from matplotlib import pyplot as plt
from pyzbar.pyzbar import decode

img = cv2.imread("imagens/barcode-code-128.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200, apertureSize=3)

lines = cv2.HoughLines(edges, 1, np.pi / 180, 150)

img_lines = img.copy()
if lines is not None:
    for r_theta in lines:
        rho, theta = r_theta[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img_lines, (x1, y1), (x2, y2), (0, 0, 255), 1)

# Leitura do código com pyzbar
decoded_objects = decode(img)
codigo_lido = decoded_objects[0].data.decode('utf-8') if decoded_objects else 'Não lido'

plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(cv2.cvtColor(img_lines, cv2.COLOR_BGR2RGB)), plt.title('Linhas detectadas')
plt.axis('off')
plt.subplot(122), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title(f'Código lido: {codigo_lido}')
plt.axis('off')
plt.tight_layout()
plt.show()
