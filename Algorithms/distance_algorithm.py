# This function links the batteries one by one to a home that has the smallest distance to that battery.

from Functions.switcher import switching_algorithm
import random
import time

def distance_algorithm(all_info):

	# sort the houses and batteries
	if all_info.battery_sort == "random":
		all_info.batteries = random.sample(all_info.batteries, len(all_info.batteries))
	elif all_info.battery_sort != "voltage":
		all_info.batteries = sorted(all_info.batteries, key=lambda battery: getattr(battery, all_info.battery_sort))
	else:
		all_info.batteries = sorted(all_info.batteries, key=lambda battery: -battery.voltage)
	
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
	houses_to_place = len(all_info.houses)
	
	# place all the houses
	while houses_to_place > 0:
		for j in range(0, len(all_info.batteries)):
		
			# only try to add if it has spare voltage
			if all_info.batteries[j].spare_voltage > 0:
			
				# place the first posible house
				place_house = False
				while place_house == False:
				
					# if there are no houses left to place, go to the next battery
					if index_list[j] == len(all_info.houses):
						index_list[j] = len(all_info.houses) - 1
						place_house = True
						
					# if posible, place a house	
					elif all_info.houses[dict_list["distance" + str(j) + "list"][index_list[j]][1]].placed == False:
						if all_info.batteries[j].add_house(all_info.houses[dict_list["distance" + str(j) + "list"][index_list[j]][1]]):
							houses_to_place -= 1
							place_house = True
					index_list[j] += 1
		
		# check if it is posible to link more houses, if not break			
		sum_index_list = 0
		for i in range(0, len(all_info.batteries)):
			sum_index_list += index_list[i]
		if sum_index_list == len(all_info.houses) * len(all_info.batteries):
			all_info.solution = False
			return all_info

	return all_info