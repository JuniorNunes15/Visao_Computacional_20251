import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randrange

image1 = cv2.imread("imagens/01.jpg")
image2 = cv2.imread("imagens/02.jpg")

#reduz o tamanho das imagens para melhor visualização
h1 = image1.shape[0]
w1 = image1.shape[1]
image1 = cv2.resize(image1, (int(w1*0.2), int(h1*0.2)))

h2 = image2.shape[0]
w2 = image2.shape[1]
image2 = cv2.resize(image2, (int(w2*0.2), int(h2*0.2)) )

img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# find the keypoints and descriptors with SIFT
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)


bf = cv2.BFMatcher()

matches = bf.knnMatch(des1, des2, k=2)
# Apply ratio test

good = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])

if len(good) >= 4:

    # Extrair localizações dos bons matches
    pts1 = []
    pts2 = []
    for m in good:
        pts1.append(kp1[m[0].queryIdx].pt)
        pts2.append(kp2[m[0].trainIdx].pt)

    # matrix points
    points1 = np.float32(pts1).reshape(-1, 1, 2)
    points2 = np.float32(pts2).reshape(-1, 1, 2)

    # Encontrar homografia usando RANSAC
    transformation_matrix, inliers = cv2.findHomography(points1, points2, cv2.RANSAC)

    print(transformation_matrix)
    print(inliers)
else:
    raise AssertionError("No enough keypoints.")

height, width = img1.shape
img1_transformed = cv2.warpPerspective(image1, transformation_matrix, (width, height))

# Criar uma imagem para mostrar a combinação
combined_img = cv2.addWeighted(img1_transformed, 0.5, image2, 0.5, 0)
cv2.imwrite("combined_image.jpg", combined_img)

# Mostrar a imagem combinada
cv2.imshow("Imagem Combinada", combined_img)
cv2.imwrite("resultado.jpg", combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
