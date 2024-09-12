import cv2 as cv
import numpy as np

# 500 height and width and 3 color channels
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank", blank)

# 1. Paint the image a certain color
blank[200:300, 300:400] = 0,255,0
cv.imshow("Green", blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,250), (10,500), (0,0,255), thickness=2)
cv.imshow("Rectangle", blank)

# 3. Draw a circle
cv.circle(blank, (250,250), 100, (0,0,255), thickness=3)
cv.imshow("Circle", blank)
# img = cv.imread("Photos/cat.jpg")
# cv.imshow("Cat", img)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (183,380,255), thickness=3)
cv.imshow("Line", blank)

# 5. Write text on images
cv.putText(blank, "Hello Naruto", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank)

cv.waitKey(0)