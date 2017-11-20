import csv
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png
from classesWijk import House, Battery
from SortingAlgorithm import sorting_algorithm
from download_data import download_data

# start the cable length
cable_length = 0

# Chose naberhood
wijk = '1'

# DOWNLOAD AND ORDER DATA
information = download_data(wijk)
batteries = information[0]
houses = information[1]
	
# ALGORITHM
# chose the sorting method for batteries and houses
information = sorting_alogrithm(batteries, houses, 'x', 'x')
batteries = information[0]
houses = information[1]
	
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
