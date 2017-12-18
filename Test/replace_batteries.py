# This function replaces a battery to the middle of its houses.

def replace(all_info):

	# remember its position and calculate a new one
	old_positions = []
	better_positions = []
	for battery in all_info.batteries:
		old_positions.append([battery.x, battery.y])
		new_point = [0, 0]
		
		# calculate the mean x and y coordinate
		for house in battery.houses_list:
			new_point[0] += house.x
			new_point[1] += house.y
		new_point[0] /= len(battery.houses_list)
		new_point[1] /= len(battery.houses_list)
		better_positions.append(new_point)
		battery.x = round(new_point[0])
		battery.y = round(new_point[1])
	
	return all_info	
	
	
