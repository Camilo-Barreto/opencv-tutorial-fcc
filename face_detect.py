import cv2 as cv 

def rescale(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

# # Testing nevins video
# capture = cv.VideoCapture('NEVIN\Tsumyoki x Bharg - Pink Blue _ Official Music Video.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescale(frame, scale=0.75)
#     cv.imshow("NEVIN original", frame_resized)

#     gray_video = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
#     cv.imshow("Nevin B and W", gray_video)

#     faces_vid_rect = haar_cascade.detectMultiScale(gray_video, scaleFactor=1.1, minNeighbors=10)
#     print(faces_vid_rect)
#     print(f'Number of faces found = {len(faces_vid_rect)}')

#     for (x, y, w, h) in faces_vid_rect:
#         cv.rectangle(frame_resized, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
#     cv.imshow("Faces detected", frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows() 


# Tutorial code 
img = cv.imread('Photos/group 1.jpg')
cv.imshow("Person", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray person", gray)

# ADDED AT THE TOP ASWELL
## haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow("Detected faces", img)
cv.waitKey(0)