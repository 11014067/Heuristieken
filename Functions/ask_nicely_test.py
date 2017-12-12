# This function asks the user what data and which functions they want to use.

from Classes.neighborhood_classes import Neighborhood_class

def ask_nicely():

	# create boolians 
	check1 = True
	check2a = True
	check2b = True
	check3 = True
	check4a = True
	check4b = True
	check5a = True
	check5b = True

	# create possible correct answers for the questions
	neighborhood_list = ["1", "2", "3"]
	variable_batteries_list = ["y", "n", "yes", "no"]
	sorting_method_list = ["s", "d", "sorting", "distance"]
	sorting_options = ["x", "y", "voltage", "random", "v", "r"]
	variable_batteries_voltages = []
	hill_climbing = ["y", "n", "yes", "no"]
	
	# create a new neighborhood class
	all_info = Neighborhood_class()
	
	# ask for the neighborhood
	print ("You can pick neighborhood 1, 2 or 3")
	while check1:
		all_info.neighborhood = input("Please enter neighborhood: ")
		if all_info.neighborhood in neighborhood_list:
			print ("You entered", all_info.neighborhood)
			check1 = False
		else:
			print ("Please choose 1, 2 or 3")
	
	# ask for the algorithm
	print ("Do you want to make batteries variable? Yes/no:")
	while check2a:
		variable_batteries = input("")
		if variable_batteries in variable_batteries_list:
			if variable_batteries_list.index(variable_batteries) < 2:
				variable_batteries = variable_batteries_list[variable_batteries_list.index(variable_batteries) + 2]
			print ("You entered", variable_batteries)
			check2a = False
		else:
			print ("Please answer with yes or no:")
			
	if variable_batteries == "yes":
		while check2b:
			print ("How many batteries do you want?")
			number_of_batteries = input("")
			if(int(number_of_batteries) in range(1, 31)):
				check2b = False
		for i in range(0, int(number_of_batteries)):
			new_entry = True
			while new_entry:
				voltage_battery = input("How much voltage has battery " + str(i) + ": ")
				if int(voltage_battery) > 0 and int(voltage_battery) <= 1800:
					variable_batteries_voltages.append(int(voltage_battery))
					new_entry = False
				else:
					print("Please enter a number between 0 and 1800")
		all_info.battery_voltages = variable_batteries_voltages
		print(variable_batteries_voltages)
	else:
		all_info.battery_voltages = [1510, 1510, 1510, 1510, 1510]
		
	# ask for the algorithm
	print ("You can currently use 2 algorithms: sorting or distance")
	while check3:
		all_info.sorting_method = input("Please enter sorting algorithm: ")
		if all_info.sorting_method in sorting_method_list:
			if sorting_method_list.index(all_info.sorting_method) < 2:
				all_info.sorting_method = sorting_method_list[sorting_method_list.index(all_info.sorting_method) + 2]
			print ("You entered", all_info.sorting_method)
			check3 = False
		else:
			print ("Please choose sorting or distance")
	
	# ask for the batteries sorting method
	print ("You can sort the batteries on voltage, x, y or random.")
	while check4a:
		all_info.battery_sort = input("Please enter a sorting method for the batteries: ")
		if all_info.battery_sort in sorting_options:
			if sorting_options.index(all_info.battery_sort) > 3:
				all_info.battery_sort = sorting_options[sorting_options.index(all_info.battery_sort) - 2]
			print ("You entered", all_info.battery_sort)
			check4a = False
		else:
			print ("Please choose x, y, voltage or random")
	
	
	if all_info.sorting_method != "distance":
		# ask for the batteries sorting method
		print ("You can sort the houses on voltage, x, y or random.")
		while check4b:
			all_info.house_sort = input("Please enter a sorting method for the houses: ")
			if all_info.house_sort in sorting_options:
				if sorting_options.index(all_info.house_sort) > 3:
					all_info.house_sort = sorting_options[sorting_options.index(all_info.house_sort) - 2]
				print ("You entered", all_info.house_sort)
				check4b = False
			else:
				print ("Please choose x, y, voltage or random")
	else:
		all_info.house_sort = None


	# ask for hill climbing
	print("Would you like to proceed with a hill climber after connecting all houses? Yes/no")
	while check5a:
			hill_climber = input("")
			if hill_climber in hill_climbing:
				if hill_climbing.index(hill_climber) < 2:
					hill_climber = hill_climbing[hill_climbing.index(hill_climber) + 2] 
				print("You entered", hill_climber)
				check5a = False
			else:
				print("Please answer with yes or no:")

	if hill_climber == "yes":
		while check5b:
			print ("How many iterations do you want?")
			number_of_iterations = input("")
			check5b = False
		all_info.hill_climber = "yes"
		all_info.iterations = int(number_of_iterations)
		print(all_info.iterations)

	else:
		all_info.hill_climber == "no"

		
	return all_info
	
