import serial
ser = serial.Serial("COM3", 9600)

for x in range(10):
	x = ser.read()
	print x
