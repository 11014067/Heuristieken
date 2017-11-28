import csv
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png
from switcher import switching_algorithm

# start the cable length
cable_length = 0

# define classes
class House:

	def __init__(self, x, y, voltage, id):
		self.x = x
		self.y = y
		self.voltage = voltage
		self.battery_no = None
		self.placed = False
		self.id = id

	def add_battery(self, battery_no):
		self.battery_no = battery_no
		self.placed = True

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
		
			
# HOUSE PART
# download the raw house data in a list			
xyvolt= []
with open('Wijk_informatie/wijk1_huizen.csv', 'rb') as csvfile:
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

# BATERY PART
# download the raw battery data in a list		
raw_battery = []
file =  open('Wijk_informatie/wijk1_batterijen.txt', 'r')
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
	batteries[i].add_name(i + 1)
	print("Battery {} on index {} has x = {}".format(batteries[i].name, i, batteries[i].x))

batteries = sorted(batteries, key=lambda battery: battery.y)
houses = sorted(houses, key=lambda house: house.id)

distance0list = []
distance1list = []
distance2list = []
distance3list = []
distance4list = []

for house in houses:
	distance0 = abs(house.x - batteries[0].x) + abs(house.y - batteries[0].y)
	distance1 = abs(house.x - batteries[1].x) + abs(house.y - batteries[1].y)
	distance2 = abs(house.x - batteries[2].x) + abs(house.y - batteries[2].y)
	distance3 = abs(house.x - batteries[3].x) + abs(house.y - batteries[3].y)
	distance4 = abs(house.x - batteries[4].x) + abs(house.y - batteries[4].y)
	distance0list.append([distance0, house.id])
	distance1list.append([distance1, house.id])
	distance2list.append([distance2, house.id])
	distance3list.append([distance3, house.id])
	distance4list.append([distance4, house.id])

def numeric_compare(x, y):
    return x - y
	
distance0list = sorted(distance0list, key=lambda x: x[0])
distance1list = sorted(distance1list, key=lambda x: x[0])
distance2list = sorted(distance2list, key=lambda x: x[0])
distance3list = sorted(distance3list, key=lambda x: x[0])
distance4list = sorted(distance4list, key=lambda x: x[0])

distanceslists = [distance0list, distance1list, distance2list, distance3list, distance4list]

b = [0,0,0,0,0]
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
					b[j] = 149
					placeHouse = True
				elif houses[distanceslists[j][b[j]][1]].placed == False:
					if battery.add_house(houses[distanceslists[j][b[j]][1]]):
						#house placed op true
						placednum += 1
						placeHouse = True
				b[j] += 1
		j += 1
	if b[0] == 150 and b[1] == 150 and b[2] == 150 and b[3] == 150 and b[4] == 150:
		print(" UNSUCCESFULL ")
		break
		
for house in houses:
	if house.battery_no:
		print("huis {} batterij {} voltage {}".format(house.id, house.battery_no, house.voltage))
	else:
		print house.voltage
for battery in batteries:
	print("batterij over {}".format(battery.spare_voltage))
	
solution = switching_algorithm(batteries, houses)
batteries = solution[0]
houses = solution[1]


# DRAWING PART
# get the house image
house = read_png('Wijk_informatie/house.png')
house_img = OffsetImage(house, zoom = .05)

# get the battery image
battery = read_png('Wijk_informatie/battery.png')
battery_img = OffsetImage(battery, zoom = .05)

# make a subplot to allow for add_artist
ax = plt.subplot(111)
	
cable_length = 0;

colors = ['b', 'r', 'y', 'c', 'g']
for house in houses:
	h_x = house.x
	h_y = house.y
	b_x = next(battery for battery in batteries if battery.name == house.battery_no).x
	b_y = next(battery for battery in batteries if battery.name == house.battery_no).y
	
	# give them the img with colored border
	ab = AnnotationBbox(house_img, [house.x, house.y],
	xybox=(0, 0),
	xycoords='data',
	boxcoords="offset points",
	bboxprops = dict(ec=colors[house.battery_no - 1]))                                  
	ax.add_artist(ab)

	# the Y coordinate line (keeps its x coordinate)
	plt.plot([h_x, h_x], [h_y, b_y], color=colors[house.battery_no - 1], linestyle='-')
	cable_length += abs(b_y - h_y)
	# the X coordinate line
	plt.plot([h_x, b_x], [b_y, b_y], color = colors[house.battery_no - 1], linestyle='-')
	cable_length += abs(b_x - h_x)

for battery in batteries:

	# add the battery images
	for battery in batteries:
		ab = AnnotationBbox(battery_img, [battery.x, battery.y],
		xybox=(0, 0),
		xycoords='data',
		boxcoords="offset points",
		bboxprops = dict(ec=colors[battery.name - 1]))                                  
		ax.add_artist(ab)
	
print cable_length

# make the major and minor grid
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.xlabel("x")
plt.ylabel("y")
plt.axis([0, 50, 0, 50])
plt.xticks([0, 10, 20, 30, 40, 50])
plt.yticks([0, 10, 20, 30, 40, 50])
plt.text(15, 55, "Cable length is " + str(cable_length))

plt.show()