# This function is a hillclimber that does the wanted amount of itterations.
# With each itteration it try's to find a better solution by switching two random houses from two of the batteries.
from pathlib import Path
from Functions.switcher import switching_algorithm
from Classes.neighborhood_classes import Neighborhood_class
from Functions.download_data import download_data
from Functions.score_function import score_function
import random
import csv
import datetime

def hill_climber(all_info, repeat):
	info_iterations = []
	info_cable_length = []
	range_loops = all_info.iterations 
	# print("start hill_climber")
	for i in range(range_loops):
		# print("iteration {}".format(i))
		# random selection of two batteries
		select_battery = random.sample(all_info.batteries , 2)
		house_list_battery_0 = select_battery[0].houses_list
		# print(select_battery[0].id)
		# print(select_battery[1].id)
		
		# random selection of a house out of the first sampled battery 
		# [0] behind it to get the first item out of the list (eventhough there is only 1 item, still need to do this)
		select_house = random.sample(house_list_battery_0, 1)[0]
		# print(select_house)
		
		# loop through all houses connected to the second battery
		# for house in select_battery[1].houses_list: 
		for house in select_battery[1].houses_list:
			# Check if current selected house has a voltage bigger + battery.spare_voltage bigger than other selected house and if random selected house + battery.spare_voltage is bigger than the other selected house
			if (select_house.voltage + select_battery[0].spare_voltage) >= house.voltage and (house.voltage + select_battery[1].spare_voltage) >= select_house.voltage:
				# print("first obstacle won")
				# print(select_house.x, select_house.y)
				# print(house.x, house.y)
				# calculate cable length current and option
				cable_length = 0
				current_houses = [select_house, house]
				# print("id selected battery {}".format(select_battery[1].id))
				# print(select_battery[1].x)
				# print(select_battery[1].y)
				# print("id selected battery {}".format(select_battery[0].id))
				# print(select_battery[0].x)
				# print(select_battery[1].y)
				# print(house.x)
				# print(house.y)
				# print(select_house.x)
				# print(select_house.y)
				# print("first selected battery_number {}".format(select_battery[0].id))
				# print(select_house.id)
				# print("second selected battery_number {}".format(select_battery[1].id))
				# print(house.id)
				cable_length_overview = []
				# compare options between selected house in first battery, current house in second battery, selected house to seconde battery, current house to first battery  
				options = [0, 0, 1, 1, 0, 1, 1, 0]
				add = 0

				for j in range(4):
					h_x = current_houses[options[add]].x
					h_y = current_houses[options[add]].y
					b_x = select_battery[options[add + 1]].x
					b_y = select_battery[options[add + 1]].y
					# print(cable_length)
					cable_length += abs(b_y - h_y)
					cable_length += abs(b_x - h_x)
					# print(cable_length)
					cable_length_overview.append(cable_length)
					cable_length = 0
					# print(cable_length)
					cable_length = 0
					# print(cable_length)
					add = add + 2
				# print(cable_length_overview)

				# make current and new sum
				cable_length_current = cable_length_overview[0] + cable_length_overview[1]
				cable_length_future = cable_length_overview[2] + cable_length_overview[3]

				# print("current {}".format(cable_length_current))
				# print("future {}".format(cable_length_future))

				# If that is the case check the cable lenghts of houses to other battery if sum cable length of new situation is shorter than original cable length 
				if cable_length_current > cable_length_future:
					# print("first selected battery_number {}".format(select_battery[0].id))
					# print(select_house.id)
					# print(select_house.battery_no)
					# print("second selected battery_number {}".format(select_battery[1].id))
					# print(house.id)
					# print(house.battery_no)
					# print("second won!!")
					# If that is the case execute the switch of battery
					# change the information in the batteries list
					for battery in all_info.batteries:
						if select_battery[0].id == battery.id:
							battery.spare_voltage += select_house.voltage - house.voltage
							battery.houses_list.remove(select_house)
							battery.houses_list.append(house)
						if select_battery[1].id == battery.id:
							battery.spare_voltage += select_house.voltage - house.voltage
							battery.houses_list.remove(house)
							battery.houses_list.append(select_house)

					# change the information of the changed houses
					temp = select_house.battery_no
					select_house.battery_no = house.battery_no
					house.battery_no = temp
					# print(select_house.battery_no)
					# print(house.battery_no)
					break

					temp = select_house.select_battery[0]
					select_house.select_battery[0] = house.select_battery[1]
					house.select_battery[1] = temp
					# print("switch")
					print("switch")
		
		# save info
		info_iterations.append(i)
		# print(info_iterations)

		info_cable_length.append(score_function(all_info).cable_length)
		# print(info_cable_length)
		# for battery in all_info.batteries:
		# 	print("battery id: {}".format(battery.id))
		# 	for house in battery.houses_list:
		# 		print("house number: {}".format(house.id))

	for house in all_info.houses:
		print("house id: {}".format(house.id))
		print("house is coupled to battery: {}".format(house.battery_no))

	with open(("hillclimber" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + str(len(all_info.batteries)) + str((all_info.iterations)) + str(repeat) +".csv"), "w") as csvfile:
		fieldnames = ["iterations", "cable_length"]
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for j in range(len(info_iterations)):
			writer.writerow({fieldnames[0]: info_iterations[j], fieldnames[1]: info_cable_length[j]})

	return all_info