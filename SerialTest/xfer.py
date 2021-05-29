#!/usr/bin/python3

# py-serial is required: $ sudo apt-get install python3-serial

import time
import serial

# **********   IMPORTANT   **********
# Disable Serial console for ttyTHS1
# On the Nano, execute the following
#	$ systemctl stop nvgetty
#	$ systemctl disable nvgetty
#	$ udevadm trigger
# ***********************************

print("Starting UART Receiver Program")

serial_port = serial.Serial(
    port="/dev/ttyTHS1",
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)

# Wait a second to let the port initialize
time.sleep(1)

try:
    while True:
        i = 0
        data = b""
        while i < 176:
            if serial_port.inWaiting() > 0:
                data = data + serial_port.read()
                i = i + 1
        str = data.decode()
        print(data)
        print(str)

except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
