# Remake the batteries on the new coordinates.

import csv
import os
from Classes.neighborhood_classes import Neighborhood_class

def new_batteries(all_info):

	# stores the data into classes
	def fillBatteries(data_battery, i):
		new_battery = Neighborhood_class.Battery(data_battery[0], data_battery[1], all_info.battery_voltages[i])
		return new_battery
	
	# create the battery list again
	all_info.batteries = []
	for i in range(0, len(all_info.battery_coordinates)):
		all_info.batteries.append(fillBatteries(all_info.battery_coordinates[i], i))
		all_info.batteries[i].add_name(i)
	
	return all_info