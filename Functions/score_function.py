import math

def score_function(houses, batteries):
	cost_of_neighborhood = 0
	for house in houses:
		if (int(house.battery_no) >= 0):
			h_x = house.x
			h_y = house.y
			b_x = next(battery for battery in batteries if battery.name == house.battery_no).x
			b_y = next(battery for battery in batteries if battery.name == house.battery_no).y
			cost_of_neighborhood += abs(b_y - h_y)
			cost_of_neighborhood += abs(b_x - h_x)
		else:
			print("house {} is not connected".format(house.id))
		
	cable_length = cost_of_neighborhood
	cost_of_neighborhood *= 9
	
	for battery in batteries:
		cost_of_neighborhood += int((math.log(battery.voltage, math.e)*649.21) - 3066.2)
	
	return [cable_length, cost_of_neighborhood]