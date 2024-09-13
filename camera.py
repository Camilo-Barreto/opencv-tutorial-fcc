import cv2 as cv
import sys

# Use default camera device --> 0
camera_device = 0

# Change camera device if specified in the cli
if len(sys.argv) > 1:
    camera_device = sys.argv[1]

source = cv.VideoCapture(camera_device)

win_name = "Camera Preview"
cv.namedWindow(win_name, cv.WINDOW_NORMAL)

# Run until user presses the Esc key
while cv.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break

    cv.imshow(win_name, frame)

source.release()
cv.destroyWindow(win_name)