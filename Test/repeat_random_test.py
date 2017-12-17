from main import main
from Classes.neighborhood_classes import Neighborhood_class
import sys
import time


def repeat():
	t0 = time.time()

	all_info = Neighborhood_class("long")
	best_solution = Neighborhood_class("long")
	best_solution.cable_length = 9999999999
	print(best_solution.cable_length)
	improvement_rate = []
	solution_list = []

	f1 = sys.stdin
	for i in range (0, 2):
		print("Dit is het " + str(i) + "e couplet.")
		repeat = i

		f = open('input.txt','r')
		sys.stdin = f
		solution = main(a = "a")
		f.close()

		solution_list.append([i, solution])
			
		if solution.cable_length < best_solution.cable_length:
			best_solution = solution

			improvement_rate.append([i, best_solution.cable_length])
		return repeat
			
	sys.stdin = f1	

	t1 = time.time()

	print("En de winnaar heeft kabellengte:")	
	print(best_solution.cable_length)

	print("Check this!")
	print(improvement_rate)

	print ("All solutions:")
	print(solution_list)

	very_long_string = ""
	for house in best_solution.houses:
		very_long_string += "House " + str(house.id) + " on (" + str(house.x) + "," + str(house.y) + ") with voltage " + str(house.voltage) + " connected to battery " + str(house.battery_no) + ". \n" 
	print(very_long_string)	

	print("Running time:", t1-t0)

repeat()

	