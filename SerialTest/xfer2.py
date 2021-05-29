#!/usr/bin/python3

# py-serial is required: $ sudo apt-get install python3-serial

import time
import serial

# ************ Important ************
# Disable Serial console for ttyTHS1
# On the Nano, execute the following:
#     systemctl stop nvgetty
#     systemctl disable nvgetty
#     udevadm trigger
# ***********************************

print("Starting Receiver Program")
print("Press Crtl-C to Exit")

J41uart = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
time.sleep(1)

try:
    # Run continuously
    while True:
        data = b""
        if J41uart.inWaiting() > 0:
            data = data + J41uart.read_until(b'\x0D',180)
            str = data.decode()
            print(str)
            print()

except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    J41uart.close()
    pass
