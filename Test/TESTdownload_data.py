import csv
import os
from Test.classes2 import Neighborhood_class

def TESTdownload_data(x, battery_size):
	house_file = os.path.normpath('Information/wijk' + x + '_huizen.csv')
	battery_file = os.path.normpath('Information/wijk' + x + '_batterijen.txt')

	
	all_info=Neighborhood_class
	
	# download the raw house data in a list	
	xyvolt= []

	with open(house_file, "rt", encoding="utf8") as csvfile:
		reader = csv.reader(csvfile, delimiter = ",")
		for row in reader:
			if row[0] != "x":
				xyvolt.append([int(row[0]), int(row[1]), float(row[2])])
		
	
	# stores the data into classes
	def fillHouses(xy_house, i):
		new_house = all_info.House(xy_house[0], xy_house[1], xy_house[2], i)
		return new_house
	
	houses = []
	for i in range(0, len(xyvolt)):
		houses.append(fillHouses(xyvolt[i], i))
		
	# download the raw battery data in a list		
	raw_battery = []
	file =  open(battery_file, 'r')
	for line in file: 
		if(line.split("\t")[0] != "pos"):
			list_string = line.split("\t")[0]
			list_string = list_string[1:len(list_string) - 1]
			raw_battery.append([int(list_string.split(",")[0]), int(list_string.split(",")[1])])
	
	# stores the data into classes
	def fillBatteries(data_battery, i):
		new_battery = all_info.Battery(data_battery[0], data_battery[1], battery_size[i])
		return new_battery
	
	batteries = []
	for i in range(0, len(raw_battery)):
		batteries.append(fillBatteries(raw_battery[i], i))
		batteries[i].add_name(i)
		print("Battery {} on index {} has x = {}".format(batteries[i].id, i, batteries[i].x))
		
	sum_houses = 0
	for house in houses:
		sum_houses += house.voltage
	
	sum_batteries = 0
	for battery in batteries:
		sum_batteries += battery.voltage
	
	solveable = False
	if (sum_batteries > sum_houses):
		solveable = True
	return [all_info, solveable]