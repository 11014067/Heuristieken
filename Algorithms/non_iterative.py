# This function links the batteries one by one to a home that has the smallest distance to that battery.

from Functions.switcher import switching_algorithm
import random
import time

def non_iterative(all_info):
	
	# sort the batteries and houses
	all_info.batteries = sorted(all_info.batteries, key=lambda battery: battery.id)
	all_info.houses = sorted(all_info.houses, key=lambda house: house.id)
	
	# make a list for each battery with the distance to the houses and its id
	dict_list = []
	for house in all_info.houses:
		for i in range(0, len(all_info.batteries)):
			dict_list.append([(abs(house.x - all_info.batteries[i].x) + abs(house.y - all_info.batteries[i].y)), house.id, i])

	# sort the lists from shortest distance to longest		
	dict_list = sorted(dict_list, key=lambda x: x[0])
	
	# place all the houses
	for j in range(len(dict_list)):
		all_info.batteries[dict_list[j][2]].add_house(all_info.houses[dict_list[j][1]])

	# check if all the houses are placed
	for house in all_info.houses:
		if house.placed == False:
			all_info.solution = False
			return all_info
		
	return all_info