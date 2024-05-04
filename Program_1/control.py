
# Import mavutil
from pymavlink import mavutil

# Membuat koneksi
master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600)
# Tunggu HearBeat Sebelum mengirim perintah
master.wait_heartbeat()

x_axis  = 500
y_axis  = 500
z_axis  = 500
r_muter = 500
tombol  = 0


# master.mav.manual_control_send( X, Y, Z, R, button)
def movement():
    master.mav.manual_control_send(
        master.target_system, 
        x_axis, 
        y_axis,
        z_axis, 
        r_muter,
        tombol)
    print('Run')

movement()
