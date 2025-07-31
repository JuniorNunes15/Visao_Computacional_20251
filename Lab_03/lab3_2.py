import cv2
import numpy as np

img = cv2.imread('oguri.png')
b, g, r = cv2.split(img)

gray = 0.3*r + 0.59*g + 0.11*b
gray = np.uint8(gray)

cv2.imwrite('respostas/oguri_cinza.jpg', gray)
cv2.imshow('Cinza Personalizado', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
