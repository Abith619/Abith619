import cv2
import numpy as np
url = "Your IP Address/video"
cp = cv2.VideoCapture(url)
while(True):
    camera, frame = cap.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()
"""First, install the OpenCV library in Python; pip install opencv-python.Download and install the IP Webcam application on your 
smartphones. After installing the IP Webcam app, make sure your phone and PC are connected to the same network. 
Run the app on your phone and click Start Server.After that, your camera will open with an IP address at the bottom.
Copy the IP address as we will need to use it in our Python code to open your phone’s camera."""