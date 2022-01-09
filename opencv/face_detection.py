#importing openCV
import cv2

# load the input image
img = cv2.imread('picture.jpg')

# Converting the image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Loading the cascade
cascade_faces = cv2.CascadeClassifier('haarcascade_frontal_face.xml') 

# Detecting faces
faces = cascade_faces.detectMultiScale(gray, 1.1, 4)

# Drawing rectangle around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()
