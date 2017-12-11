class Neighborhood_class:

	def __init__(self):
		self.houses = []
		self.batteries = []
	
	def try_out(self):
		print("Hoi!")
	
	def get_houses(self):
		return(self.houses)
	
	def get_batteries(self):
		return(self.batteries)
	
	def show_houses(self):
		very_long_string = ""
		for house in self.houses:
			very_long_string += "House " + str(house.id) + " on (" + str(house.x) + "," + str(house.y) + ") with voltage " + str(house.voltage) + " connected to battery " + str(house.battery_no) + ". \n" 
		return very_long_string