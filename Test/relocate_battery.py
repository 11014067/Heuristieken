# This function relocates batteries and saves the best result from 20 relocations.

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
from Test.empty import empty
from Information.upper import upper
from Information.lower import lower
import matplotlib.pyplot as plt

import time

def relocate(all_info):
	
	# store the solution
	old_all_info = Neighborhood_class("short")
	old_all_info.houses = all_info.houses
	old_all_info.cable_length = all_info.cable_length
	old_all_info.cost = all_info.cost
	old_all_info.batteries = all_info.batteries
	
	# put the batteries in their new location
	all_info = replace(all_info)
		
	# score the outcome
	all_info = score_function(all_info)
		
	# check whether the new solution is better
	print("!!!!", all_info.cable_length, old_all_info.cable_length)
	if all_info.cable_length < old_all_info.cable_length:
		print("HIER!")
		old_all_info.houses = all_info.houses
		old_all_info.cable_length = all_info.cable_length
		old_all_info.cost = all_info.cost
		
	# version to stop when new one is worse then old one
	#
	#elif all_info.cable_length > old_all_info.cable_length:
	#	print("Dit is mijn uitspraak en daar zal u het mee moeten doen.")
	#	return old_all_info
	
	# make the visualisation
	plt = plot_grid(all_info)
	plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + "_" + str(len(all_info.batteries)) + "replacebatteriesandreplace.png")
	plt.ion();
	plt.pause(0.5)
	plt.close();
	
	# now repeat the following steps
	for i in range(0, 20):
		
		#disconnect the houses
		all_info = empty(all_info)
	
		# reconnect the batteries
		all_info.battery_sort = "random"
		all_info = distance_algorithm(all_info)
		
		# switch if nessecairy
		all_info = switching_algorithm(all_info, 0)
		
		# score the outcome
		all_info = score_function(all_info)			
		
		# make a visualisation
		plt = plot_grid(all_info)
		plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + "_" + str(len(all_info.batteries)) + "replacebatteriesandreplace.png")
		plt.pause(1)
		plt.gcf().clear()
		
		# replace the batteries to the middle	
		all_info = replace(all_info)
		
		# score the outcome
		all_info = score_function(all_info)	
		
		# check op verbeteringen
		print("!!!!" + str(all_info.cable_length) + ",  " + str(old_all_info.cable_length) + " itteration: " + str(i))
		if all_info.cable_length < old_all_info.cable_length:
			old_all_info.houses = all_info.houses
			old_all_info.cable_length = all_info.cable_length
			old_all_info.cost = all_info.cost
			old_all_info.batteries = all_info.batteries
			print("Hier!")
		
		# version to stop when new one is worse then old one
		#
		#elif all_info.cable_length > old_all_info.cable_length:
		#	print("Dit is mijn uitspraak en daar zal u het mee moeten doen.")
		#	return old_all_info
		
		# make a visualisation
		plt = plot_grid(all_info)
		plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + "_" + str(len(all_info.batteries)) + "replacebatteriesandreplace.png")
		plt.pause(1)
		plt.gcf().clear()
	
	# print the best version
	print("This is the best version found!")
	plt = plot_grid(old_all_info)
	plt.pause(10)
	plt.savefig("Visual_solutions/fig_" + str(all_info.sorting_method) + str(all_info.neighborhood) + str(all_info.battery_sort) + str(all_info.house_sort) + "_" + str(len(all_info.batteries)) + "replacebatteriesandreplace.png")
		
	return old_all_info