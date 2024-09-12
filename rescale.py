import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # cv.resize resizes a frame to a particular dimension
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
    
# Only works for live videos 
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# Read videos
capture = cv.VideoCapture('Videos/dog.mp4')

# Rescale imgage
img = cv.imread('Photos/cat_large.jpg')

resized_image = rescaleFrame(img, 0.5)
cv.imshow('OG Cat', img)
cv.imshow('Cat', resized_image)
cv.waitKey(0)

while True:
    # Boolean to say if the frame was successfully read or not and the frame
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.50)
    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    # if d is pressed close
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

