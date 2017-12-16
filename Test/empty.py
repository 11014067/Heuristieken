def empty(all_info):
	for battery in all_info.batteries:
		battery.spare_voltage = battery.voltage
		battery.houses_list = []
	for house in all_info.houses:
		house.battery_no = -1
		house.placed = False
	return all_info