"""
Example of how to Arm and Disarm an Autopilot with pymavlink
"""
# Import mavutil
from pymavlink import mavutil

master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
# tunggu sampai heartbeat terkonfirmasi
master.wait_heartbeat()

# https://mavlink.io/en/messages/common.html#MAV_CMD_COMPONENT_ARM_DISARM

# Disarm
# def dis_arm():
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
    0,
    0, 0, 0, 0, 0, 0, 0)

# wait until arming confirmed (can manually check with master.motors_armed())
print("Waiting for the vehicle to arm")
master.motors_disarmed_wait()
print('Disarm!')
