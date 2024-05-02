from pymavlink import mavutil
from arm import arming

# Create the connection
master = mavutil.mavlink_connection('')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

arming(1,1)
master.motors_armed_wait()
print('Armed!')

