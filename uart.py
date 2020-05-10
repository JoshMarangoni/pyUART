from pathlib import Path
import serial
import time
import os


class Uart():
	def __init__(self, state=None):
		self.working_dir = Path(os.path.dirname(os.path.abspath(__file__)))
		self.platform = state["platform"]

		if (self.platform == "laptop"):
			self.port = '/dev/ttyUSB0'
		else:
			self.port = '/dev/serial0'

		self.ser = serial.Serial(
			port=self.port ,\
			baudrate=115200,\
			parity=serial.PARITY_NONE,\
			stopbits=serial.STOPBITS_ONE,\
			bytesize=serial.EIGHTBITS,\
				timeout=0)

	def read_buffer(self):
		received_data = self.ser.read()
		time.sleep(0.03)
		data_left = self.ser.inWaiting()
		received_data += self.ser.read(data_left)
		#print(received_data)
		return received_data.decode()

	def twos_complement(self, hexstr, bits):
		value = int(hexstr,16)
		if value & (1 << (bits-1)):
			value -= 1 << bits
		return value

	def read_hex(self):
		str_num = self.read_buffer()

		if len(str_num) == 0:
			print("buffer empty")
			return 0

		stripped_chars = str_num.rstrip("\n\r")
		num_bits = len(stripped_chars)*4
		s_hex_num = self.twos_complement(stripped_chars, num_bits)
		return s_hex_num

	def send_hex(self, angle):
		if angle < 0:
			hex_str = hex(65536+angle)
		else:
			hex_str = hex(angle)
		self.send_string(hex_str + '\r\n')

	def send_string(self, data_out=None):
		if data_out is None:
			data = input("Type: ")
			if data == "":
				print("Data must not be null")
				return False
			else:
				self.ser.write(data.encode())
		else:
			self.ser.write(data_out.encode())
		return True
