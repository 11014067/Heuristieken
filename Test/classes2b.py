
class Neighborhood_class:

	houses = []
	batteries = []
	house_sort = ""
	battery_sort = ""
	neighborhood = ""
	
	def show_houses(self):
		for house in self.houses:
			print("House " + str(house.id) + " on (" + str(house.x) + "," + str(house.y) + ") with voltage " + str(house.voltage) + " connected to battery " + str(house.battery_no) + ".")
	
	def show_batteries(self):
		for battery in self.batteries:
			print("Battery " + str(battery.id) + " has a voltage of " + str(battery.voltage) + " and a spare voltage of " + str(battery.spare_voltage))
		
	def add_house_sort(sort):
		Neighborhood_class.house_sort = sort
		
	def add_battery_sort(sort):
		Neighborhood_class.battery_sort = sort	
		
	def add_neighborhood(neighborhood):
		Neighborhood_class.neighborhood = str(neighborhood)
		
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