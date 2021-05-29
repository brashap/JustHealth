#!/usr/bin/python3
import time
import serial

print("Starting Receiver Program")

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
    # Send a simple header
    while True:
        #i = 0
        data = b""
        #while i < 176:
        if serial_port.inWaiting() > 0:
            data = data + serial_port.read_until(b'\x13',177)
            str = data.decode()
            print("------------------------")
            print(data)
            print()
            print(str)
            print()

except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
