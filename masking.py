import cv2 as cv 
import numpy as np

img = cv.imread('Photos/group 1.jpg')
cv.imshow("Group", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("blank", blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Circle", circle)

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cv.imshow("Rectangle", rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("wierd shape", weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("Masked image", masked)

cv.waitKey(0)