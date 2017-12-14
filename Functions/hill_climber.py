# This function is a hillclimber that does the wanted amount of itterations.
# With each itteration it try's to find a better solution by switching two random houses from two of the batteries.

from Functions.switcher import switching_algorithm
from Classes.neighborhood_classes import Neighborhood_class
from Functions.download_data import download_data
from Functions.score_function import score_function
import random

def hill_climber(all_info):
	range_loops = all_info.iterations 
	# print("start hill_climber")
	for i in range(range_loops):
		print(i)
		# random selection of two batteries
		select_battery = random.sample(all_info.batteries , 2)
		house_list_battery_0 = select_battery[0].houses_list
		# print(select_battery)
		
		# random selection of a house out of the first sampled battery 
		# [0] behind it to get the first item out of the list (eventhough there is only 1 item, still need to do this)
		select_house = random.sample(house_list_battery_0, 1)[0]
		# print(select_house)
		
		# loop through all houses connected to the second battery 
		for house in select_battery[1].houses_list:
			# Check if current selected house has a voltage bigger + battery.spare_voltage bigger than other selected house and if random selected house + battery.spare_voltage is bigger than the other selected house
			if (select_house.voltage + select_battery[0].spare_voltage) >= house.voltage and (house.voltage + select_battery[1].spare_voltage) >= select_house.voltage:
				# print("first obstacle won")
				# print(select_house.x, select_house.y)
				# print(house.x, house.y)
				# calculate cable length current and option
				cable_length = 0
				current_houses = [select_house, house]
				cable_length_overview = []
				# compare options between selected house in first battery, current house in second battery, selected house to seconde battery, current house to first battery  
				options = [0, 0, 1, 1, 0, 1, 1, 0]
				add = 0

				for j in range(4):
					h_x = current_houses[options[add]].x
					h_y = current_houses[options[add]].y
					b_x = select_battery[options[add + 1]].x
					b_y = select_battery[options[add + 1]].y
					cable_length += abs(b_y - h_y)
					cable_length += abs(b_x - h_x)
					cable_length_overview.append(cable_length)
					add = add + 2
				# print(cable_length_overview)

				# make current and new sum
				cable_length_current = cable_length_overview[0] + cable_length_overview[1]
				cable_length_future = cable_length_overview[2] + cable_length_overview[3]

				# print(cable_length_current)
				# print(cable_length_future)

				# If that is the case check the cable lenghts of houses to other battery if sum cable length of new situation is shorter than original cable length 
				if cable_length_current > cable_length_future:
					print("second won!!")
					# If that is the case execute the switch of battery
					# change the information in the batteries list
					select_battery[0].spare_voltage += select_house - house
					select_battery[1] += select_house - house

					# change the information of the changed houses
					temp = select_house.select_battery[0]
					select_house.select_battery[0] = house.select_battery[1]
					house.select_battery[1] = temp
					
					print("switch")
	return all_info