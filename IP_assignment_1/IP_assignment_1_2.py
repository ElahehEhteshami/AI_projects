import cv2
import numpy as np

# read image
image = cv2.imread("Screenshot from 2025-04-15 08-11-45.png")

# converting to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# A
mole_coords = [
    (390, 165),
    (357, 332),
    (480, 315),
    (350, 400),
    (413, 479)
]
#
# image_with_white_moles = gray_bgr.copy()
# for center in mole_coords:
#     cv2.circle(image_with_white_moles, center, radius=6, color=(255, 255, 255), thickness=-1)
#
# cv2.imshow("2-a: White moles", image_with_white_moles)
# cv2.imwrite('2-a: White moles.png', image_with_white_moles)
# cv2.waitKey(0)


# B
forehead_patch = gray_bgr[165:170, 480:485]
mean_color = forehead_patch.mean(axis=(0, 1)).astype(np.uint8)

image_with_skin_moles = gray_bgr.copy()
for center in mole_coords:
    cv2.circle(image_with_skin_moles, center, radius=6, color=tuple(int(c) for c in mean_color), thickness=-1)

cv2.imshow("2-b: Moles with forehead color", image_with_skin_moles)
cv2.imwrite('2-b: Moles with forehead color.png', image_with_skin_moles)
cv2.waitKey(0)
cv2.destroyAllWindows()
