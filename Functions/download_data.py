# This function downloads the data specified in the input.

import csv
import os
from Classes.neighborhood_classes import Neighborhood_class

def download_data(all_info):
	# download the files
	house_file = os.path.normpath('Information/wijk' + all_info.neighborhood + '_huizen.csv')
	battery_file = os.path.normpath('Information/wijk' + all_info.neighborhood + '_batterijen.txt')

	# download the raw house data in a list	
	xyvolt= []
	with open(house_file, "rt", encoding="utf8") as csvfile:
		reader = csv.reader(csvfile, delimiter = ",")
		for row in reader:
			if row[0] != "x":
				xyvolt.append([int(row[0]), int(row[1]), float(row[2])])
		
	# stores the data in a list in classes
	def fillHouses(xy_house, i):
		new_house = Neighborhood_class.House(xy_house[0], xy_house[1], xy_house[2], i)
		return new_house
	
	for i in range(0, len(xyvolt)):
		all_info.houses.append(fillHouses(xyvolt[i], i))
		
	# download the raw battery data in a list		
	raw_battery = []
	file =  open(battery_file, 'r')
	for line in file: 
		if(line.split("\t")[0] != "pos"):
			list_string = line.split("\t")[0]
			list_string = list_string[1:len(list_string) - 1]
			raw_battery.append([int(list_string.split(",")[0]), int(list_string.split(",")[1])])
	
	# stores the data in a list in classes
	def fillBatteries(data_battery, i):
		new_battery = Neighborhood_class.Battery(data_battery[0], data_battery[1], all_info.battery_voltages[i])
		return new_battery
	
	for i in range(0, len(raw_battery)):
		all_info.batteries.append(fillBatteries(raw_battery[i], i))
		all_info.batteries[i].add_name(i)
		print("Battery {} on index {} has x = {}".format(all_info.batteries[i].id, i, all_info.batteries[i].x))
	
	# calculate the sum of needed and available amount voltage
	sum_houses = 0
	for house in all_info.houses:
		sum_houses += house.voltage
	sum_batteries = 0
	for battery in all_info.batteries:
		sum_batteries += battery.voltage
	
	# see if the problem is solveable
	print(sum_houses, sum_batteries)
	if (sum_batteries > sum_houses):
		all_info.solveable = True
		
	return all_info