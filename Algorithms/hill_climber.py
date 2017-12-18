# This function is a hillclimber that does the wanted amount of itterations.
# With each itteration it try's to find a better solution by switching two random houses from two of the batteries.

from Functions.switcher import switching_algorithm
from Classes.neighborhood_classes import Neighborhood_class
from Functions.download_data import download_data
from Functions.score_function import score_function
import random
import csv
import datetime

def hill_climber(all_info):

	print("Before hillclimber cable_length is: {}".format(all_info.cable_length))

	info_iterations = []
	info_cable_length = []
	range_loops = all_info.iterations 
	
	# go through the hillclimber as many times as wanted
	for i in range(range_loops):
		
		# randomly select two batteries and a house who is linked to the first battery
		select_battery = random.sample(all_info.batteries , 2)
		house_list_battery_0 = select_battery[0].houses_list
		select_house = random.sample(house_list_battery_0, 1)[0]
		
		# loop through all houses connected to the second battery
		for house in select_battery[1].houses_list:
		
			# check if the current houses could be switched
			if (select_house.voltage + select_battery[0].spare_voltage) >= house.voltage and (house.voltage + select_battery[1].spare_voltage) >= select_house.voltage:
				
				# calculate cable length current and option
				cable_length = 0
				current_houses = [select_house, house]
				cable_length_overview = []
				options = [0, 0, 1, 1, 0, 1, 1, 0]
				add = 0
				
				# calculate the options
				for j in range(4):
					h_x = current_houses[options[add]].x
					h_y = current_houses[options[add]].y
					b_x = select_battery[options[add + 1]].x
					b_y = select_battery[options[add + 1]].y
					cable_length += abs(b_y - h_y)
					cable_length += abs(b_x - h_x)
					cable_length_overview.append(cable_length)
					cable_length = 0
					add = add + 2
					
				# calculate current and new sum
				cable_length_current = cable_length_overview[0] + cable_length_overview[1]
				cable_length_future = cable_length_overview[2] + cable_length_overview[3]

				# check if it is cheaper to switch
				if cable_length_current > cable_length_future:
					
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
					break

					temp = select_house.select_battery[0]
					select_house.select_battery[0] = house.select_battery[1]
					house.select_battery[1] = temp
					print("switch")
		
		# save info
		info_iterations.append(i)
		info_cable_length.append(score_function(all_info).cable_length)

	# print the houses and which battery they are linked to
	for house in all_info.houses:
		print("house id: {}".format(house.id))
		print("house is coupled to battery: {}".format(house.battery_no))

	# save the hillclimber information in a csv
	with open(("hillclimber" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + str(len(all_info.batteries)) + str((all_info.iterations)) + ".csv"), "w") as csvfile:
		fieldnames = ["iterations", "cable_length"]
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		for j in range(len(info_iterations)):
			writer.writerow({fieldnames[0]: info_iterations[j], fieldnames[1]: info_cable_length[j]})

	print("After hillclimber cable_length is: {}".format(all_info.cable_length))
	return all_info