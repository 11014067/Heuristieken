from Functions.switcher import switching_algorithm
import random
import time

def test_algorithm(all_info):
	# Sort the batteries
	print ("Sorting...")
	if (all_info.battery_sort == "random"):
		all_info.batteries = random.sample(all_info.batteries, len(all_info.batteries))
	elif (all_info.battery_sort != "voltage"):
		all_info.batteries = sorted(all_info.batteries, key=lambda battery: getattr(battery, all_info.battery_sort))
	else:
		all_info.batteries = sorted(all_info.batteries, key=lambda battery: -battery.voltage)
	
	# Sort the houses on id
	all_info.houses = sorted(all_info.houses, key=lambda house: house.id)
	
	dict_list = {}
	for i in range(0, len(all_info.batteries)):
		dict_list["distance" + str(i) + "list"] = []
		
	for house in all_info.houses:
		for i in range(0, len(all_info.batteries)):
			dict_list["distance" + str(i) + "list"].append([abs(house.x - all_info.batteries[i].x) + abs(house.y - all_info.batteries[i].y), house.id])

	for i in range(0, len(all_info.batteries)):
		dict_list["distance" + str(i) + "list"] = sorted(dict_list["distance" + str(i) + "list"], key=lambda x: x[0])
		
	# Save the indexes and how many houses are placed
	index_list = [0] * len(all_info.batteries)
	houses_to_place = len(all_info.houses)
	
	# place all the houses
	while (houses_to_place > 0):
		for j in range(0, len(all_info.batteries)):
			# only try to add if it has spare voltage
			if (all_info.batteries[j].spare_voltage > 0):
				# place the first posible house
				place_house = False
				while (place_house == False):
					if (index_list[j] == len(all_info.houses)):
						index_list[j] = len(all_info.houses) - 1
						# if there are no houses left to place, go to the next battery
						place_house = True
					elif (all_info.houses[dict_list["distance" + str(j) + "list"][index_list[j]][1]].placed == False):
						if (all_info.batteries[j].add_house(all_info.houses[dict_list["distance" + str(j) + "list"][index_list[j]][1]])):
							# house placed op true
							houses_to_place -= 1
							# go to the next battery
							place_house = True
					index_list[j] += 1
		sum_index_list = 0
		if (index_list[(len(all_info.batteries) - 2)] == 150):
			print(" UNSUCCESFULL ")
			break
		for i in range(0, len(all_info.batteries)-1):
			sum_index_list += index_list[i]
		if (sum_index_list == len(all_info.houses) * len(all_info.batteries)):
			print(" UNSUCCESFULL ")
			break
			
	for house in all_info.houses:
		if (house.battery_no > -1):
			print("House number: {}, battery : {}".format(house.id, house.battery_no))
		else:
			print("House {} is {} volt and not linked to a battery".format(house.id, house.voltage))
			
	for battery in all_info.batteries:
		print("batterij over {}".format(battery.spare_voltage))
	
	all_info = switching_algorithm(all_info)
	
	return all_info