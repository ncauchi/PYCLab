import serial 
import time 

pcPort = 'COM3' #might be different for different computers

arduino = serial.Serial(port=pcPort, baudrate=9600, timeout=.1) 

inp = input("test")
if(inp == "y"):
	print("worked")
	exit(0)

print("failed")