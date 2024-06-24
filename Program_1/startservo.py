import serial
import subprocess
from main_servo import servo

# Ganti '/dev/ttyUSB0' dengan port yang sesuai di Raspberry Pi
arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

while True:
    data = arduino.readline().decode('utf-8').strip()
    if data == "YY":
        servo(1000, 2000, 50)
    else:
        servo(2000, 1000, -50)