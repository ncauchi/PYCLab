
import cv2
from pylibdmtx.pylibdmtx import decode


#change if multiple cameras
cam_port = 0

cam = cv2.VideoCapture(cam_port) 
success, image = cam.read()
if success:
    cv2.imwrite("test.png", image)


im = cv2.imread('control2.png')
data = decode(im)
name, loc = data[0]
print(name)

