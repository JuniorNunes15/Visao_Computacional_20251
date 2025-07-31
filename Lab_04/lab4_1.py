import cv2
import numpy as np
import sys

# Carregamento
filename = sys.argv[1]
img = cv2.imread(filename)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 5)

#Detectar placas circulares
circles = cv2.HoughCircles(
    blur, cv2.HOUGH_GRADIENT, dp=1.5, minDist=80,
    param1=120, param2=50, minRadius=42, maxRadius=60
)

img_circles = img_rgb.copy()
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img_circles, (i[0], i[1]), i[2], (0, 255, 0), 10)

#Detectar contornos para quadrados/octógono
edges = cv2.Canny(blur, 100, 200)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_quads = img_rgb.copy()
img_octas = img_rgb.copy()

for cnt in contours:
    epsilon = 0.044 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    area = cv2.contourArea(cnt)
    if area < 1000:
        continue
    if len(approx) == 4:
        cv2.drawContours(img_quads, [approx], 0, (255, 0, 255), 10)
    elif len(approx) == 8:
        cv2.drawContours(img_octas, [approx], 0, (0, 0, 255), 10)


from matplotlib import pyplot as plt

plt.figure(figsize=(12, 8))

plt.subplot(131), plt.imshow(img_circles), plt.title('Placas Circulares')
plt.axis('off')
plt.subplot(132), plt.imshow(img_quads), plt.title('Placas Quadradas')
plt.axis('off')
plt.subplot(133), plt.imshow(img_octas), plt.title('Placas Octogonais')
plt.axis('off')

plt.tight_layout()
plt.show()
