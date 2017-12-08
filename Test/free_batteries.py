def free_batteries(houses) :
	list_co = []
	
	coordinates = [0, 5, 10, 15, 20, 25, 30, 35, 40]
	x = 0
	y = 0
	breakLoop = False
	while (breakLoop == False):
		houses_amount = 0
		print(houses_amount)
		for house in houses:
			if (((house.x - coordinates[x]) >= 0 and (house.x - coordinates[x]) < 10) and ((house.y - coordinates[y]) >= 0 ) and ((house.y - coordinates[y]) < 10)):
				houses_amount += 1
		list_co.append([coordinates[x], coordinates[y], houses_amount])
		
		x += 1
		# Als x door de coordinaten heen is, zet hem terug naar nul en tel 1 bij y op, als y ook door de coordinaten heen is break
		if (x == len(coordinates)):
			if (y == len(coordinates) - 1):
				breakLoop = True
			else:
				x = 0
				y += 1
	battery_coordinates = []
	list_co = sorted(list_co, key=lambda listCo: -listCo[2])
	print( len(list_co))
	for i in range(0, 6):
		print(list_co)
		print("#################")
		xCoor = list_co[0][0]
		yCoor = list_co[0][1]
		battery_coordinates.append([xCoor, yCoor])
		for list_object in list_co:
			if (abs(list_object[0] - xCoor) < 6 ):
				list_co.remove(list_object)
			elif (abs(list_object[1] - yCoor) < 6):
				list_co.remove(list_object)
	
	print(len(list_co))
	print(battery_coordinates, list_co)
		
		
