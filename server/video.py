import cv2


camera = cv2.VideoCapture(1)

while True:
      # read the camera frame
    success, frame = camera.read()
    if not success:
        break
    else:
        ret, buffer = cv2.imencode('.jpg', frame)
