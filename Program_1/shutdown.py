import os
import time

def shtdwn():
    for i in range (5):
        print("Auto Shutdown")
        time.sleep(1)

    os.system("sudo shutdown -h now")
