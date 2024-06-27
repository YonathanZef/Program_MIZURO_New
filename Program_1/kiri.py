
from pymavlink import mavutil
import time

# buat koneksi
master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600 )
# Tunggu Konfirmasi HeartBeat
master.wait_heartbeat()

def kiri_lateral():

    def set_rc_channel_pwm(channel_id, pwm=1500):

        if channel_id < 1 or channel_id > 18:
            print("Channel does not exist.")
            return

        
        # https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE
        rc_channel_values = [65535 for _ in range(18)]
        rc_channel_values[channel_id - 1] = pwm
        master.mav.rc_channels_override_send(
            master.target_system,                # target_system
            master.target_component,             # target_component
            *rc_channel_values [:8])             # chanell list

    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 
        0,
        1, 0, 0, 0, 0, 0, 0)

    # tunggu sampai mendapatkan konfirmasi ARM
    print("Waiting for the vehicle to arm")
    master.motors_armed_wait()
    print('Armed!2')


    # Kiri on
    set_rc_channel_pwm(6,1300)
    # Throte on
    set_rc_channel_pwm(3,1800)
    # Maju off
    set_rc_channel_pwm(5,1500)