"""
Example of how to change flight modes using pymavlink
"""

import sys

from pymavlink import mavutil


    # Membuat
master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)

master.wait_heartbeat()

mode = 'STABILIZE'


if mode not in master.mode_mapping():
    print('Unknown mode : {}'.format(mode))
    print('Try:', list(master.mode_mapping().keys()))
    sys.exit(1)


mode_id = master.mode_mapping()[mode]

def stabilize():
    master.mav.set_mode_send(
        master.target_system,
        mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
        mode_id)
    print('Mode Stabilize')

stabilize()

