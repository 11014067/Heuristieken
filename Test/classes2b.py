
class Neighborhood_class:
	houses = []
	batteries = []
	
	class House:
	
		def __init__(self, x, y, voltage, id):
			self.x = x
			self.y = y
			self.voltage = voltage
			self.id = id
			self.battery_no = -1
			self.placed = False
			self.id = id
			Neighborhood_class.houses.append(self)
	
		def add_battery(self, battery_no):
			self.battery_no = battery_no
			self.placed = True
			
	class Battery:
	
		def __init__(self, x, y, voltage):	
			self.x = x
			self.y = y
			self.voltage = voltage
			self.spare_voltage = voltage
			Neighborhood_class.batteries.append(self)
			
		def add_name(self, id):
			self.id = id
		
		# checks whether a house can be added and adds if possible
		def add_house(self, house):
		
			if self.spare_voltage > house.voltage:
				house.add_battery(self.id)
				self.spare_voltage -= house.voltage
				return True
			else:
				return False