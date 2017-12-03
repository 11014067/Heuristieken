import csv
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png

# start the cable length
cable_length = 0

# define classes
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
		self.max_x = x
		self.voltage = voltage
		self.spare_voltage = voltage
		
	def add_name(self, name):
		self.name = name
	
	# checks whether a house can be added and adds if possible
	def add_house(self, house):
	
		if self.spare_voltage > house.voltage:
			if self.min_x > house.x:
				self.min_x = house.x
				house.add_battery(self.name)
				self.spare_voltage -= house.voltage
				return True
			elif self.max_x < house.x:
				self.max_x = house.x
				house.add_battery(self.name)
				self.spare_voltage -= house.voltage
				return True
			else:
				house.add_battery(self.name)
				self.spare_voltage -= house.voltage
				return True
		else:
			return False

# HOUSE PART
# download the raw house data in a list			
xyvolt= []
with open('wijk3_huizen.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader:
		if row[0] != "x":
			xyvolt.append([int(row[0]), int(row[1]), float(row[2])])

# stores the data into classes
def fillHouses(xy_house):
	new_house = House(xy_house[0], xy_house[1], xy_house[2])
	return new_house

houses = []
for i in range(0, len(xyvolt)):
	houses.append(fillHouses(xyvolt[i]))

## CHECK	
#for i in range(0, 5):	
#	print("Huis {} heeft x = {} en y = {} en battery = {}".format(i, houses[i].x, houses[i].y, houses[i].battery_no))
	
# BATERY PART
# download the raw battery data in a list		
raw_battery = []
file =  open('wijk3_batterijen.txt', 'r')
for line in file: 
	if(line.split("\t")[0] != "pos"):
		list_string = line.split("\t")[0]
		list_string = list_string[1:len(list_string)-1]
		raw_battery.append([int(list_string.split(",")[0]), int(list_string.split(",")[1]), float(line.split("\t")[-1].rstrip())])

# stores the data into classes	
def fillBatteries(data_battery):
	new_battery = Battery(data_battery[0], data_battery[1], data_battery[2])
	return new_battery

batteries = []
for i in range(0, len(raw_battery)):
	batteries.append(fillBatteries(raw_battery[i]))
	batteries[i].add_name(i)
	print("Battery {} on index {} has x = {}".format(batteries[i].name, i, batteries[i].x))

print "Sorting..."
batteries = sorted(batteries, key=lambda battery: battery.x)
houses = sorted(houses, key=lambda house: house.x)

maximum = 0
for house in houses:
	longestCable = 0
	for battery in batteries:
		distance = abs(house.x - battery.x) + abs(house.y - battery.y)
		if distance > longestCable:
			longestCable = distance
	maximum += longestCable

print maximum
