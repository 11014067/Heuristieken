class Neighborhood_class:

	def __init__(self):
		self.houses = []
		self.batteries = []
		self.upper_bound = 9999999
		self.lower_bound = 0
	
	def get_houses(self):
		return(self.houses)
	
	def get_batteries(self):
		return(self.batteries)
	
	def show_houses(self):
		very_long_string = ""
		for house in self.houses:
			very_long_string += "House " + str(house.id) + " on (" + str(house.x) + "," + str(house.y) + ") with voltage " + str(house.voltage) + " connected to battery " + str(house.battery_no) + ". \n" 
		print(very_long_string)
		
	def show_batteries(self):
		very_long_string = ""
		for battery in self.batteries:
			very_long_string += "Battery " + str(battery.id) + " on (" + str(battery.x) + "," + str(battery.y) + ") with voltage " + str(battery.spare_voltage) + "/" + str(battery.voltage) + ", connected to houses" 
			for house in battery.houses_list:
				very_long_string += str(house.id) + ", "
			very_long_string += "\n"
		print(very_long_string)
		
	