import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png

# make a subplot to allow for add_artist
ax = plt.subplot(111)

# get the house image
house = read_png('house.png')
houseimg = OffsetImage(house, zoom=.1)

# get the house coordinates
xy = []

# create classes
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
		
# get the house voltage output next to coordinates
xyvolt= []

# store houses
with open('wijk1_huizen.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader:
		if row[0] != "x":
			xy.append([int(row[0]), int(row[1]))
			xyvolt.append([int(row[0]), int(row[1]), int(row[2]))

# function to creat a new class				       
def fillHouses(xy_house):
	new_house = House(xy_house[0], xy_house[1], xy_house[2])
	return new_house

# create array of houses
houses = []
for i in range(0, len(xyvolt)):
	houses.append(fillHouses(xyvolt[i]))
	
#for i in range(0, len(xyvolt)):	
#	print("Huis {} heeft x = {} en y = {} en volt = {}".format(i, houses[i].x, houses[i].y, houses[i].voltage))

# get data for batteries				       
raw_battery = []

file =  open('wijk1_batterijen.txt', 'r')
for line in file: 
	if(line.split("\t")[0] != "pos"):
		raw_battery.append([line.split("\t")[0], (line.split("\t")[-1].rstrip())])   

# add the house image to the coordinates
for row in xy:
	ab = AnnotationBbox(houseimg, row,
		xybox=(0, 0),
		xycoords='data',
		boxcoords="offset points")                                  
	ax.add_artist(ab)

# make the major and minor grid
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.axis([0, 50, 0, 50])
plt.xticks([0, 10, 20, 30, 40, 50])
plt.yticks([0, 10, 20, 30, 40, 50])

# show the plot
plt.show()
