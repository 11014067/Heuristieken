import csv

class House:

	def __init__(self, x, y, voltage):
		self.x = x
		self.y = y
		self.voltage = voltage
		self.battery_no = None

	def add_battery(self, battery_no):
		self.battery_no = battery_no	

class Battery:

	def __init__(self, x, y, voltage):	
		self.x = x
		self.y = y
		self.min_x = x
		self.min_y = y
		self.voltage = voltage
		self.spare_voltage = voltage
#usedvoltage
		

xyvolt= []

with open('wijk1_huizen.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader:
		if row[0] != "x":
			xyvolt.append([int(row[0]), int(row[1]), (row[2])])

def fillHouses(xy_house):
	new_house = House(xy_house[0], xy_house[1], xy_house[2])
	return new_house

houses = []
for i in range(0, len(xyvolt)):
	houses.append(fillHouses(xyvolt[i]))
	
for i in range(0, len(xyvolt)):	
	print("Huis {} heeft x = {} en y = {} en volt = {}".format(i, houses[i].x, houses[i].y, houses[i].voltage))
	
