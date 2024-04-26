"""
Needed modules:
OpenCV (pip install opencv-python)
MediaPipe (pip install mediapipe) !Important: until now, runs only with python 3.7.0 or earlier
CVZone (pip install cvzone
"""


# cv2 is used to capture the video steam from the cam
import cv2
# module for face detection
from cvzone.FaceDetectionModule import FaceDetector

# instantiate the cam. "0" means the first/default cam of your system
cam = cv2.VideoCapture(0)

# instantiate the face detector
# first parameter varies from 0 to 1, where 1 indicates that the detection needs to be sure a face was present on the image (confidence mode)
# second parameter is 0 for near range faces, and 1 to far-range faces
detector = FaceDetector(0.7, 0)

# keep capturing images (like a live video) until ESC key is pressed
while True:
    # cam.read() will return a boolean indicating the capture was ok, and the image itself
    success,img = cam.read()

    # if the image was successfully captured
    if success:
        # findFaces method will return the image with the 'bounding box' drawn around the face, and the list of parameters of the box
        img,box = detector.findFaces(img, draw=True)

    # show the last image successfully captured
    cv2.imshow('Face detection', img)

    # abort when pressing ESC
    if cv2.waitKey(1) == 27: break