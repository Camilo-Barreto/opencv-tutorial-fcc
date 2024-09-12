import cv2 as cv 

img = cv.imread('Photos/group 1.jpg')
cv.imshow("Group", img)

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow("Average blur", average)

# Gaussian blur
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian Blur", gaussian)

# Median blur 
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral blur 
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral blur", bilateral)

cv.waitKey(0)