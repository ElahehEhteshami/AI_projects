import cv2
import numpy as np
import matplotlib.pyplot as plt

# A
img_color = cv2.imread("Screenshot from 2025-04-16 07-45-42.png")
gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

bit_planes = []
plt.figure(figsize=(14, 6))
for i in range(8):
    bit_plane = (gray >> i) & 1
    bit_planes.append(bit_plane)
    bit_plane = bit_plane * 255 // (1 << i)

    plt.subplot(2, 4, i+1)
    plt.imshow(bit_plane, cmap='gray')
    plt.title(f'Bit Plane {i}')
    plt.axis('off')
plt.suptitle("Bit Planes of Image")
plt.tight_layout()
plt.savefig("bit_planes.png")

# B
img_E_1 = cv2.imread("Screenshot from 2025-04-15 08-11-45.png", cv2.IMREAD_GRAYSCALE)
_, img_binary = cv2.threshold(img_E_1, 127, 1, cv2.THRESH_BINARY)


img_binary_resized = cv2.resize(img_binary, (gray.shape[1], gray.shape[0]), interpolation=cv2.INTER_NEAREST)
bit_planes_1 = bit_planes.copy()
bit_planes_1[0] = img_binary_resized

final_img_1 = np.zeros_like(gray, dtype=np.uint8)
for i in range(8):
    final_img_1 |= (bit_planes_1[i] << i)
cv2.imwrite("output_image_for_plane_1.png", final_img_1)

bit_planes_5 = bit_planes.copy()
bit_planes_5[4] = img_binary_resized
final_img_5 = np.zeros_like(gray, dtype=np.uint8)
for i in range(8):
    final_img_5 |= (bit_planes_5[i] << i)
cv2.imwrite("output_image_for_plane_5.png", final_img_5)
