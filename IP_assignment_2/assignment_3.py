import cv2
import numpy as np

# خواندن تصویر و تبدیل به خاکستری
image = cv2.imread("Screenshot from 2025-05-02 18-24-59.png")  # یا مسیر تصویر شما
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# اعمال فیلتر لاپلاس
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.clip(laplacian, 0, 255).astype(np.uint8)

# جمع با تصویر اصلی برای تیز کردن
sharpened_laplacian = cv2.add(gray, laplacian)

# اعمال بلور گاوسی برای تهیه نسخه نرم‌شده
blurred = cv2.GaussianBlur(gray, (5, 5), sigmaX=1)

# ماسک = تصویر اصلی - نسخه بلورشده
mask = cv2.subtract(gray, blurred)

# افزودن ماسک به تصویر اصلی
sharpened_unsharp = cv2.add(gray, mask)

cv2.imshow("Original", gray)
cv2.imshow("Laplacian Sharpened", sharpened_laplacian)
cv2.imshow("Unsharp Masking", sharpened_unsharp)


# ذخیره خروجی‌ها
cv2.imwrite("gray.png", gray)
cv2.imwrite("sharpened_laplacian.png", sharpened_laplacian)
cv2.imwrite("sharpened_unsharp.png", sharpened_unsharp)

cv2.waitKey(0)
cv2.destroyAllWindows()