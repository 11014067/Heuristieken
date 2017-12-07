import random

def sorting_algorithm(batteries, houses, sort_battery, sort_house):
	
	#Algorithm
	print ("Sorting...")
	if (sort_battery == "random"):
		batteries = random.sample(batteries, len(batteries))
	elif (sort_battery != "voltage"):
		batteries = sorted(batteries, key=lambda battery: getattr(battery, sort_battery))
	else:
		batteries = sorted(batteries, key=lambda battery: -battery.voltage)
	
	if (sort_house == "random"):
		houses = random.sample(houses, len(houses))
	elif (sort_house != "voltage"):
		houses = sorted(houses, key=lambda house: getattr(house, sort_house))
	else:
		houses = sorted(houses, key=lambda house: -house.voltage)
	
	# link houses and batteries
	solution = True
	for house in houses:
		house_placed = False
		i = 0
		while (house_placed == False):
			if (batteries[i].add_house(house)):
				house_placed = True
			i+=1
			if (i > len(batteries) - 1 and house_placed == False):
				solution = False
				break
	
	for i in range(0, len(batteries) - 1):
		print (batteries[i].spare_voltage)

	return [batteries, houses, solution]