import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png

# make a subplot to allow for add_artist
ax = plt.subplot(111)

# get the house image
house = read_png('house.png')
house_img = OffsetImage(house, zoom = .1)

# get the battery image
battery = read_png('battery.png')
battery_img = OffsetImage(battery, zoom = .01)

# get the houses
xy = []
with open('wijk1_huizen.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	for row in reader:
		if row[0] != "x":
			xy.append([int(row[0]), int(row[1])])

# get the batteries
battery = []

file =  open('wijk1_batterijen.txt', 'r')
for line in file: 
	if(line.split("\t")[0] != "pos"):
		battery.append([line.split("\t")[0], (line.split("\t")[-1].rstrip())])   

# start the cable length
cable_length = 0

battery = []
battery.append([3,3])

# make the x min and max
x_min = battery[0][0]
x_max = battery[0][0]

# add the house image to the coordinates
for row in xy:
	ab = AnnotationBbox(house_img, row,
		xybox=(0, 0),
		xycoords='data',
		boxcoords="offset points",
		bboxprops = dict(ec='r'))                                  
	ax.add_artist(ab)
	
# add the battery images
for row in battery:
	ac = AnnotationBbox(battery_img, row,
		xybox=(0, 0),
		xycoords='data',
		boxcoords="offset points",
		bboxprops = dict(ec='b'))                                  
	ax.add_artist(ac)
	
# create and calculate the lines
for row in xy:
	h_x = row[0]
	h_y = row[1]
	b_x = battery[0][0]
	b_y = battery[0][1]

	# the Y coordinate line (keeps its x coordinate)
	plt.plot([h_x, h_x], [h_y, b_y], color='b', linestyle='-')
	cable_length += abs(b_y - h_y)

	# the X coordinate line (keeps its y coordinate)
	# if the x value is the new x_min
	if (x_min > h_x):
		x_min = h_x
	# else
	elif (x_max < h_x):
		x_max = h_x
	
# calculate and draw the line X coordinate line
cable_length += (x_max - x_min)
plt.plot([x_min, x_max],[b_y, b_y], color='g', linestyle='-')

# make the major and minor grid
plt.grid(b=True, which='major', color='k', linestyle='-')
plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
plt.minorticks_on()
plt.axis([0, 50, 0, 50])
plt.xticks([0, 10, 20, 30, 40, 50])
plt.yticks([0, 10, 20, 30, 40, 50])

print "The cable length is:"
print cable_length

# show the plot
plt.show()