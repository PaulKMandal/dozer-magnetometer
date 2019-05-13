import serial
import pyfirmata
import time
import math
ser = serial.Serial('COM8', 9600) #/dev/ttyACM0

#from pyfirmata import ArduinoMega, util

while True:   #two hash indicate comment. 1 hash is needed for while loop 
    ser_bytes = ser.readline().decode()
    ##strips out whitespace characters from string
    line = ser_bytes.strip()
    ##print(line)
    ##changes value to interger
    parts = line.split(' ')
    
    valuex = int(parts[0])
    valuey = int(parts[1])
    valuez = int(parts[2])

    print(valuex)
    print(" ")
    print(valuey)
    if(valuex == 0):
        if(valuey < 0):
            result = 3.14159/2
        if(valuey >= 0):
            result = 0
    else:
        result = math.atan((valuey)/(valuex))        

    degrees = (result*(180/3.14159))
    if(degrees > 360):
        degrees = degrees - 360
    if(degrees < 0):
        degrees = degrees + 360
    
    print(result)
    print(degrees)

    time.sleep(1)
    
    #prints values of data to check 
    #print(ser_bytes)
    #print(line)
    #print(valuex, valuey, valuez)
    

