#from Test.classes2 import Neighborhood_class
from Test.classes2b import Neighborhood_class
from Classes.neighborhood_classes import House, Battery
from Algorithms.sorting_algorithm import sorting_algorithm
from Algorithms.distance_algorithm import distance_algorithm
from Test.TESTdownload_data import TESTdownload_data as download_data
from Functions.plot_grid import plot_grid as plot_grid
from Functions.score_function import score_function
from Functions.switcher import switching_algorithm
from Test.free_batteries import free_batteries
from Test.new_batteries import new_batteries
from Test.forlooptest import test_algorithm
import random

def TESTmain():
	# remember the method to use
	method = ["1", "s", True, "x", "x"]
	
	Neighborhood_class.House(10, 11, 12, 3)
	print(Neighborhood_class.houses[0].id)
	
	# choose the neighborhood number
	neighborhood = method[0]
	
	# choose the sorting method for batteries and houses (x, y, voltage, random or distance)
	battery_sort = method[2]
	house_sort = method[3]
	
	# choose the battery size, standaard bij wijk 1 1507, wijk 2 1508.25 en wijk 3 1506.75
	battery_size = [1507, 1507, 1507, 1507, 1507]
	
	# DOWNLOAD AND ORDER DATA
	information = download_data(neighborhood, battery_size)
	all_info = information[0]
	
	
	all_info.show_houses()
	
	#if (information[2] == False):
	#	print("This problem is not able to be solved do to to little battery voltage.")
	#	return 0
	#	
    #
	## ALGORITHM
	#if (method[1] == "distance"):
	#	information = test_algorithm(batteries, houses, battery_sort)
	#	#information = distance_algorithm(batteries, houses, battery_sort)
	#elif (method[1] == "sorting"):
	#	information = sorting_algorithm(batteries, houses, battery_sort, house_sort)
	#batteries = information[0]
	#houses = information[1]
	
	## SWITCH (and print cables)
	#solution = switching_algorithm(batteries, houses)
	#batteries = solution[0]
	#houses = solution[1]
	#
	## SCORE
	#scores = score_function(houses, batteries)
	#cable_length = scores[0]
	#cost_of_neighborhood = scores[1]
	#
	## PLOT
	#plt = plot_grid(houses, batteries, cable_length, cost_of_neighborhood)
	#plt.savefig("Visual_solutions/fig_" + method[1] + str(neighborhood) + battery_sort + str(house_sort) + "_" + str(len(batteries)) + "batteries.png")
	#
	#plt.show()
	return 0

if __name__ == "__main__":
    TESTmain()