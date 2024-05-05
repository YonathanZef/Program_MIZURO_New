
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
# Wait a heartbeat before sending commands
master.wait_heartbeat()

def set_rc_channel_pwm(channel_id, pwm=1500):

    if channel_id < 1 or channel_id > 18:
        print("Channel does not exist.")
        return

    rc_channel_values = [65535 for _ in range(18)]
    rc_channel_values[channel_id - 1] = pwm
    master.mav.rc_channels_override_send(
        master.target_system,                # target_system
        master.target_component,             # target_component
        *rc_channel_values[8])                  # RC channel list, in microseconds.


# fungsi bergerak ke kanan
def move_kanan():
    set_rc_channel_pwm(6, 1600)
    set_rc_channel_pwm(5, 1500)
# fungsi bergerak ke kiri
def move_kiri():
    set_rc_channel_pwm(6, 1400)
    set_rc_channel_pwm(5, 1500)
# fungsi bergerak maju
def move_maju():
    set_rc_channel_pwm(5, 1600)
    set_rc_channel_pwm(6, 1500)