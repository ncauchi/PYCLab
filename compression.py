
import serial
import time
import cv2
from pylibdmtx.pylibdmtx import decode


#Serial Comm Setup
pcPort = 'COM3'     #might be different for different computers
arduino = serial.Serial(port=pcPort, baudrate=9600, timeout=.1) 

#Camera Setup
cam_port = 0
cam = cv2.VideoCapture(cam_port) 
sampleCode = ""


def captureSample()->bool:
    success, image = cam.read()
    if success:
        cv2.imwrite("img.png", image)
        im = cv2.imread('img.png')
        data = decode(im)
        name, loc = data[0]
        sampleCode = name
        print("Found Sample: ", name)
        return True
    else:
        print("Image capture failure")
        return False

while True:
    inp = input("[dev] Test Complete (Y/N) ") 
    if(inp != "Y"):
        print("Exiting")
        exit()
    
    if(captureSample() ):
        print("Starting Test")
        arduino.write(int(1).to_bytes() )
        time.sleep(0.05)
        res = arduino.readline().decode()
        if(res != "On"):
            print("Arduino Communication Error")
        else:
            print("Starting Test")