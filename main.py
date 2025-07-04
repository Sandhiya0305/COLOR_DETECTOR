import cv2
from PIL import Image
from utils import get_limits

video = cv2.VideoCapture(0)
yellow = (0, 255, 255)
while True:
    ret, frame = video.read()

    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower, upper = get_limits(yellow)
    mask = cv2.inRange(img_hsv, lower, upper)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)

    cv2.imshow('mask', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
