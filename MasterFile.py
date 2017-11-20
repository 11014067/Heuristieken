from classesWijk import House, Battery
from SortingAlgorithm import sorting_algorithm
from download_data import download_data
from PlotGrid import PlotGrid as plot_grid

# start the cable length
cable_length = 0

# DOWNLOAD AND ORDER DATA
# choose the neighboohood number
information = download_data('1')
batteries = information[0]
houses = information[1]
	
# ALGORITHM
# choose the sorting method for batteries and houses
information = sorting_algorithm(batteries, houses, 'x', 'x')
batteries = information[0]
houses = information[1]

# PLOT
plot_grid(houses, batteries)

