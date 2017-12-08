from Classes.neighborhood_classes import House, Battery
from Algorithms.sorting_algorithm import sorting_algorithm
from Algorithms.distance_algorithm import distance_algorithm
from Functions.download_data import download_data
from Functions.plot_grid import plot_grid as plot_grid
from Functions.ask_nicely import ask_nicely
from Functions.score_function import score_function
from Functions.switcher import switching_algorithm
from Test.free_batteries import free_batteries
import random

# remember the method to use
method = ask_nicely()

# choose the neighborhood number
neighborhood = method[0]

# choose the sorting method for batteries and houses (x, y, voltage, random or distance)
battery_sort = method[2]
house_sort = method[3]

# choose the battery size, standaard bij wijk 1 1507, wijk 2 1508.25 en wijk 3 1506.75
battery_size = [1507, 1507, 1507, 1507, 1507]

# DOWNLOAD AND ORDER DATA
information = download_data(neighborhood, battery_size)
batteries = information[0]
houses = information[1]
	
# TEST
free_batteries(houses)	
	
# ALGORITHM
if (method[1] == "distance"):
	information = distance_algorithm(batteries, houses, battery_sort)
elif (method[1] == "sorting"):
	information = sorting_algorithm(batteries, houses, battery_sort, house_sort)
batteries = information[0]
houses = information[1]

# SWITCH (and print cables)
solution = switching_algorithm(batteries, houses)
batteries = solution[0]
houses = solution[1]

# SCORE
scores = score_function(houses, batteries)
cable_length = scores[0]
cost_of_neighborhood = scores[1]

# PLOT
plt = plot_grid(houses, batteries, cable_length, cost_of_neighborhood)
if (method[1] == "distance"):
	plt.savefig("Visual_solutions/fig" + neighborhood + battery_sort + ".png")
else:
	plt.savefig("Visual_solutions/fig" + neighborhood + battery_sort + house_sort + ".png")
plt.show()


