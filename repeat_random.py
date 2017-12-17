from main import main
from Classes.neighborhood_classes import Neighborhood_class
import sys
import time

t0 = time.time()

best_solution = Neighborhood_class("long")
best_solution.cable_length = 9999999999
print(best_solution.cable_length)

improvement_rate = []
all_solutions = []

f1 = sys.stdin
for i in range (0, 2):
	print("Dit is het " + str(i) + "e couplet.")
	    
	f = open('input.txt','r')
	sys.stdin = f
	solution = main(a = "a")
	f.close()

	all_solutions.append([i,solution.cable_length])
		
	if solution.cable_length < best_solution.cable_length:
		best_solution = solution

		improvement_rate.append([i, best_solution.cable_length])
		
sys.stdin = f1	

t1 = time.time()

print("The final cable_length of each iteration is: {}".format(all_solutions))

print("En de winnaar heeft kabellengte:")	
print(best_solution.cable_length)

print("Check this!")
print(improvement_rate)

very_long_string = ""
for house in best_solution.houses:
	very_long_string += "House " + str(house.id) + " on (" + str(house.x) + "," + str(house.y) + ") with voltage " + str(house.voltage) + " connected to battery " + str(house.battery_no) + ". \n" 
print(very_long_string)	

print("Running time:", t1-t0)

	