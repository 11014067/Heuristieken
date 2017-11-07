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

# get the house coordinates
xy = []
battery = []
cable_length = 0
xy.append([3,13])
xy.append([1,7]) 
xy.append([5,6]) 
xy.append([11,1])
xy.append([15,8])
xy.append([19,12])
xy.append([19,4])
battery.append([11,8])

x_min = 11
x_max = 11

# add the house image to the coordinates
for row in xy:
	ab = AnnotationBbox(house_img, row,
		xybox=(0, 0),
		xycoords='data',
		boxcoords="offset points")                                  
	ax.add_artist(ab)
	
# add the battery images
for row in battery:
	ab = AnnotationBbox(battery_img, row,
		xybox=(0, 0),
		xycoords='data',
		boxcoords="offset points")                                  
	ax.add_artist(ab)

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

# show the plot
plt.show()
