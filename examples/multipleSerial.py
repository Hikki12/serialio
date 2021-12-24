from serialio import SerialManager


serial = SerialManager(devices=['/dev/cu.usbserial-1460'], baudrate=9600)

# Do something if the connection status changes
serial.on('connection-status', lambda device, status: print(f'{device} connection status: {status}'))

# Do something if a new data were received
serial.on('data-incoming', lambda device, data: print(f'{device} has new data: {data}'))

# Start all serial devices listed
serial.startAll()