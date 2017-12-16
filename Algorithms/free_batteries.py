# calculate densly packed areas of houses to put batteries.
from Classes.neighborhood_classes import Neighborhood_class
import csv
import os
import random

def free_batteries(all_info): 

	# make a list with coordinates
	list_co = []
	coordinates = [0, 5, 10, 15, 20, 25, 30, 35, 40]
	x = 0
	y = 0
	
	# calculate the house density for the coordinates
	breakLoop = False
	while breakLoop == False:
		houses_amount = 0
		for house in all_info.houses:
			if (house.x - coordinates[x]) >= 0 and (house.x - coordinates[x]) < 10 and 
				(house.y - coordinates[y]) >= 0  and (house.y - coordinates[y]) < 10:
				houses_amount += 1
		list_co.append([coordinates[x], coordinates[y], houses_amount])
		x += 1
		
		# if x has gone through all the coordinates, make x zero again and go to the next y coordinate, stop if y is also through the coordinates
		if x == len(coordinates):
			if y == len(coordinates) - 1:
				breakLoop = True
			else:
				x = 0
				y += 1
	
	# sort the list on density
	list_co = sorted(list_co, key=lambda listCo: -listCo[2])

	# make sure the battery is not on a house and they arent to close to eachother
	for i in range(0, len(all_info.batteries)):
		x_coor = list_co[i][0]
		y_coor = list_co[i][1]
		fix_coor = False
		while fix_coor == False:
			fix_coor2 = False
			while fix_coor2 == False:
				for house in all_info.houses :
					
					# if the battery is on a house, randomly change it one position.
					if house.x == x_coor and house.y == y_coor:
						a = random.sample([1, 2], 1)[0]
						if a == 1:
							if x_coor == 50:
								x_coor = 49
							elif x_coor == 0:
								x_coor = 1
							else :
								x = random.sample([-1, 1], 1)[0]
								x_coor += x
						else :
							if y_coor == 50:
								y_coor = 49
							elif y_coor == 0:
								y_coor = 1
							else :
								x = random.sample([-1, 1], 1)[0]
								y_coor += x
						fix_coor2 = True
				fix_coor = True
				fix_coor2 = True
		
		# append the chosen battery coordinate
		all_info.battery_coordinates.append([x_coor, y_coor])
		remove_list = []
		
		# if there are more then 9 batteries wanted, lessen the border to always have a solution
		if len(all_info.batteries) > 9:
			border = 1
		else:
			border = 6
		
		# remove other battery coordinates within the list that are to close to the chosen one
		for list_object in list_co:
			if abs(list_object[0] - x_coor) < border and abs(list_object[1] - y_coor) < border:
				remove_list.append(list_object)
		for list_object in remove_list:
			list_co.remove(list_object)
	
	# store the new batteries
	def fillBatteries(data_battery, i):
		new_battery = Neighborhood_class.Battery(data_battery[0], data_battery[1], all_info.battery_voltages[i])
		return new_battery
	
	all_info.batteries = []
	for i in range(0, len(all_info.battery_coordinates)):
		all_info.batteries.append(fillBatteries(all_info.battery_coordinates[i], i))
		all_info.batteries[i].add_name(i)
	
	return all_info