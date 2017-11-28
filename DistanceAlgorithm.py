def distanceAlgorithm(batteries, houses, sort_battery):
	print "Sorting..."
	if (sort_battery != "voltage"):
		batteries = sorted(batteries, key=lambda battery: getattr(battery, sort_battery))
	else:
		batteries = sorted(batteries, key=lambda battery: -battery.voltage)
	houses = sorted(houses, key=lambda house: house.id)
	
	distance0list = []
	distance1list = []
	distance2list = []
	distance3list = []
	distance4list = []
	
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
	
	def numeric_compare(x, y):
		return x - y
		
	distance0list = sorted(distance0list, key=lambda x: x[0])
	distance1list = sorted(distance1list, key=lambda x: x[0])
	distance2list = sorted(distance2list, key=lambda x: x[0])
	distance3list = sorted(distance3list, key=lambda x: x[0])
	distance4list = sorted(distance4list, key=lambda x: x[0])
	
	distanceslists = [distance0list, distance1list, distance2list, distance3list, distance4list]
	
	b = [0,0,0,0,0]
	placednum = 0
	
	# place all the houses
	while placednum < 150:
		# pass the batteries
		j = 0
		for battery in batteries:
			# only try to add if it has spare voltage
			if battery.spare_voltage > 0:
				# place the first posible house
				placeHouse = False
				while placeHouse == False:
					if b[j] == 150:
						b[j] = 149
						placeHouse = True
					elif houses[distanceslists[j][b[j]][1]].placed == False:
						if battery.add_house(houses[distanceslists[j][b[j]][1]]):
							#house placed op true
							placednum += 1
							placeHouse = True
					b[j] += 1
			j += 1
		if b[0] == 150 and b[1] == 150 and b[2] == 150 and b[3] == 150 and b[4] == 150:
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