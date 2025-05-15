import cv2
import numpy as np
import matplotlib.pyplot as plt

# مرحله 1: خواندن و خاکستری کردن تصویر
img = cv2.imread("Screenshot from 2025-05-02 18-24-59.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# مرحله 2: تعریف پارامترها و آماده‌سازی خروجی
a, b = 50, 180
ya, yb = 20, 230
L = 255
output = np.zeros_like(gray, dtype=np.uint8)

# مرحله 3: اعمال انتقال کنتراست استرچینگ
for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        x = gray[i, j]
        if x < a:
            y = ya / a * x
        elif x < b:
            y = ((yb - ya) / (b - a)) * (x - a) + ya
        else:
            y = ((L - yb) / (L - b)) * (x - b) + yb
        output[i, j] = np.clip(y, 0, 255)

# نمایش با OpenCV
cv2.imshow("Original Gray", gray)
cv2.imshow("Contrast Stretched", output)

# ذخیره خروجی
cv2.imwrite("original_gray.png", gray)
cv2.imwrite("contrast_stretch_output.png", output)

cv2.waitKey(0)
cv2.destroyAllWindows()

