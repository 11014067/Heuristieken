classes.py

class House:

	def __init__(self, x, y, voltage, battery_no):
		self.x = x
		self.y = y
		self.voltage = voltage
		self.battery_no = None

	def add_battery(self, battery_no):
		self.battery_no = battery_no		


class Battery:

	def __init__(self, x, y, min_x, max_x, voltage, d_voltage):	
		x = self.x
		y = self.y