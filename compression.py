
import serial
import time
import cv2
import os
from pylibdmtx.pylibdmtx import decode


#Serial Comm Setup
pcPort = 'COM4'     #might be different for different computers
arduino = serial.Serial(port=pcPort, baudrate=9600, timeout=.1) 

#Camera Setup
cam_port = 0
cam = cv2.VideoCapture(cam_port) 
sampleCode = ""



while True:
    image, success, data = None
    #Get Name of Sample
    success, image = cam.read()

    if not success:
        exit("Image capture error")

    data = decode(image)

    if(len(data) < 1):
        exit("Could not decode data matrix from image")
    
    name, loc = data[0]
    sampleCode = bytes.decode(name)
    print("Starting test on sample: ", sampleCode)

    #Tell UR5 to grab next sample
    arduino.write(int(1).to_bytes() )
    time.sleep(0.05)
    res = arduino.readline().decode()

    if(res != "On"):
        exit("Arduino communication error")

    print("Starting Test")

    #Tell Instron to start
    #Get Signal From Instron
    inp = input("[dev] Test Complete (Y/N) ") 

    if(inp != "Y" and inp != "y"):
        exit("Exiting")