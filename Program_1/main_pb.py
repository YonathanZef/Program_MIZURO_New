import gpiod
from pymavlink import mavutil
from maju import maju_fwd
from kanan import kanan_laterall
from kiri import kiri_lateral
# from servo_open import servo_opn
#from servo_close import servo_cls
from stop import stop_4m
from emergency import emergency_1
from mode import stabilize
# from disarm import dis_arm
from shutdown import shtdwn
import time

def tes_q():
    print("tes_q started")
    # Create the connection
    master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
    print("Connection created")
    # Wait a heartbeat before sending commands
    master.wait_heartbeat()
    print("Heartbeat received")

    # Arm
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
        0,
        1, 0, 0, 0, 0, 0, 0)

    # wait until arming confirmed
    print("Waiting for the vehicle to arm")
    master.motors_armed_wait()
    print('Armed!')

    # from depth import set_target_depth
    # set_target_depth(-2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()

    stop_4m()

    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()   
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()  
    stop_4m()
    # dis_arm()

    # time.sleep(2)
    # print("Executing kanan_laterall(5)")
    # kanan_laterall(5)
    # print("kanan_laterall completed")


LED_PIN = 17
BUTTON_PIN = 24
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
button_line = chip.get_line(BUTTON_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

print("Starting main loop")

try:
    while True:
        button_state = button_line.get_value()
        print(f"Button state: {button_state}")
        if button_state == 1:
            print("Button pressed, executing tes_q()")
            tes_q()
        else:
            led_line.set_value(0)
        time.sleep(0.1)  # Add a small delay to avoid overwhelming the CPU
finally:
    led_line.release()
    button_line.release()
