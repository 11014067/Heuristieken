# Calculate the cable length and cost of a neighborhood.

import math

def score_function(all_info):
	
	# calculate the cable length for each house and save the sum
	cost_of_neighborhood = 0
	for house in all_info.houses:
		if int(house.battery_no) >= 0:
			h_x = house.x
			h_y = house.y
			b_x = next(battery for battery in all_info.batteries if battery.id == house.battery_no).x
			b_y = next(battery for battery in all_info.batteries if battery.id == house.battery_no).y
			cost_of_neighborhood += abs(b_y - h_y)
			cost_of_neighborhood += abs(b_x - h_x)
		else:
			print("house {} is not connected".format(house.id))
	all_info.cable_length = cost_of_neighborhood
	
	# calculate the price with battery price and save it
	cost_of_neighborhood *= 9
	for battery in all_info.batteries:
		cost_of_neighborhood += int((math.log(battery.voltage, math.e)*649.21) - 3066.2)
	all_info.cost = cost_of_neighborhood
	
	return all_info