import csv
import os
from Classes.neighborhood_classes import House, Battery

def new_batteries(battery_coordinates, battery_size):

	# stores the data into classes
	def fillBatteries(data_battery, i):
		new_battery = Battery(data_battery[0], data_battery[1], battery_size[0])
		return new_battery
	
	batteries = []
	for i in range(0, len(battery_coordinates)):
		batteries.append(fillBatteries(battery_coordinates[i], i))
		batteries[i].add_name(i)
		print("WOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOWOW")
		print("Battery {} on index {} has x = {}".format(batteries[i].name, i, batteries[i].x))
	return batteries