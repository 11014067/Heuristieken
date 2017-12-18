# This function repeats the main with a certain input.

from main import main
from Classes.neighborhood_classes import Neighborhood_class
import sys
import time

# start a timer
t0 = time.time()

improvement_rate = []
best_solution = Neighborhood_class("long")
best_solution.cable_length = 9999999999

# stores the last system path
f1 = sys.stdin

# start 150000 iterations
for i in range (0, 150000):
	
	# opens a text file with the commands
	f = open('input.txt','r')
	sys.stdin = f
	solution = main(a = "a")
	f.close()
	
	# check if you found a better cable length
	if solution.cable_length < best_solution.cable_length:
		best_solution = solution
		improvement_rate.append([i, best_solution.cable_length])
		
# restore the last system path
sys.stdin = f1	

# stop timer
t1 = time.time()

# print the results
print("Best cable length: ", best_solution.cable_length)
print("Improvement rate: ", improvement_rate)
best_solution.show_houses()
print("Running time:", t1-t0)	