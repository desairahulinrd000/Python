import serial
ser=serial.Serial('COM13',baudrate=9600,timeout=1)
while True:
    arduinod=ser.readline().decode('ascii')
    print(arduinod)
