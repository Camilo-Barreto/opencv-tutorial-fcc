import os
import cv2 as cv
import numpy as np

# List to store names of people whose faces will be trained
people = []

# Directory with the names of people and haar cascade
DIR = r'.\Face Recognition\Faces\train'
# Relative paths work from the main folder OPENCV WITH PYTHON 
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# Get names of people from the folder
for i in os.listdir(DIR):
    people.append(i)

print(f'The names of people are {people}')

# List of faces and the name
features = []
labels = []

def create_train():
    for person in people:
        # Get path to the folder of this person
        path = os.path.join(DIR, person)
        label = people.index(person)

        # Get path to each image in the folder
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            # Read the image and convert to grayscale
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Detect the coordinates of a face in the image
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            # Crop out the face and add it to the features list and also add the persons index position in label
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

create_train()
print("Training done ----------------------------------")

features = np.array(features, dtype="object")
labels = np.array(labels)
# Train the recognizer on the features list and the labels list 
face_recognizer.train(features, labels)

face_recognizer.save("Face Recognition/face_trained.yml")
np.save('Face Recognition/features.npy', features)
np.save('Face Recognition/labels.npy', labels)
