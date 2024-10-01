import serial
import time
import cv2
import os
from pylibdmtx.pylibdmtx import decode


#Serial Comm Setup
pcPort = 'COM4'     #might be different for different computers
#arduino = serial.Serial(port=pcPort, baudrate=9600, timeout=.1) 

#Camera Setup
cam_port = 0
#cam = cv2.VideoCapture(cam_port) 
sampleCode = ""


image = cv2.imread("control2.png")
while True:
    #Get Name of Sample
    ##success, image = cam.read()
    success = True
    

    if not success:
        exit("Image capture error")

    data = decode(image)

    if(len(data) < 1):
        exit("Could not decode data matrix from image")
    
    name, loc = data[0]
    sampleCode = bytes.decode(name)
    print("Starting test on sample: ", sampleCode)

    #Tell Instron to start
    #Get Signal From Instron
    inp = input("[dev] Test Complete (Y/N) ") 

    if(inp != "Y" and inp != "y"):
        exit("Exiting")

    image = cv2.imread("control1.png")