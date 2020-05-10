# pyUART
A python UART library using pySerial

## Using the driver
```
cd pyUart
python uart/ -p {platform} -m {mode}
```

### Arguments
- platform: laptop (Ubuntu), nano, pi
- mode: listen, send

### Driver modes
- Send: You will be prompted to input a string and press enter, which will be transmitted through the UART.
- Listen: Program will listen on UART port and print to the console

### Class Methods
- read_buffer(): empty's UART and returns string
- twos_compliment(): given a hexidecimal bit string, return a signed integer
- read_hex(): calls read_buffer() and twos_compliment() and returns integer
- send_hex(): given an integer, convert into a hex bit string
