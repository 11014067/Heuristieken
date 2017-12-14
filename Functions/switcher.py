# This function switches houses if the neighborhood was not solved.

def switching_algorithm(all_info, n):

	if n > 40:
		all_info.cable_length = 9999999
		return all_info
	
	# check if there is a solution already
	if all_info.solution == True:
		return all_info
	
	# sort the houses on id
	all_info.houses = sorted(all_info.houses, key=lambda house: house.id)
	
	# switch two houses to make more room in the biggest spare voltage
	makeroom = sorted(all_info.batteries, key=lambda battery: -battery.spare_voltage)[0]
	fill = sorted(all_info.batteries, key=lambda battery: -battery.spare_voltage)[1]
	picked_houses = pick_a_house(all_info, makeroom, fill, 99999999)
	small_house = picked_houses[0]
	big_house = picked_houses[1]

	# change the information in the batteries list
	for battery in all_info.batteries:
		if battery.id == big_house.battery_no:
			battery.spare_voltage += big_house.voltage - small_house.voltage
		
		if battery.id == small_house.battery_no:
			battery.spare_voltage -= big_house.voltage - small_house.voltage
	
	# change the information of the changed houses
	temp = small_house.battery_no
	small_house.battery_no = big_house.battery_no
	big_house.battery_no = temp
	
	# go through the switcher again if necessery 
	for house in all_info.houses:
		if house.placed == False:
			if makeroom.add_house(house):
				print ("HOORAY!")
			else:
				print ("Stop me if I go crazy!")
				switching_algorithm(all_info, n + 1)
				
	return all_info
	
# pick houses to switch	
	
def pick_a_house(all_info, makeroom, fill, last_try):
	
	# get a big house
	big_house = 0
	for house in all_info.houses:
		if house.battery_no == makeroom.id:
			if big_house == 0 and house.voltage < last_try:
				big_house = house
			elif big_house.voltage < house.voltage and house.voltage < last_try:
				big_house = house
	print("Big huis {} batterij {} voltage {} xy {}, {}".format(big_house.id, big_house.battery_no, big_house.voltage, big_house.x, big_house.y))
	
	# get a small house
	small_house = 999999
	for house in all_info.houses:
		if house.battery_no == fill.id and house.voltage > big_house.voltage - fill.spare_voltage:
			if small_house == 999999:
				small_house = house
			elif small_house.voltage > house.voltage:
				small_house = house
	
	# if failed, try again
	if small_house == 999999:
		print ("Let's do this again!")
		picked_houses = pick_a_house(all_info, makeroom, fill, big_house.voltage)
		small_house = picked_houses[0]
		big_house = picked_houses[1]
	print("Small huis {} batterij {} voltage {} xy {}, {} ".format(small_house.id, small_house.battery_no, small_house.voltage, small_house.x, small_house.y))
	
	return [small_house, big_house]