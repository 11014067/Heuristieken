# It's a me! Jasper!
# This function links the houses to the batteries, both sorted in wanted order.

import random

def sorting_algorithm(all_info):
	
	# sort the lists as wanted
	print ("Sorting...")
	if (all_info.battery_sort == "random"):
		all_info.batteries = random.sample(all_info.batteries, len(all_info.batteries))
	elif (all_info.battery_sort != "voltage"):
		all_info.batteries = sorted(all_info.batteries, key=lambda battery: getattr(battery, all_info.battery_sort))
	else:
		all_info.batteries = sorted(all_info.batteries, key=lambda battery: -battery.voltage)
	
	if (all_info.house_sort == "random"):
		all_info.houses = random.sample(all_info.houses, len(all_info.houses))
	elif (all_info.house_sort != "voltage"):
		all_info.houses = sorted(all_info.houses, key=lambda house: getattr(house, all_info.house_sort))
	else:
		all_info.houses = sorted(all_info.houses, key=lambda house: -house.voltage)
	
	# link houses and batteries
	for house in all_info.houses:
		house_placed = False
		i = 0
		while (house_placed == False):
			if (all_info.batteries[i].add_house(house)):
				house_placed = True
			i+=1
			# if imposible to solve, break
			if (i > len(all_info.batteries) - 1 and house_placed == False):
				all_info.solution = False
				break
	
	return all_info