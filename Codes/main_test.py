from neighborhood_classes import House, Battery
from sorting_algorithm import sorting_algorithm
from distance_algorithm import distance_algorithm
from download_data import download_data
from plot_grid import plot_grid as plot_grid
from ask_nicely import ask_nicely

ask_nicely()

# choose the neighborhood number
wijk = '2'

# choose the sorting method for batteries and houses (x, y, voltage, random or distance)
battery_sort = 'y'
house_sort = 'distance'

# start the cable length
cable_length = 0

# DOWNLOAD AND ORDER DATA
information = download_data(wijk)
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


