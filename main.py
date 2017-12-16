# This function visualises a neighborhood where all the houses are linked to batteries.
# It asks the user what kind of algorithm it wants to use, which neighborhood and how big and how many batteries.

from Algorithms.distance_algorithm import distance_algorithm
from Algorithms.free_batteries import free_batteries
from Algorithms.hill_climber import hill_climber
from Algorithms.non_itterative_distance import non_itterative_distance
from Algorithms.sorting_algorithm import sorting_algorithm
from Classes.neighborhood_classes import Neighborhood_class
from Functions.ask_nicely import ask_nicely
from Functions.ask_nicely_long import ask_nicely_long
from Functions.ask_nicely_short import ask_nicely_short
from Functions.bounds import bounds
from Functions.download_data import download_data
from Functions.plot_grid import plot_grid as plot_grid
from Functions.score_function import score_function
from Functions.switcher import switching_algorithm
from Test.replace_batteries import replace
from Test.relocate_battery import relocate
from Test.empty import empty
from Information.upper import upper
from Information.lower import lower
import random

def main( a = None):
	# fill all_info with information
	all_info = ask_nicely()
	
	# download and order the data
	all_info = download_data(all_info)
	
	# check if it is solvable
	if all_info.solveable == False:
		print("This problem is not able to be solved do to to little battery voltage.")
		return 0
		
	# calculate the bounds and free batteries
	save_free = ""
	if all_info.choice == "long":
		if all_info.free == "yes":
			save_free = "Free"
			all_info = free_batteries(all_info)
		all_info = bounds(all_info)
		
	# algorithm
	if (all_info.sorting_method == "distance"):
		all_info = distance_algorithm(all_info)
	elif (all_info.sorting_method == "non-itterative"):
		all_info = non_itterative_distance(all_info)
	elif (all_info.sorting_method == "sorting"):
		all_info = sorting_algorithm(all_info)
	
	# switch if nessecairy
	all_info = switching_algorithm(all_info, 0)
	
	# score the outcome
	all_info = score_function(all_info)
	
	# start hillclimber when wished
	if all_info.choice == "long":
		if all_info.hill_climber == "yes":
			hill_climber(all_info)

	# score the outcome
	all_info = score_function(all_info)
	
	# make a visualisation
	plt = plot_grid(all_info)
	
	# save the visualisation
	plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + "_" + str(len(all_info.batteries)) + save_free + "_" + str((all_info.iterations)) + "batteries.png")
	
	# if there is no argument given, show the plot
	if a == None :
		plt.show()
	
	if all_info.choice == "long":
		if all_info.improve == "yes":
			relocate(all_info)
			
	return all_info

if __name__ == "__main__":
    main()