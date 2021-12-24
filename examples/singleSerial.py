from serialio import SerialEmitter


serial = SerialEmitter(port='/dev/cu.usbserial-1460', baudrate='9600')

# Do something if the connection status changes
serial.on('connection-status', lambda status: print('serial port is open: ', status))

# Do something if a new data were received
serial.on('data-incoming', lambda data: print('received data: ', data))

# Do something if a change occurs in the serial ports
serial.on('ports-update', lambda ports: print('New devices detected: ', ports))

# Start execution loop
serial.start()