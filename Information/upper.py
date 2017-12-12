import math

def upper(houses, batteries):
	# start with 0 cable pieces
	cable_length = 0
	price = 0
	for house in houses:
		# if placed in the opposide corners of the grid, the length is max 100
		upper_bound = 0
		for battery in batteries:
			# calculate the length of the cable
			temp = abs(house.x - battery.x) + abs(house.y - battery.x)
			# if better, save it
			if temp > upper_bound:
				upper_bound = temp
		# add it for every house
		cable_length += upper_bound
	price = cable_length * 9
	for battery in batteries:
		price += int((math.log(battery.voltage, math.e) * 649.21) - 3066.2)
	
	print("The upper bound is " + str(cable_length) + " pieces of cable for a price of " + str(price))
	
	return [cable_length, price]