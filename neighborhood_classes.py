#classes.py

class House:

	def __init__(self, x, y, voltage, id):
		self.x = x
		self.y = y
		self.voltage = voltage
		self.id = id
		self.battery_no = None
		self.placed = False

	def add_battery(self, battery_no):
		self.battery_no = battery_no	

class Battery:

	def __init__(self, x, y, voltage):	
		self.x = x
		self.y = y
		self.voltage = voltage
		self.spare_voltage = voltage
		
	def add_name(self, name):
		self.name = name
	
	# checks whether a house can be added and adds if possible
	def add_house(self, house):
	
		if self.spare_voltage > house.voltage:
			house.add_battery(self.name)
			self.spare_voltage -= house.voltage
			return True
		else:
			return False
