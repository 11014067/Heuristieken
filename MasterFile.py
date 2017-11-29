from classesWijk import House, Battery
from SortingAlgorithm import sorting_algorithm
from download_data import download_data
from PlotGrid import PlotGrid as plot_grid
from switcher import switching_algorithm

# start the cable length
cable_length = 0

# choose the neighboohood number
wijk = '1'

# choose the sorting method for batteries and houses
battery_sort = 'voltage'
house_sort = 'voltage'

# DOWNLOAD AND ORDER DATA
information = download_data(wijk)
batteries = information[0]
houses = information[1]
	
# ALGORITHM
information = sorting_algorithm(batteries, houses, battery_sort, house_sort)
batteries = information[0]
houses = information[1]

# SWITCH
if information[2] == False:
	switching_algorithm(batteries, houses)

# PLOT
plt = plot_grid(houses, batteries)
plt.savefig("Visual_solutions/fig" + wijk + battery_sort + house_sort + ".png")
plt.show()