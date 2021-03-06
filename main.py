# This function visualises a neighborhood where all the houses are linked to batteries.
# It asks the user what kind of algorithm it wants to use, which neighborhood and how big and how many batteries.

from Algorithms.distance_algorithm import distance_algorithm
from Algorithms.free_batteries import free_batteries
from Algorithms.hill_climber import hill_climber
from Algorithms.non_iterative import non_iterative
from Algorithms.sorting_algorithm import sorting_algorithm
from Classes.neighborhood_classes import Neighborhood_class
from Functions.ask_nicely import ask_nicely
from Functions.ask_nicely_long import ask_nicely_long
from Functions.ask_nicely_short import ask_nicely_short
from Functions.bounds import bounds
from Functions.download_data import download_data
from Functions.plot_grid import plot_grid
from Functions.score_function import score_function
from Functions.switcher import switching_algorithm
from Test.replace_batteries import replace
from Test.relocate_battery import relocate
from Test.empty import empty
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
	elif (all_info.sorting_method == "non-iterative"):
		all_info = non_iterative(all_info)
	elif (all_info.sorting_method == "sorting"):
		all_info = sorting_algorithm(all_info)
	
	# switch if nessecairy
	all_info = switching_algorithm(all_info, 0)
	
	# score the outcome
	all_info = score_function(all_info)
	
	# starting trying to get improvements if wanted
	if all_info.choice == "long":
		if all_info.improve == "yes":
			all_info = relocate(all_info)
		
		# start hillclimber when wished
		if all_info.hill_climber == "yes":
			all_info = hill_climber(all_info)
			
	# make and save a visualisation
	if a == None :
		plt = plot_grid(all_info)
		if all_info.choice == "short":
			plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + ".png")
		else:
			plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + "_" + str(len(all_info.batteries)) + save_free + "_" + str((all_info.iterations)) + "batteries.png")
		plt.pause(10)
		
	return all_info

if __name__ == "__main__":
    main()