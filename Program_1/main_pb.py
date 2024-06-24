import gpiod
from tesmain import tes_q

from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
# tunggu sampai arm
master.wait_heartbeat()

# https://mavlink.io/en/messages/common.html#MAV_CMD_COMPONENT_ARM_DISARM

# Arm
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
    0,
    1, 0, 0, 0, 0, 0, 0)

# Tunggu Sampai armed terkonfirmasi
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')

LED_PIN = 17
BUTTON_PIN = 24
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
button_line = chip.get_line(BUTTON_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)
stats = False

try:
   while True:
       button_state = button_line.get_value()
       if button_state == 1:
           led_line.set_value(1)
           print("hh")
           stats = True
       elif stats == True:
           led_line.set_value(0)
           tes_q()
           
finally:
   led_line.release()
button_line.release()
