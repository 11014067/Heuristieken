
class Neighborhood_class:
	
	class House:
		
		houses = []
		
		def __init__(self, x, y, voltage, id):
			self.x = x
			self.y = y
			self.voltage = voltage
			self.id = id
			self.battery_no = -1
			self.placed = False
			self.id = id
			self.houses.append(self)
	
		def add_battery(self, battery_no):
			self.battery_no = battery_no
			self.placed = True
			
		def get_houses():
			return(self.houses)
	
	class Battery:
	
		batteries = []
	
		def __init__(self, x, y, voltage):	
			self.x = x
			self.y = y
			self.voltage = voltage
			self.spare_voltage = voltage
			self.batteries.append(self)
			
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