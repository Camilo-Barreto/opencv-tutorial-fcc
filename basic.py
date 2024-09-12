# 5 essential functions in openCV
import cv2 as cv 

img = cv.imread('Photos/group 1.jpg')
cv.imshow("Cat", img)

# Converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", gray)

# Blur img
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow("dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=4)
cv.imshow("Eroded", eroded)

# Resize
resize = cv.resize(img, (500,500), cv.INTER_AREA)
cv.imshow("resized", resize)

# Cropping 
cropped = img[50:200, 200:500]
cv.imshow("Cropped", cropped)

cv.waitKey(0)