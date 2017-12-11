#from Test.classes2 import Neighborhood_class
from Test.classes2b import Neighborhood_class
from Test.TESTsorting_algorithm import TESTsorting_algorithm as sorting_algorithm
from Test.TESTdownload_dataSanne import TESTdownload_data as download_data
from Test.TESTplot_grid import TESTplot_grid as plot_grid
from Test.TESTscore_function import TESTscore_function as score_function
import random

def TESTmain():


	A = Neighborhood_class
	
	# remember the method to use
	method = ["1", "s", "x", "x"]
	
	# choose the neighborhood number
	A.add_neighborhood(method[0])
	
	# choose the sorting method for batteries and houses (x, y, voltage, random or distance)
	A.add_battery_sort(method[2])
	A.add_house_sort(method[3])
	
	# choose the battery size, standaard bij wijk 1 1507, wijk 2 1508.25 en wijk 3 1506.75
	battery_size = [1507, 1507, 1507, 1507, 1507]
	
	# DOWNLOAD AND ORDER DATA
	information = download_data(battery_size, A)
	all_info = information[0]
	
    #Algorithm
	information = sorting_algorithm(all_info)
	all_info = information[0]

	# SCORE
	scores = score_function(all_info)
	cable_length = scores[0]
	cost_of_neighborhood = scores[1]

	# PLOT
	plt = plot_grid(all_info, cable_length, cost_of_neighborhood)
	
	plt.show()
	return 0

if __name__ == "__main__":
    TESTmain()