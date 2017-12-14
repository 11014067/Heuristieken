# Calculates the bounds of the neighborhood.

def bounds (all_info):
	maximum = 0
	for house in all_info.houses:
		longest_cable = 0
		for battery in all_info.batteries:
			distance = abs(house.x - battery.x) + abs(house.y - battery.y)
			if distance > longest_cable:
				longest_cable = distance
		maximum += longest_cable
	
	all_info.upper_bound = maximum
	print("The maximum is: " + str(maximum))
	
	minimum = 0
	for house in all_info.houses:
		shortest_cable = 0
		for battery in all_info.batteries:
			distance = abs(house.x - battery.x) + abs(house.y - battery.y)
			if distance < shortest_cable:
				shortest_cable = distance
		minimum += longest_cable
	
	all_info.lower_bound = minimum
	print("The minimum is: " + str(minimum))
	return all_info