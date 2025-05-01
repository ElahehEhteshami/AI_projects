import numpy as np
import cv2

img_size = 512

# creating image
img = np.zeros((img_size, img_size, 3), dtype=np.uint8)

circle_centers =  [
    (200, 200), (232, 200), (200, 300), (248, 300), (200, 400), (264, 400)
]

# drawing circles
for center in circle_centers:
    cv2.circle(img, center, radius=16, color=(255, 255, 255), thickness=-1)  # دایره سفید پر شده

# writing name
cv2.putText(img, 'Elaheh Ehteshami', org=(40, 40), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=1, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)

#showing image
cv2.imshow("Exercise 1", img)
cv2.imwrite("Excercise 1.png", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

