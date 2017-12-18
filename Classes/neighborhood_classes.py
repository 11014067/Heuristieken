# This class holds all the information to a neighborhood.

class Neighborhood_class:
	
	# save all the necassery information
	def __init__(self, choice):
		self.batteries = []
		self.battery_sort = ""
		self.battery_voltages = []
		self.choice = choice
		self.cost = ""
		self.cable_length = ""
		self.houses = []
		self.house_sort = ""
		self.neighborhood = ""
		self.solveable = False
		self.solution = True
		self.sorting_method = ""
		
		# get more variables with the long version
		if (choice == "long"):
			self.battery_coordinates = []
			self.free = ""
			self.improve = "no"
			self.hill_climber = ""
			self.iterations = 0
			self.lower_bounds = 0
			self.upper_bounds = 9999999
	
	# print the information about the houses
	def show_houses(self):
		very_long_string = ""
		for house in self.houses:
			very_long_string += "House " + str(house.id) + " on (" + str(house.x) + "," + str(house.y) + ") with voltage " + str(house.voltage) + " connected to battery " + str(house.battery_no) + ". \n" 
		print(very_long_string)
	
	# print the information about the batteries
	def show_batteries(self):
		very_long_string = ""
		for battery in self.batteries:
			very_long_string += "Battery " + str(battery.id) + " on (" + str(battery.x) + "," + str(battery.y) + ") with voltage " + str(battery.spare_voltage) + "/" + str(battery.voltage) + ", connected to houses" 
			for house in battery.houses_list:
				very_long_string += str(house.id) + ", "
			very_long_string += "\n"
		print(very_long_string)
		
	# class with house information
	class House:
		
		# save all the necassery information
		def __init__(self, x, y, voltage, id):
			self.x = x
			self.y = y
			self.voltage = voltage
			self.id = id
			self.battery_no = -1
			self.placed = False
	
		def add_battery(self, battery_no):
			self.battery_no = battery_no
			self.placed = True
		
	# class with battery information	
	class Battery:
	
		# save all the necassery information
		def __init__(self, x, y, voltage):	
			self.x = x
			self.y = y
			self.voltage = voltage
			self.spare_voltage = voltage
			self.houses_list = []
			
		def add_name(self, id):
			self.id = id
		
		# checks whether a house can be added and adds if possible
		def add_house(self, house):
		
			if self.spare_voltage > house.voltage and house.placed == False:
				house.add_battery(self.id)
				self.houses_list.append(house)
				self.spare_voltage -= house.voltage
				return True
			else:
				return False

