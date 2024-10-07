import serial
import sys, time

Serial = serial.Serial(port="/dev/cu.HC-06", baudrate=9600)

with open("PATH.txt", "r") as f:
    msg = f.read()

m = ""

for i in msg.split("\n"):
    m += i

# print(m)
for i in range(100):
    Serial.write((m + '\n').encode())