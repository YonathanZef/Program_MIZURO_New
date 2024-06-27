from pymavlink import mavutil
from maju import maju_fwd
from kanan import kanan_laterall
from kiri import kiri_lateral
# from servo_open import servo_opn
from servo_close import servo_cls
from stop import stop_4m
from emergency import emergency_1
from mode import stabilize
# from disarm import dis_arm
from shutdown import shtdwn
import time


# buat koneksi
master = mavutil.mavlink_connection("/dev/ttyAMA0", baud=57600 )
# Tunggu Konfirmasi HeartBeat
master.wait_heartbeat()

#========= Buat program Tombol ==========#

#========== END PB ============#

def run():
    
    #========== MAJU*1 ============#
    print("Maju *1 ")
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    #------ Stabil -------#
    stabilize()
    #------ ++++++ -------#
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
    stop_4m()
    time.sleep(2)
    print("================>")

    #========== KANAN*1 ============#
    print("Kanan *1 ")
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    kanan_laterall()
    time.sleep(2)
    stop_4m()
    time.sleep(2)
    print("================>")

    #========== MAJU*2 ============#
    print("Maju *2 ")
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    maju_fwd()
    time.sleep(2)
    stop_4m()
    time.sleep(2)
    print("================>")

    #========== Servo Open ============#
    print("Servo Open")
    # servo_opn()
    time.sleep(2)
    print("================>")

    #========== Finish ============#
    print("Finish")
    emergency_1()
    time.sleep(1)
    # dis_arm()
    time.sleep(1)
    print("================>")

    #========== Shutdown ============#
    shtdwn()