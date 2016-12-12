import cv2
import numpy as np

img = cv2.imread('EMP.png', cv2.IMREAD_COLOR)
px = img[550, 500]

# Region of image = white
roi = img[550:600, 500:550] = [255,255,255]
# move roi
emp_green = img[650:700, 550:600]
img[150:200, 150:200] = emp_green

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
