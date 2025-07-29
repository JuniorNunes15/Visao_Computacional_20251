import cv2
import numpy as np

head = cv2.imread('imagens/circle.jpg', cv2.IMREAD_GRAYSCALE)
line = cv2.imread('imagens/line.jpg', cv2.IMREAD_GRAYSCALE)

# Inverte os tons (fundo branco → preto, forma preta → branca)
head = cv2.bitwise_not(head)
line = cv2.bitwise_not(line)

# Binariza para garantir fundo preto e forma branca
_, head = cv2.threshold(head, 127, 255, cv2.THRESH_BINARY)
_, line = cv2.threshold(line, 127, 255, cv2.THRESH_BINARY)

# Cria o canvas preto de 300x300
canvas = np.zeros((300, 300), dtype=np.uint8)

# Cabeça
h_h, w_h = head.shape
x_h = 150 - w_h // 2
y_h = 40
canvas[y_h:y_h+h_h, x_h:x_h+w_h] = cv2.bitwise_or(canvas[y_h:y_h+h_h, x_h:x_h+w_h], head)
y_h = 22

# Tronco
tronco = cv2.rotate(line, cv2.ROTATE_90_CLOCKWISE)
h_t, w_t = tronco.shape
x_t = 146 - w_t // 2
yt = y_h + h_h - 20
y_t = y_h + h_h
canvas[yt:yt+h_t, x_t:x_t+w_t] = cv2.bitwise_or(canvas[yt:yt+h_t, x_t:x_t+w_t], tronco)

# Braços
arm_length = int(0.75 * h_t)
arm = cv2.resize(line, (w_t, arm_length), interpolation=cv2.INTER_NEAREST)

# Rotações dos braços
arm_left = cv2.warpAffine(arm, cv2.getRotationMatrix2D((w_t//2, arm_length//2), 45, 1), (w_t, arm_length))
arm_right = cv2.warpAffine(arm, cv2.getRotationMatrix2D((w_t//2, arm_length//2), -45, 1), (w_t, arm_length))

# Posiciona os braços
def place_on_canvas(part, center_x, center_y):
    h, w = part.shape
    x = center_x - w // 2
    y = center_y - h // 2
    # Recorte seguro para evitar sair da borda
    y1, y2 = max(0, y), min(canvas.shape[0], y + h)
    x1, x2 = max(0, x), min(canvas.shape[1], x + w)
    part_crop = part[y1 - y:y2 - y, x1 - x:x2 - x]
    canvas[y1:y2, x1:x2] = cv2.bitwise_or(canvas[y1:y2, x1:x2], part_crop)

place_on_canvas(arm_left, 150 - 35, y_t + 35)
place_on_canvas(arm_right, 150 + 28, y_t + 35)

# Pernas
leg_length = int(2 * arm_length)
leg = cv2.resize(line, (w_t, leg_length), interpolation=cv2.INTER_NEAREST)

leg_left = cv2.warpAffine(leg, cv2.getRotationMatrix2D((w_t//2, leg_length//2), 45, 1), (w_t, leg_length))
leg_right = cv2.warpAffine(leg, cv2.getRotationMatrix2D((w_t//2, leg_length//2), -45, 1), (w_t, leg_length))

place_on_canvas(leg_left, 150 - 30, y_t + h_t)
place_on_canvas(leg_right, 150 + 25, y_t + h_t)

#Exibe resultado
cv2.imwrite('boneco_palito.jpg', canvas)
cv2.imshow("Boneco Palito", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
