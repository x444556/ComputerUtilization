import psutil
import os
import time
import sys

if len(sys.argv) >= 2:
    drive = sys.argv[1]
else:
    drive = 'C'

while True:
    end_time = time.time() + 1
    while time.time() < end_time:
        pass
    os.system("cls")
    print("CPU: "+str(psutil.cpu_percent()+20))
    print("RAM: "+str(psutil.virtual_memory()[2]))
    print("Disk: "+str(psutil.disk_usage(drive + ':\\')[3]))

exit()
