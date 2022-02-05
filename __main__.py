'''
Uart driver for testing the uart module

'''

from uart import Uart
import argparse
import time
import re


def write_chars(uart):
    i = 0
    while True:
        uart.send_string(str( ord('A') + i))
        time.sleep(0.01)
        try:
            received_str = uart.read_buffer().replace('\x00','')
            if received_str != '':
                print(chr(int(received_str)))
        except ValueError as e:
            print(e)
        i += 1
        time.sleep(1)

def listen(uart):
    while True:
        received = uart.read_buffer()
        if received != '':
            print(received)
        time.sleep(1)

def write_string(uart):
    send = input("Send over UART: ")
    while True:
        uart.send_string(send)
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', "--port", default="/dev/ttyUSB0", help="Which serial port to use")
    parser.add_argument('-m', "--mode", default="listen", help="Options: listen, write_string, write_chars")
    args = vars(parser.parse_args())
    uart = Uart(args["port"])

    if args["mode"] == "listen":
        listen(uart)
    elif args["mode"] == "write_string":
        write_string(uart)
    else:
        write_chars(uart)
