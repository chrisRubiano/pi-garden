import serial
import time

ser = serial.Serial('/dev/ttyUSB0')

#Read input from serial after sending a character and a newline
ser.write(b's\n')
while True:
    if (ser.inWaiting()>0):
        data = ser.readline()
        data = data.decode("ASCII")
        data = data.rstrip()
        print(data)
        break