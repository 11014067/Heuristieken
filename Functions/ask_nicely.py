# This function asks the user what data and which functions they want to use.

from Classes.neighborhood_classes import Neighborhood_class
from Functions.ask_nicely_short import ask_nicely_short
from Functions.ask_nicely_long import ask_nicely_long

def ask_nicely():

	yes_list = ["y", "yes"]
	no_list = ["n", "no"]
	check = True

	# shortcut option
	print("Do you want to take a shortcut with less options?")
	while check:
		shortcut = input("shortcut: ")
		if shortcut in yes_list:
			all_info = ask_nicely_short()
			check = False
		elif shortcut in no_list:
			all_info = ask_nicely_long()
			check = False
		else:
			print ("Please choose yes or no")
		
	return all_info
	
