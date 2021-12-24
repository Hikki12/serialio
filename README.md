# SerialIO

A serial library based on callbacks and threading.

## Single Serial Device
You could run a single serial device as follows:
```python
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
```
The serial device has its own execution loop running on a thread.
## Multiple Serial Devices
Also multiples serial devices cool be manage at the same time:
```python
from serialio import SerialManager


serial = SerialManager(devices=['/dev/cu.usbserial-1460'], baudrate=9600)

# Do something if the connection status changes
serial.on('connection-status', lambda device, status: print(f'{device} connection status: {status}'))

# Do something if a new data were received
serial.on('data-incoming', lambda device, data: print(f'{device} has new data: {data}'))

# Start all serial devices listed
serial.startAll()
```

## License
MIT