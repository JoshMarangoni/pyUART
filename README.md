# pyUART
A python UART library using pySerial

## Using the driver
```
cd pyUart
python uart/ -p {platform} -m {mode}
```

### Driver modes
- Send: You will be prompted to input a string and press enter, which will be transmitted through the UART.
- Listen: Program will listen on UART port and print to the console

### Arguments
- platform: laptop (Ubuntu), nano, pi
- mode: listen, send

