import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# bitwise OR 
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR", bitwise_or)

# bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise XOR", bitwise_xor)

# bitwise NOT
bitwise_not_r = cv.bitwise_not(rectangle)
cv.imshow("Bitwise NOT rectangle", bitwise_not_r)

bitwise_not_c = cv.bitwise_not(circle)
cv.imshow("Bitwise NOT circle", bitwise_not_c)

cv.waitKey(0)