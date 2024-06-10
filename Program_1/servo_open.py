
import time

from pymavlink import mavutil

def servo_opn():
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

    # membuat koneks
    master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
    # tunggu heartbeat terkonfirmasi
    master.wait_heartbeat()

    # Servo bergerak dari min ke max (close)
    for us in range(1100, 1900, 50):
        set_servo_pwm(3, us)
        time.sleep(0.125)