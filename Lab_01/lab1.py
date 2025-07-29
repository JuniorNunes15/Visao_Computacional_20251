import cv2
import numpy as np

# Carregar a imagem
img = cv2.imread("gamora_nebula.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Máscara para tons de azul
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# Máscara para tons de verde
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Trocar azul por verde
img[mask_blue > 0] = [0, 255, 0]  # BGR: verde

# Trocar verde por azul
img[mask_green > 0] = [255, 0, 0]  # BGR: azul

cv2.imwrite('resultado.jpg', img)
cv2.imshow("Troca de Cores", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
