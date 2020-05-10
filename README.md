# pyUART
A python UART library using pySerial

## Run

```
cd pyUart
python uart/ -p {platform} -m {mode}
```
### Arguments
- platform: laptop (Ubuntu), nano, pi
- mode: listen, send

### Using the driver
- Send mode: You will be prompted to input a string and press enter, which will be transmitted through the UART.
- Listen: Program will listen on UART port and print to the console
