from neighborhood_classes import House, Battery
from sorting_algorithm import sorting_algorithm
from distance_algorithm import distance_algorithm
from download_data import download_data
from plot_grid import plot_grid as plot_grid
from ask_nicely import ask_nicely

# remember the method to use, return index[1] not in use
method = ask_nicely()

# choose the neighborhood number
wijk = method[0]

# choose the sorting method for batteries and houses (x, y, voltage, random or distance)
battery_sort = method[2]
house_sort = method[3]

# choose the battery size, standaard bij wijk 1 1507, wijk 2 1508.25 en wijk 3 1506.75
battery_size = [1507, 1507, 1507, 1507, 1507]

# start the cable length
cable_length = 0

# DOWNLOAD AND ORDER DATA
information = download_data(wijk, battery_size)
batteries = information[0]
houses = information[1]
	
# ALGORITHM
if (house_sort == "distance"):
	information = distance_algorithm(batteries, houses, battery_sort)
else:
	information = sorting_algorithm(batteries, houses, battery_sort, house_sort)
batteries = information[0]
houses = information[1]

# PLOT
plt = plot_grid(houses, batteries)
plt.savefig("Visual_solutions/fig" + wijk + battery_sort + house_sort + ".png")
plt.show()


