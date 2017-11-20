def sorting_algorithm(batteries, houses, sort_battery, sort_house):
	
	#Algorithm
	print "Sorting..."
	batteries = sorted(batteries, key=lambda battery: getattr(battery, sort_battery))
	houses = sorted(houses, key=lambda house: getattr(house, sort_house))
	
	# link houses and batteries
	housenumber = 0
	for house in houses:
		unplaced = True
		i = 0
		while unplaced:
			if batteries[i].add_house(house):
				unplaced = False
				print "House {} is connected to battery {} voltage {}".format(housenumber, house.battery_no, house.voltage)
			i+=1
			if i > 4:
				break
		housenumber+=1
		
	for i in range(0,5):
		print batteries[i].spare_voltage
	print houses[149].voltage
	return [batteries, houses]