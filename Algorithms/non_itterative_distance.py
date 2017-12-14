# This function links the batteries one by one to a home that has the smallest distance to that battery.

from Functions.switcher import switching_algorithm
import random
import time

def non_itterative_distance(all_info):
	
	# sort the batteries and houses
	print ("Sorting...")
	all_info.batteries = sorted(all_info.batteries, key=lambda battery: battery.id)
	all_info.houses = sorted(all_info.houses, key=lambda house: house.id)
	
	# make a list for each battery with the distance to the houses and its id
	dict_list = {}
	for i in range(0, len(all_info.batteries)):
		dict_list["distance" + str(i) + "list"] = []
		
	for house in all_info.houses:
		for i in range(0, len(all_info.batteries)):
			dict_list["distance" + str(i) + "list"].append([abs(house.x - all_info.batteries[i].x) + abs(house.y - all_info.batteries[i].y), house.id])

	# sort the lists from shortest distance to longest		
	for i in range(0, len(all_info.batteries)):
		dict_list["distance" + str(i) + "list"] = sorted(dict_list["distance" + str(i) + "list"], key=lambda x: x[0])
	
	# save the indexes and how many houses are placed
	index_list = [0] * len(all_info.batteries)
	distance_list = [0] * len(all_info.batteries)
	houses_to_place = len(all_info.houses)
	
	# place all the houses
	while (houses_to_place > 0):
		for j in range(0, len(all_info.batteries)):
			
			# see what the first posible house is to place
			place_house = False
			while (place_house == False):
				if (index_list[j] == len(all_info.houses)):
					index_list[j] = len(all_info.houses) - 1
					distance_list[j] = [10000, 1]
					# if there are no houses left to place, go to the next battery
					place_house = True
				elif (all_info.houses[dict_list["distance" + str(j) + "list"][index_list[j]][1]].placed == False) and (all_info.houses[dict_list["distance" + str(j) + "list"][index_list[j]][1]].voltage > all_info.batteries[j].spare_voltage) :
					distance_list[j] = dict_list["distance" + str(j) + "list"][index_list[j]]
					place_house = True
				else :
					index_list[j] += 1
		
		# check which battery has the closes house and place it
		index = [0, [100, 0]]
		print(distance_list[0])
		for k in range (0, len(distance_list)):
			if distance_list[k][0] < index[1][0]:
				index = [k, distance_list[k]]
		
		if all_info.batteries[j].add_house(all_info.houses[dict_list["distance" + str(index[0]) + "list"][index_list[index[0]]][1]]):
			houses_to_place -= 1
		
		# check if it is posible to link more houses, if not break			
		sum_index_list = 0
		for i in range(0, len(all_info.batteries)):
			sum_index_list += index_list[i]
		if (sum_index_list == len(all_info.houses) * len(all_info.batteries)):
			all_info.solution = False
			print(" UNSUCCESFULL ")
			return all_info

	return all_info