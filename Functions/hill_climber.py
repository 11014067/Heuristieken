from switcher import switching_algorithm
from Classes.neighborhood_classes import House, Battery
from Functions.download_data import download_data
from Functions.score_function import score_function
import random

# get info from previous solution
if (all_info.sorting_method == "distance"):
	input_values = distance_algorithm(all_info)
elif (all_info.sorting_method == "sorting"):
		input_values = sorting_algorithm(all_info)

# range_loops =  
# for i in range(get range_loops from ask_nicely)

# random selection of two batteries
select_battery = random.sample(Neighborhood_class.batteries, 2)
print(select_battery)

# random selection of a house out of the first sampled battery
select_house = random.sample(select_battery.houses_list, 1)
print(select_house)

# Loop through all houses connected to the second battery (for house in battery)
# Check if current selected house has a voltage bigger + battery.spare_voltage bigger than other selected house and if random selected house + battery.spare_voltage is bigger than the other selected house
# If that is the case check the cable lenghts of houses to other battery if sum cable length of new situation is shorter than original cable length 
# If that is the case execute the switch of battery
# Break
