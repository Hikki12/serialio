from serialio import SerialManager
import time


serial = SerialManager(devices=['/dev/cu.usbserial-1440'], baudrate=9600)

# Do something if the connection status changes
serial.on('connection-status', lambda device, status: print(f'{device} || connection status: {status}'))

# Do something if a new data were received
serial.on('data-incoming', lambda device, data: print(f'{device}  || has new data: {data}'))

# Start all serial devices listed
serial.startAll()

# Wait some time
time.sleep(3)

# Write the message
message = "Hello world!"
serial.write(to='/dev/cu.usbserial-1440', message=message, end='\n')