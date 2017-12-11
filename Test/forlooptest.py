from Functions.switcher import switching_algorithm
import random
import time

def test_algorithm(batteries, houses, sort_battery):
	# Sort the batteries
	print ("Sorting...")
	if (sort_battery == "random"):
		batteries = random.sample(batteries, len(batteries))
	elif (sort_battery != "voltage"):
		batteries = sorted(batteries, key=lambda battery: getattr(battery, sort_battery))
	else:
		batteries = sorted(batteries, key=lambda battery: -battery.voltage)
	
	# Sort the houses on id
	houses = sorted(houses, key=lambda house: house.id)
	
	dict_list = {}
	for i in range(0, len(batteries) - 1):
		dict_list["distance" + str(i) + "list"] = []
		
	for house in houses:
		for i in range(0, len(batteries) - 1):
			dict_list["distance" + str(i) + "list"].append([abs(house.x - batteries[i].x) + abs(house.y - batteries[i].y), house.id])

	for i in range(0, len(batteries) - 1):
		dict_list["distance" + str(i) + "list"] = sorted(dict_list["distance" + str(i) + "list"], key=lambda x: x[0])
		
	# Save the indexes and how many houses are placed
	index_list = [0] * len(batteries)
	houses_to_place = len(houses)
	print (houses_to_place)
	print (dict_list)
	print(len(batteries) -1)
	
	# place all the houses
	while (houses_to_place > 0):
		for j in range(0, len(batteries) -1):
			# only try to add if it has spare voltage
			if (batteries[j].spare_voltage > 0):
				# place the first posible house
				place_house = False
				while (place_house == False):
					if (index_list[j] == len(houses)):
						index_list[j] = len(houses) - 1
						# if there are no houses left to place, go to the next battery
						place_house = True
					elif (houses[dict_list["distance" + str(j) + "list"][index_list[j]][1]].placed == False):
						if (batteries[j].add_house(houses[dict_list["distance" + str(j) + "list"][index_list[j]][1]])):
							# house placed op true
							houses_to_place -= 1
							# go to the next battery
							place_house = True
					index_list[j] += 1
		sum_index_list = 0
		if (index_list[(len(batteries) - 2)] == 150):
			print(" UNSUCCESFULL ")
			break
		for i in range(0, len(batteries)-1):
			sum_index_list += index_list[i]
		if (sum_index_list == len(houses) * len(batteries)):
			print(" UNSUCCESFULL ")
			break
			
	for house in houses:
		if (self.battery_no > -1):
			print("House number: {}, battery : {}".format(self.id, self.battery_no))
		else:
			print("House {} is {} volt and not linked to a battery".format(self.id, self.voltage))
			
	for battery in batteries:
		print("batterij over {}".format(battery.spare_voltage))
	
	solution = switching_algorithm(batteries, houses)
	batteries = solution[0]
	houses = solution[1]
	
	return [batteries, houses]