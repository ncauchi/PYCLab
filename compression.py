
import processData
import serial
import time
import cv2
import os
from pylibdmtx.pylibdmtx import decode


#Serial Comm Setup
pcPort = 'COM6'     #might be different for different computers
arduino = serial.Serial(port=pcPort, baudrate=9600, timeout=.1) 

#Camera Setup
cam_port = 0
cam = cv2.VideoCapture(cam_port) 
sampleCode = ""

#Data Processing Setup
dataFile = "example_data.csv"
nameFile = "data\\sample_names.txt"
startLine = 3

input("Press enter to begin")


namef = open(nameFile, "w")

while True:
    print("Taking Sample Picture")
    #Get Name of Sample
    success, image = cam.read()

    if not success:
        exit("Image capture error")

    data = decode(image)

    if(len(data) < 1):
        print("Could not decode data matrix from image")
        break
    
    name, loc = data[0]
    sampleCode = bytes.decode(name)
    namef.write(sampleCode+"\n")        #write name to file
    print("Starting test on sample: ", sampleCode)

    #Tell UR5 to grab next sample and Instron to start
    arduino.write(int(1).to_bytes() )
    time.sleep(0.05)
    res = int.from_bytes(arduino.readline())

    if(res != 1):
        exit("Arduino communication error")

    #Get Signal From Instron
    while arduino.in_waiting < 1:  #wait until arduino sends signal
        pass
    
    res = int.from_bytes(arduino.readline())

    if(res != 2):
        exit("Arduino communication error")

    print("Test Complete")

namef.close()

if input("Process Data? (y/n)") == "y":
    processData.process(dataFile, nameFile, startLine)

