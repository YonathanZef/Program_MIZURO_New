
# Import mavutil
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