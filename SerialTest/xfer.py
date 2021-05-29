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
<<<<<<< HEAD
                #print(data)
                #serial_port.write(data)
                # if we get a carriage return, add a line feed too
                # \r is a carriage return; \n is a line feed
                # This is to help the tty program on the other end 
                # Windows is \r\n for carriage return, line feed
                # Macintosh and Linux use \n
                if data == "\r".encode():
                    # For Windows boxen on the other end
                    serial_port.write("\n".encode())
        str = data.decode()
        print(data)
        print(str)
=======
        print(data)
>>>>>>> d18c9e30fa1432e824c04a081a035c59e5c48364

except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
