import cv2
import numpy as np

img = cv2.imread("Screenshot from 2025-05-02 18-10-56.png")  # یا هر تصویری
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#پیاده‌سازی دستی equalization
hist = np.bincount(gray.flatten(), minlength=256)

cdf = hist.cumsum()
cdf_normalized = cdf * 255 / cdf[-1]  # نرمال‌سازی

equalized_manual = cdf_normalized[gray].astype(np.uint8)

# روش OpenCV: equalizeHist
equalized_cv = cv2.equalizeHist(gray)

# روش CLAHE (Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
equalized_clahe = clahe.apply(gray)

# نمایش نتایج
cv2.imshow("Manual Equalization", equalized_manual)
cv2.imshow("cv2.equalizeHist", equalized_cv)
cv2.imshow("cv2.CLAHE", equalized_clahe)

cv2.imwrite("original_gray.png", gray)
cv2.imwrite("manual_equalization.png", equalized_manual)
cv2.imwrite("cv_equalizeHist.png", equalized_cv)
cv2.imwrite("cv_CLAHE.png", equalized_clahe)

cv2.waitKey(0)
cv2.destroyAllWindows()
