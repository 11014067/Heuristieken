# This function visualises a neighborhood where all the houses are linked to batteries.
# It asks the user what kind of algorithm it wants to use, which neighborhood and how big and how many batteries.

from Classes.neighborhood_classes import Neighborhood_class
from Algorithms.sorting_algorithm import sorting_algorithm
from Algorithms.distance_algorithm import distance_algorithm
from Functions.download_data import download_data
from Functions.plot_grid import plot_grid as plot_grid
from Functions.ask_nicely import ask_nicely
from Functions.score_function import score_function
from Functions.switcher import switching_algorithm
from Functions.free_batteries import free_batteries
from Functions.new_batteries import new_batteries
from Functions.hill_climber import hill_climber
from Information.upper import upper
from Information.lower import lower

#from Test.forlooptest import test_algorithm
import random

def main( a = None):
	# fill all_info with information
	all_info = ask_nicely()
	
	# download and order the data
	all_info = download_data(all_info)
	
	# check if it is solvable
	if (all_info.solveable == False):
		print("This problem is not able to be solved do to to little battery voltage.")
		return 0
		
	# free batteries
	save_free = ""
	if all_info.free == "yes":
		save_free = "Free"
		all_info = free_batteries(all_info)
		all_info = new_batteries(all_info)
		
	# algorithm
	if (all_info.sorting_method == "distance"):
		all_info = distance_algorithm(all_info)
		#information = distance_algorithm(batteries, houses, battery_sort)
	elif (all_info.sorting_method == "sorting"):
		all_info = sorting_algorithm(all_info)
	
	# switch if nessecairy
	all_info = switching_algorithm(all_info)
	
	# score the outcome
	all_info = score_function(all_info)
	
	hill_climber(all_info)
	
	# make a visualisation
	plt = plot_grid(all_info)
	
	# save the visualisation
	plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + "_" + str(len(all_info.batteries)) + save_free + "batteries.png")
	
	# if there is no argument given, show the plot
	if (a == None) :
		plt.show()
		
	return all_info

if __name__ == "__main__":
    main()