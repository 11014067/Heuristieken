from Classes.neighborhood_classes import Neighborhood_class
from Algorithms.sorting_algorithm import sorting_algorithm
from Algorithms.distance_algorithm import distance_algorithm
from Functions.download_data import download_data
from Functions.plot_grid import plot_grid as plot_grid
from Functions.ask_nicely import ask_nicely
from Functions.score_function import score_function
from Functions.switcher import switching_algorithm
#from Test.free_batteries import free_batteries
#from Test.new_batteries import new_batteries
from Test.forlooptest import test_algorithm
import random

def main():
	# remember the method to use
	all_info = ask_nicely()
	
	# DOWNLOAD AND ORDER DATA
	all_info = download_data(all_info)
	
	
	if (all_info.solveable == False):
		print("This problem is not able to be solved do to to little battery voltage.")
		return 0
		
	## TEST 
	#battery_coordinates = free_batteries(all_info)
	#better_batteries = new_batteries(battery_coordinates, all_info)
	#print(battery_coordinates)	
		
	#batteries = better_batteries
		
	# ALGORITHM
	if (all_info.sorting_method == "distance"):
		all_info = test_algorithm(all_info)
		#information = distance_algorithm(batteries, houses, battery_sort)
	elif (all_info.sorting_method == "sorting"):
		all_info = sorting_algorithm(all_info)
	
	# SWITCH (and print cables)
	all_info = switching_algorithm(all_info)
	
	# SCORE
	all_info = score_function(all_info)
	
	# PLOT
	plt = plot_grid(all_info)
	# plt.savefig("Visual_solutions/fig_" + method[1] + str(neighborhood) + battery_sort + str(house_sort) + "_" + str(len(batteries)) + "batteries.png")
	
	plt.show()
	return 0

if __name__ == "__main__":
    main()