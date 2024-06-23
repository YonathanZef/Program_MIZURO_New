import serial
import subprocess

# Ganti '/dev/ttyUSB0' dengan port yang sesuai di Raspberry Pi
arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

while True:
    data = arduino.readline().decode('utf-8').strip()
    if data == "YY":
        print("hello world")
