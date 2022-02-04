'''
Wrapper class for pySerial
'''

import serial
import time

class Uart():
	def __init__(self, port):
		self.port = port
		self.ser  = serial.Serial(
			port=self.port,
			baudrate=115200,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS,
			timeout=0
		)
		self.ser.reset_input_buffer()
		self.ser.reset_output_buffer()

	''' Reads and empties all contents of receive buffer '''
	def read_buffer(self):
		num_bytes = self.ser.inWaiting()
		received_data = self.ser.read(num_bytes)
		# return self.ser.read()
		# return received_data
		return received_data.decode()

	'''
	Used by read_hex method to convert a hex string to an integer
	'''
	def twos_complement(self, hexstr, bits):
		value = int(hexstr,16)
		if value & (1 << (bits-1)):
			value -= 1 << bits
		return value

	'''
	Read a hex string and convert to an integer
	'''
	def read_hex(self):
		str_num = self.read_buffer()

		if len(str_num) == 0:
			print("buffer empty")
			return 0

		stripped_chars = str_num.rstrip("\n\r")
		num_bits = len(stripped_chars)*4
		s_hex_num = self.twos_complement(stripped_chars, num_bits)
		return s_hex_num

	''' Converts an integer to a corresponding hex string and sends it '''
	def send_hex(self, angle):
		if angle < 0:
			hex_str = hex(65536+angle)
		else:
			hex_str = hex(angle)
		self.send_string(hex_str + '\r\n')

	''' Send an input string, or prompt user for input if not given a string '''
	def send_string(self, data_out=None):
		if data_out is None:
			return False
		return self.ser.write(data_out.encode())

	''' Close serial port '''
	def close(self):
		self.ser.close()

	def __del__(self):
		self.ser.reset_output_buffer()
		self.close()
