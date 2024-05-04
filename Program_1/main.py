from pymavlink import mavutil
from arm import arming
from mode import stabilize
from control import movement

# Create the connection
master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
# Tunggu HearBeat Sebelum mengirim perintah
master.wait_heartbeat()
# Kirim perintah Untuk ARMED
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)

# tunggu sampai arming dikonfirmasi (bisa dicek manual dengan master.motors_armed())
print("Waiting for the vehicle to arm")
master.motors_armed_wait()
print('Armed!')

stabilize()

movement()

