from classesWijk import House, Battery
from sorting_algorithm import sorting_algorithm
from distance_algorithm import distance_algorithm
from download_data import download_data
from plot_grid import plot_grid as plot_grid

# start the cable length
cable_length = 0

# choose the neighboohood number
wijk = '1'

# choose the sorting method for batteries and houses (x, y, voltage, random or distance)
battery_sort = 'x'
house_sort = 'x'

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


