def ask_nicely():

	# create boolians 
	check1 = True
	check1b = True
	check1c = True
	check1d = True
	check2 = True
	check3 = True
	check4 = True

	# create possible correct answers for the questions
	neighborhood_list = ["1", "2", "3"]
	variable_batteries_list = ["y", "n", "yes", "no"]
	sorting_method_list = ["s", "d", "sorting", "distance"]
	sorting_options = ["x", "y", "voltage", "random", "v", "r"]
	
	variable_batteries_voltages = []
	variable_batteries_bool = False
	
	
	# ask for the neighborhood
	print ("You can pick neighborhood 1, 2 or 3")
	while check1:
		neighborhood = input("Please enter neighborhood: ")
		if neighborhood in neighborhood_list:
			print ("You entered", neighborhood)
			check1 = False
		else:
			print ("Please choose 1, 2 or 3")
	
	# ask for the algorithm
	print ("Do you want to make batteries variable? Yes/no:")
	while check1b:
		variable_batteries = input("")
		if variable_batteries in variable_batteries_list:
			if variable_batteries.index(variable_batteries) < 2:
				variable_batteries = variable_batteries_list[variable_batteries_list.index(variable_batteries) + 2]
			print ("You entered", variable_batteries)
			check1b = False
		else:
			print ("Please answer with yes or no:")
			
	if variable_batteries == "yes":
		variable_batteries_bool = True
		while check1c:
			print ("How many batteries do you want?")
			number_of_batteries = input("")
			if(int(number_of_batteries) in range(1, 31)):
				check1c = False
		for i in range(0, int(number_of_batteries)):
			new_entry = True
			while new_entry:
				voltage_battery = input("How much voltage has battery " + str(i) + ": ")
				if int(voltage_battery) > 0 and int(voltage_battery) <= 1800:
					variable_batteries_voltages.append(int(voltage_battery))
					new_entry = False
				else:
					print("Please enter a number between 0 and 1800")
		print(variable_batteries_voltages)
		
	# ask for the algorithm
	print ("You can currently use 2 algorithms: sorting or distance")
	while check2:
		sorting_method = input("Please enter sorting algorithm: ")
		if sorting_method in sorting_method_list:
			if sorting_method_list.index(sorting_method) < 2:
				sorting_method = sorting_method_list[sorting_method_list.index(sorting_method) + 2]
			print ("You entered", sorting_method)
			check2 = False
		else:
			print ("Please choose sorting or distance")
	
	# ask for the batteries sorting method
	print ("You can sort the batteries on voltage, x, y or random.")
	while check3:
		sorting_batteries = input("Please enter a sorting method for the batteries: ")
		if sorting_batteries in sorting_options:
			if sorting_options.index(sorting_batteries) > 3:
				sorting_batteries = sorting_options[sorting_options.index(sorting_batteries) - 2]
			print ("You entered", sorting_batteries)
			check3 = False
		else:
			print ("Please choose x, y, voltage or random")
	
	
	if sorting_method != "distance":
		# ask for the batteries sorting method
		print ("You can sort the houses on voltage, x, y or random.")
		while check4:
			sorting_houses = input("Please enter a sorting method for the houses: ")
			if sorting_houses in sorting_options:
				if sorting_options.index(sorting_houses) > 3:
					sorting_houses = sorting_options[sorting_options.index(sorting_houses) - 2]
				print ("You entered", sorting_houses)
				check4 = False
			else:
				print ("Please choose x, y, voltage or random")
	else:
		sorting_houses = None
		
	
	return [neighborhood, sorting_method, sorting_batteries, sorting_houses, variable_batteries_bool, variable_batteries_voltages]
	
