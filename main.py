from neighborhood_classes import House, Battery
from sorting_algorithm import sorting_algorithm
from distance_algorithm import distance_algorithm
from download_data import download_data
from plot_grid import plot_grid as plot_grid
from ask_nicely import ask_nicely
from score_function import score_function

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
	
# ALGORITHM
if (method[1] == "distance"):
	information = distance_algorithm(batteries, houses, battery_sort)
elif (method[1] == "sorting"):
	information = sorting_algorithm(batteries, houses, battery_sort, house_sort)
batteries = information[0]
houses = information[1]

# SCORE
cost_of_neighborhood = score_function(houses, batteries)

# PLOT
plt = plot_grid(houses, batteries, cost_of_neighborhood)
plt.savefig("Visual_solutions/fig" + neighborhood + battery_sort + house_sort + ".png")
plt.show()


