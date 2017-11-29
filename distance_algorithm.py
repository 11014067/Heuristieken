from switcher import switching_algorithm

def distance_algorithm(batteries, houses, sort_battery):
	# Sort the batteries
	print "Sorting..."
	if (sort_battery != "voltage"):
		batteries = sorted(batteries, key=lambda battery: getattr(battery, sort_battery))
	elif (sort_battery == "random"):
		batteries = random.shuffle(batteries)
	else:
		batteries = sorted(batteries, key=lambda battery: -battery.voltage)
	
	# Sort the houses on id
	houses = sorted(houses, key=lambda house: house.id)
	
	# Make a list for each battery
	distance0list = []
	distance1list = []
	distance2list = []
	distance3list = []
	distance4list = []
	
	# Put the distance from each house to each battery in the list as [distance, house id]
	for house in houses:
		distance0 = abs(house.x - batteries[0].x) + abs(house.y - batteries[0].y)
		distance1 = abs(house.x - batteries[1].x) + abs(house.y - batteries[1].y)
		distance2 = abs(house.x - batteries[2].x) + abs(house.y - batteries[2].y)
		distance3 = abs(house.x - batteries[3].x) + abs(house.y - batteries[3].y)
		distance4 = abs(house.x - batteries[4].x) + abs(house.y - batteries[4].y)
		distance0list.append([distance0, house.id])
		distance1list.append([distance1, house.id])
		distance2list.append([distance2, house.id])
		distance3list.append([distance3, house.id])
		distance4list.append([distance4, house.id])
	
	# Sort the list on distance	
	distance0list = sorted(distance0list, key=lambda x: x[0])
	distance1list = sorted(distance1list, key=lambda x: x[0])
	distance2list = sorted(distance2list, key=lambda x: x[0])
	distance3list = sorted(distance3list, key=lambda x: x[0])
	distance4list = sorted(distance4list, key=lambda x: x[0])
	
	# Put all the lists together for easy access
	distanceslists = [distance0list, distance1list, distance2list, distance3list, distance4list]
	
	# Save the indexes and how many houses are placed
	index_list = [0,0,0,0,0]
	houses_to_place = houses.length
	
	# place all the houses
	while houses_to_place > 0:
		for j in range(0, batteries.length - 1):
			# only try to add if it has spare voltage
			if batteries[j].spare_voltage > 0:
				# place the first posible house
				placeHouse = False
				while placeHouse == False:
					if index_list[j] == 150:
						index_list[j] = 149
						# if there are no houses left to place, go to the next battery
						placeHouse = True
					elif houses[distanceslists[j][index_list[j]][1]].placed == False:
						if batteries[j].add_house(houses[distanceslists[j][index_list[j]][1]]):
							# house placed op true
							houses_to_place -= 1
							# go to the next battery
							placeHouse = True
					index_list[j] += 1
		if index_list[0] == 150 and index_list[1] == 150 and index_list[2] == 150 and index_list[3] == 150 and index_list[4] == 150:
			print(" UNSUCCESFULL ")
			break
			
	for house in houses:
		if house.battery_no:
			print("huis {} batterij {} voltage {}".format(house.id, house.battery_no, house.voltage))
		else:
			print house.voltage
	for battery in batteries:
		print("batterij over {}".format(battery.spare_voltage))
		
	solution = switching_algorithm(batteries, houses)
	batteries = solution[0]
	houses = solution[1]
	return [batteries, houses, solution]