import random

def TESTsorting_algorithm(A):
	
	#Algorithm
	print ("Sorting...")
	A.batteries = sorted(A.batteries, key=lambda battery: getattr(battery, A.battery_sort))
	
	A.houses = sorted(A.houses, key=lambda house: getattr(house, A.house_sort))
	
	
	# link houses and batteries
	solution = True
	for house in A.houses:
		house_placed = False
		i = 0
		while (house_placed == False):
			if (A.batteries[i].add_house(house)):
				house_placed = True
			i+=1
			if (i > len(A.batteries) - 1 and house_placed == False):
				solution = False
				break
	
	for i in range(0, len(A.batteries) - 1):
		print (A.batteries[i].spare_voltage)

	return [A, solution]