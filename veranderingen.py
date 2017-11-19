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
reader =[[1, 8, 10], [9, 4, 10], [5, 6, 10], [6, 3, 10]]
for row in reader:
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
raw_battery = [[8, 6, 100]]
	
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
batteries = sorted(batteries, key=lambda battery: battery.y)
houses = sorted(houses, key=lambda house: house.y)

#for i in range(0,5):
#	print("Battery {} on index {} has x = {}".format(batteries[i].name, i, batteries[i].x))	
	
# link houses and batteries
housenumber = 0
for house in houses:
	unplaced = True
	i = 0
	while unplaced:
		if batteries[i].add_house(house):
			unplaced = False
			# print "House {} is connected to battery {}".format(housenumber, house.battery_no)
		i+=1
	housenumber+=1
	
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
	b_x = next(battery for battery in batteries if battery.name == house.battery_no).x
	b_y = next(battery for battery in batteries if battery.name == house.battery_no).y
	
	# give them the img with colored border
	ab = AnnotationBbox(house_img, [house.x, house.y],
		xybox=(0, 0),
		xycoords='data',
		boxcoords="offset points",
		bboxprops = dict(ec=colors[house.battery_no]))                                  
	ax.add_artist(ab)


	
for battery in batteries:
	
	# add the battery images
	for battery in batteries:
		ab = AnnotationBbox(battery_img, [battery.x, battery.y],
			xybox=(0, 0),
			xycoords='data',
			boxcoords="offset points",
			bboxprops = dict(ec=colors[battery.name]))                                  
		ax.add_artist(ab)
		
	cable_length += abs(battery.max_x - battery.min_x)

plt.plot([1, 8], [8, 8], color=colors[house.battery_no], linestyle='-')
plt.plot([8, 8], [6, 8], color=colors[house.battery_no], linestyle='-')

plt.plot([5, 8], [6, 6], color=colors[house.battery_no], linestyle='-')

plt.plot([8, 9], [6, 6], color=colors[house.battery_no], linestyle='-')
plt.plot([9, 9], [4, 6], color=colors[house.battery_no], linestyle='-')

plt.plot([6, 8], [3, 3], color=colors[house.battery_no], linestyle='-')
plt.plot([8, 8], [3, 6], color=colors[house.battery_no], linestyle='-')

print cable_length

# make the major and minor grid
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.axis([0, 10, 0, 10])
plt.xticks([0, 5, 10])
plt.yticks([0, 5, 10])
	

# show the plot
plt.show()