# calculate densly packed areas of houses to put batteries.

import random

def free_batteries(all_info): 

	# maak een lijst met coordinaten
	list_co = []
	coordinates = [0, 5, 10, 15, 20, 25, 30, 35, 40]
	x = 0
	y = 0
	
	# calculate the house density for the coordinates
	breakLoop = False
	while (breakLoop == False):
		houses_amount = 0
		for house in all_info.houses:
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
		x_coor = list_co[0][0]
		y_coor = list_co[0][1]
		fix_coor = False
		while (fix_coor == False):
			fix_coor2 = False
			while (fix_coor2 == False):
				for house in all_info.houses :
					if (house.x == x_coor) and (house.y == y_coor):
						a = random.sample([1, 2], 1)[0]
						if (a == 1):
							if x_coor == 50 :
								x_coor = 49
							elif x_coor == 0 :
								x_coor = 1
							else :
								x = random.sample([-1, 1], 1)[0]
								x_coor += x
						else :
							if y_coor == 50 :
								y_coor = 49
							elif y_coor == 0 :
								y_coor = 1
							else :
								x = random.sample([-1, 1], 1)[0]
								y_coor += x
						fix_coor2 = True
				fix_coor = True
				fix_coor2 = True
		
		all_info.battery_coordinates.append([x_coor, y_coor])
		remove_list = []
		
		# if there are more then 9 batteries wanted, lessen the border to always have a solution
		if len(all_info.batteries) > 9:
			border = 1
		else:
			border = 6
		
		# delete other battery coordinates within the list that are to close to the chosen one
		for list_object in list_co:
			if (abs(list_object[0] - x_coor) < border and abs(list_object[1] - y_coor) < border):
				remove_list.append(list_object)
		for list_object in remove_list:
			list_co.remove(list_object)
	
	return all_info