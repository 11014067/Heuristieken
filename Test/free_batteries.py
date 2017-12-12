# calculate densly packed areas of houses to put batteries.

def free_batteries(houses): 
	
	# maak een lijst met coordinaten
	list_co = []
	coordinates = [0, 5, 10, 15, 20, 25, 30, 35, 40]
	x = 0
	y = 0
	
	# calculate the house density for the coordinates
	breakLoop = False
	while (breakLoop == False):
		houses_amount = 0
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
	
	# sort the list on density
	list_co = sorted(list_co, key=lambda listCo: -listCo[2])

	# get the best coordinates dont put new battery coordinates near that
	for i in range(0, len(all_info.batteries)):
		xCoor = list_co[0][0]
		yCoor = list_co[0][1]
		all_info.battery_coordinates.append([xCoor, yCoor])
		remove_list = []
		
		# if there are more then 9 batteries wanted, lessen the border to always have a solution
		if len(all_info.batteries) > 9:
			border = 1
		else:
			border = 6
		
		# delete other battery coordinates within the list that are to close to the chosen one
		for list_object in list_co:
			if (abs(list_object[0] - xCoor) < border and abs(list_object[1] - yCoor) < border):
				remove_list.append(list_object)
		for list_object in remove_list:
			list_co.remove(list_object)
			
	return battery_coordinates