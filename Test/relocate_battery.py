# This function relocates batteries and saves the best result from 20 relocations.

from Algorithms.distance_algorithm import distance_algorithm
from Classes.neighborhood_classes import Neighborhood_class
from Functions.plot_grid import plot_grid
from Functions.score_function import score_function
from Functions.switcher import switching_algorithm
from Test.replace_batteries import replace
from Test.empty import empty
import time

def relocate(all_info):
	
	# store the current solution
	old_all_info = Neighborhood_class("long")
	old_all_info.iterations = all_info.iterations
	old_all_info.choice = all_info.choice
	old_all_info.hill_climber = all_info.hill_climber
	old_all_info.houses = all_info.houses
	old_all_info.cable_length = all_info.cable_length
	old_all_info.cost = all_info.cost
	old_all_info.batteries = all_info.batteries
	
	# put the batteries in their new location
	all_info = replace(all_info)
		
	# score the outcome
	all_info = score_function(all_info)
		
	# check whether the new solution is better
	if all_info.cable_length < old_all_info.cable_length:
		old_all_info.houses = all_info.houses
		old_all_info.batteries = all_info.batteries
		old_all_info.cable_length = all_info.cable_length
		old_all_info.cost = all_info.cost

	# make the visualisation
	plt = plot_grid(all_info)
	plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + "_" + str(len(all_info.batteries)) + "replacebatteriesandreplace.png")
	plt.ion()
	plt.pause(0.5)
	plt.close()
	
	# now repeat the following steps
	for i in range(10):
		if i % 2 == 0:
		
			# disconnect the houses
			all_info = empty(all_info)
		
			# reconnect the batteries
			all_info.battery_sort = "random"
			all_info = distance_algorithm(all_info)
			
			# switch if necessary
			all_info = switching_algorithm(all_info, 0)
		else:
		
			# replace the batteries to the middle	
			all_info = replace(all_info)
		
		# score the outcome
		all_info = score_function(all_info)	
		
		# check if there are improvements
		if all_info.cable_length < old_all_info.cable_length:
			old_all_info.houses = all_info.houses
			old_all_info.cable_length = all_info.cable_length
			old_all_info.cost = all_info.cost
			old_all_info.batteries = all_info.batteries
		
		# make a visualization
		plt = plot_grid(all_info)
		plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + "_" + str(len(all_info.batteries)) + "replacebatteriesandreplace.png")
		plt.pause(0.5)
		plt.gcf().clear()
	
	# print the best version
	print("This is the best version found!", old_all_info.cable_length)
	plt = plot_grid(old_all_info)
	plt.pause(4)
	plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + "_" + str(len(all_info.batteries)) + "replacebatteriesandreplace.png")
	plt.gcf().clear()
	
	return old_all_info