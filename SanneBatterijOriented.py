import csv
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png

# start the cable length
cable_length = 0

# define classes
class House:

	def __init__(self, x, y, voltage, id):
		self.x = x
		self.y = y
		self.voltage = voltage
		self.battery_no = None
		self.distance0 = 0
		self.distance1 = 0
		self.distance2 = 0
		self.distance3 = 0
		self.distance4 = 0
		self.placed = False
		self.id = id

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

#
# voeg ID toe
#			
			
# HOUSE PART
# download the raw house data in a list			
xyvolt= []
with open('wijk1_huizen.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	i = 0
	for row in reader:
		if row[0] != "x":
			xyvolt.append([int(row[0]), int(row[1]), float(row[2]), int(i)])
	i += 1

# stores the data into classes
def fillHouses(xy_house):
	new_house = House(xy_house[0], xy_house[1], xy_house[2], xy_house[3])
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
file =  open('wijk1_batterijen.txt', 'r')
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

batteries = sorted(batteries, key=lambda battery: battery.x)
houses = sorted(houses, key=lambda house: house.x)

distance0list = []
distance1list = []
distance2list = []
distance3list = []
distance4list = []

for house in houses:
	house.distance0 = abs(house.x - batteries[0].x) + abs(house.y - batteries[0].y)
	house.distance1 = abs(house.x - batteries[1].x) + abs(house.y - batteries[1].y)
	house.distance2 = abs(house.x - batteries[2].x) + abs(house.y - batteries[2].y)
	house.distance3 = abs(house.x - batteries[3].x) + abs(house.y - batteries[3].y)
	house.distance4 = abs(house.x - batteries[4].x) + abs(house.y - batteries[4].y)
	distance0list.append(house.distance0)
	distance1list.append(house.distance1)
	distance2list.append(house.distance2)
	distance3list.append(house.distance3)
	distance4list.append(house.distance4)

def numeric_compare(x, y):
    return x - y
distance0list = sorted(distance0list, cmp=numeric_compare)
distance1list = sorted(distance1list, cmp=numeric_compare)
distance2list = sorted(distance2list, cmp=numeric_compare)
distance3list = sorted(distance3list, cmp=numeric_compare)
distance4list = sorted(distance4list, cmp=numeric_compare)
	
placednum = 0

# place all the houses
while placednum < 150:
	# pass the batteries
	j = 0
	for battery in batteries:
		# only try to add if it has spare voltage
		if battery.spare_voltage > 0:
			# place the first posible house
			placeHouse = False
			while placeHouse == False:
				if b[j] == 150:
					placeHouse = True
					b[5] += 1
				elif housesa[j][b[j]].placed == False:
					battery.add_house(housesa[j][b[j]])
					placednum += 1
					placeHouse = True
				b[j] += 1
		j += 1
	if b[5] == 4:
		print(" UNSUCCESFULL ")
		break

	
# DRAWING PART
# get the house image
house = read_png('house.png')
house_img = OffsetImage(house, zoom = .05)

# get the battery image
battery = read_png('battery.png')
battery_img = OffsetImage(battery, zoom = .05)

# make a subplot to allow for add_artist
ax = plt.subplot(111)
	
cable_length = 0;

colors = ['b', 'r', 'y', 'c', 'g']
for house in houses:
	h_x = house.x
	h_y = house.y
	print (" HERE ")
	b_x = next(battery for battery in batteries if battery.name == house.battery_no).x
	b_y = next(battery for battery in batteries if battery.name == house.battery_no).y
	
	# give them the img with colored border
	ab = AnnotationBbox(house_img, [house.x, house.y],
		xybox=(0, 0),
		xycoords='data',
		boxcoords="offset points",
		bboxprops = dict(ec=colors[house.battery_no]))                                  
	ax.add_artist(ab)

	# the Y coordinate line (keeps its x coordinate)
	plt.plot([h_x, h_x], [h_y, b_y], color=colors[house.battery_no], linestyle='-')
	cable_length += abs(b_y - h_y)
		# the X coordinate line
	plt.plot([h_x, b_x], [b_y, b_y], color = colors[house.battery_no], linestyle='-')
	cable_length += abs(b_x - h_x)
	
for battery in batteries:
	
	# add the battery images
	for battery in batteries:
		ab = AnnotationBbox(battery_img, [battery.x, battery.y],
			xybox=(0, 0),
			xycoords='data',
			boxcoords="offset points",
			bboxprops = dict(ec=colors[battery.name]))                                  
		ax.add_artist(ab)
		

print cable_length

# make the major and minor grid
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.axis([0, 50, 0, 50])
plt.xticks([0, 10, 20, 30, 40, 50])
plt.yticks([0, 10, 20, 30, 40, 50])
	

# show the plot
plt.show()
