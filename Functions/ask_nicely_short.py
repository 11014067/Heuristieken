# This function asks the user what data and which functions they want to use.

from Classes.neighborhood_classes import Neighborhood_class

def ask_nicely_short():

	# create possible correct answers for the questions
	neighborhood_list = ["1", "2", "3"]
	sorting_method_list = ["s", "d", "n", "sorting", "distance", "non-itterative"]
	sorting_options_list = ["x", "y", "voltage", "random", "v", "r"]
	
	# create a new neighborhood class
	all_info = Neighborhood_class("short")

	# create boolians 
	check1 = True
	check2 = True
	check3a = True
	check3b = True

	# ask for the neighborhood
	print("You can pick neighborhood 1, 2 or 3")
	while check1:
		all_info.neighborhood = input("Please enter neighborhood: ")
		if all_info.neighborhood in neighborhood_list:
			print("You entered", all_info.neighborhood)
			check1 = False
			if all_info.neighborhood == "1" :
				all_info.battery_voltages = [1507] * 5
			elif all_info.neighborhood == "2" :
				all_info.battery_voltages = [1508.25] * 5
			elif all_info.neighborhood == "3" :
				all_info.battery_voltages = [1506.75] * 5
		else:
			print("Please choose 1, 2 or 3")
			
	# ask for the algorithm
	print("You can currently use 2 algorithms: sorting, distance or non-itterative")
	while check2:
		all_info.sorting_method = input("Please enter sorting algorithm: ")
		if all_info.sorting_method in sorting_method_list:
			if sorting_method_list.index(all_info.sorting_method) < 3:
				all_info.sorting_method = sorting_method_list[sorting_method_list.index(all_info.sorting_method) + 3]
			print("You entered", all_info.sorting_method)
			check2 = False
		else:
			print("Please choose sorting, distance or non-itterative")
	
	if all_info.sorting_method != "non-itterative":
	
		# ask for the batteries sorting method
		print("You can sort the batteries on voltage, x, y or random.")
		while check3a:
			all_info.battery_sort = input("Please enter a sorting method for the batteries: ")
			if all_info.battery_sort in sorting_options_list:
				if sorting_options_list.index(all_info.battery_sort) > 3:
					all_info.battery_sort = sorting_options_list[sorting_options_list.index(all_info.battery_sort) - 2]
				print("You entered", all_info.battery_sort)
				check3a = False
			else:
				print("Please choose x, y, voltage or random:")
	
	
	if all_info.sorting_method == "sorting":
		
		# ask for the houses sorting method
		print("You can sort the houses on voltage, x, y or random.")
		while check3b:
			all_info.house_sort = input("Please enter a sorting method for the houses: ")
			if all_info.house_sort in sorting_options_list:
				if sorting_options_list.index(all_info.house_sort) > 3:
					all_info.house_sort = sorting_options_list[sorting_options_list.index(all_info.house_sort) - 2]
				print("You entered", all_info.house_sort)
				check3b = False
			else:
				print("Please choose x, y, voltage or random:")
	else:
		all_info.house_sort = None
		

	return all_info