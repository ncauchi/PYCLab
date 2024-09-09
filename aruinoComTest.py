import serial 
import time 

pcPort = 'COM3' #might be different for different computers

arduino = serial.Serial(port=pcPort, baudrate=9600, timeout=.1) 



while True: 
	inp = input("Send: ")
	num = int(inp).to_bytes()
	print(type(num))
	arduino.write(num)
	time.sleep(0.05)
	#print(arduino.in_waiting)
	res = arduino.readline().decode()
	print(res)