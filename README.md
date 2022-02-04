# pyUART
A python UART library using pySerial

## Using the driver
```
cd pyUart
python uart/ -p {port} -m {mode}
```

### Arguments
- port: Which serial port to use, default is ttyUSB0
- mode: listen, write_string, write_chars

### Driver modes
- listen: Program will listen on UART port and print to the console
- write_string: You will be prompted to input a string and press enter, which will be transmitted through the UART repetitively, every second.
- write_chars: chars will be sent to the UART every second, starting at 'a' and adding 1 to the ascii code each time

