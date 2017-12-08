from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png
import matplotlib.pyplot as plt
import math

def plot_grid(houses, batteries, cable_length, cost_of_neighborhood):

	# DRAWING PART
	# get the house image
	house = read_png('Information/house.png')
	house_img = OffsetImage(house, zoom = .05)
	
	# get the battery image
	battery = read_png('Information/battery.png')
	battery_img = OffsetImage(battery, zoom = .05)
	
	# make a subplot to allow for add_artist
	ax = plt.subplot(111)
	
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
	
		# the X coordinate line
		plt.plot([h_x, b_x], [b_y, b_y], color = colors[house.battery_no], linestyle='-')
	
	
	# add the battery images
	for battery in batteries:
		ab = AnnotationBbox(battery_img, [battery.x, battery.y],
			xybox=(0, 0),
			xycoords='data',
			boxcoords="offset points",
			bboxprops = dict(ec=colors[battery.name]))                                  
		ax.add_artist(ab)
	
	# make the major and minor grid
	plt.grid(b=True, which='major', color='k', linestyle='-')
	plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
	plt.minorticks_on()
	plt.xlabel("x")
	plt.ylabel("y")
	plt.axis([0, 50, 0, 50])
	plt.xticks([0, 10, 20, 30, 40, 50])
	plt.yticks([0, 10, 20, 30, 40, 50])
	plt.text(10, 55, "Cable length is " + str(cable_length))
	plt.text(35, 55, "Price is " + str(cost_of_neighborhood))
	
	batteries = sorted(batteries, key=lambda battery: -battery.name)
	a = 5
	for battery in batteries:
		plt.text(51, a, str(battery.name) + ": " + str(battery.voltage))
		a += 10
	
	return plt