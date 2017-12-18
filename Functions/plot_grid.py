# Plots a grid as visualisation for the neighborhood.

from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib._png import read_png
import matplotlib.pyplot as plt
import math

def plot_grid(all_info):

	# get the house image
	house = read_png('Information/house.png')
	house_img = OffsetImage(house, zoom = .05)
	
	# make a subplot to allow for add_artist
	ax = plt.subplot(111)
	
	# draw the cables
	colors = ['b', 'r', 'y', 'c', 'g', '#777777', '#000000', '#ef7700', '#8b00ef']
	for house in all_info.houses:
		h_x = house.x
		h_y = house.y
		b_x = next(battery for battery in all_info.batteries if battery.id == house.battery_no).x
		b_y = next(battery for battery in all_info.batteries if battery.id == house.battery_no).y
		
		# give them the img with colored border
		ab = AnnotationBbox(house_img, [house.x, house.y],
			xybox=(0, 0),
			xycoords='data',
			boxcoords="offset points",
			bboxprops = dict(ec=colors[house.battery_no]))                                  
		ax.add_artist(ab)

		# draw the lines
		plt.plot([h_x, h_x], [h_y, b_y], color=colors[house.battery_no], linestyle='-')
		plt.plot([h_x, b_x], [b_y, b_y], color = colors[house.battery_no], linestyle='-')
	
	
	# add the battery images
	for battery in all_info.batteries:
		ax.plot(battery.x, battery.y, 's', color=colors[battery.id], markersize=10)                             
		
	# make the major and minor grid
	plt.grid(b=True, which='major', color='k', linestyle='-')
	plt.grid(b=True, which='minor', color='k', linestyle='-', alpha=0.2)
	plt.minorticks_on()
	plt.xlabel("x")
	plt.ylabel("y")
	plt.axis([0, 50, 0, 50])
	plt.xticks([0, 10, 20, 30, 40, 50])
	plt.yticks([0, 10, 20, 30, 40, 50])
	
	# add the text
	plt.text(10, 55, "Cable length is " + str(all_info.cable_length))
	plt.text(35, 55, "Price is " + str(all_info.cost))
	
	# add the size of the batteries
	all_info.batteries = sorted(all_info.batteries, key=lambda battery: -battery.id)
	a = 5
	for battery in all_info.batteries:
		plt.text(51, a, str(battery.id) + ": " + str(battery.voltage))
		a += 10
	
	return plt