import serial

ser = serial.Serial("/dev/cu.HC-06", 9600)

print(ser.name)

while True:
    ser.write("good".encode())