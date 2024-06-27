
import time
import serial
from pymavlink import mavutil

# membuat koneks
master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
# tunggu heartbeat terkonfirmasi
master.wait_heartbeat()

arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)


# def servo_cls():
def set_servo_pwm(servo_n, microseconds):

    # master.set_servo(servo_n+8, microseconds) or:
    master.mav.command_long_send(
        master.target_system, master.target_component,
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO,
        0,            # transmisi pertama
        servo_n + 8,  # servo offset +8
        microseconds, # PWM pulse-width
        0,0,0,0,0     # parameterr
    )

    # master.mav.command_long_send(
    #     master.target_system,
    #     master.target_component,
    #     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
    #     0,
    #     1, 0, 0, 0, 0, 0, 0
    # )


while True:
    data = arduino.readline().decode('utf-8').strip()
    if data == "DD":
        # subprocess.run(["python3", "hello.py"]
        # Servo bergerak dari nax ke min (open)
        for us in range(1000, 2000, 50):
            set_servo_pwm(3, us)
            time.sleep(0.125)
            print("Servo Open")