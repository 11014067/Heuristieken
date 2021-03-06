# Project SmartGrid

In this project there is a hypothetical neighborhood with 150 houses. Each of them 
create electricity through solar panels and need to store that in a battery. These 
batteries are collective and spread through the neighborhood, connected to the houses
by electricity cables.
Given the location of the houses, the goal of this problem is to the lowest price to 
connect this neighborhood, given certain prices for cable and batteries.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

To run the following code, make sure you have at least 4 MB free space on your computer and
that you installed python version 3.6.3. If you have a previous version, please go to 
https://www.python.org/downloads/ and get yourself the proper version.

### Installing

Go to https://github.com/11014067/Heuristieken and download the folder "Heuristieken" to your
local machine. You can either download the zip and unpack it, of copy paste all folders to a 
newly created folder. In the last case, make sure the folder is empty (including possible 
hidden files).

## Getting started

To start the algorithms and recreate the solutions of the problem, you open your terminal and 
go to the folder where you saved 'Heuristieken'. Enter the command:

```
python main.py
```

or

```
py -3 main.py
```

Now follow the instructions on the screen.


You can also run multiple random samples with random repeat, which will be explained further down this page with:
```
python repeat_random.py
```

or

```
py -3 repeat_random.py
```

### Random repeat

This commando makes it possible to run a solution multiple times. To run this function, please open the file "input.txt". 
In this file you type the answers you normally give in the to the regular main.py.
The program will now automatically run this command 150000 times and stores every iteration that grands a imporvement.

## Infrastructure

There are several sub folders containing functions, algorithms, visualizations and datasets, 
to increase conspectus and facilitate reusing certain aspects of the code. A quick summary 
of all the folder and their containments:

* Algorithms - The codes needed for the sorting, switching and greedy algorithms.
* Classes - Classes and classes specific functions necessary for the algorithms.
* Deprecated - Older files that aren't used anymore.
* Experimentation - All the files with conclusions and results for our experiments.
* Functions - All assisting functions, like plotting, downloadling data and more.
* Information - Information about the case and the neighborhoods: datasets with coordinates 
				and computed upper and lower bounds for the solution.
* Test - New versions of functions and algorithms, for research purposes only.
* Visual_solutions - Visual representations of solutions to the problems. The main.py code is 
					 designed to save newly created solutions automatically here.
* ignore - Necessary to ignore *.pyc files, not necessary to run any algorithm.

## Authors

* **Daphne Box** - *Contributor* 
* **Sanne Oud** - *Contributor* 
* **Jasper Steven den Duijf** - *Contributor* 

## Acknowledgments

* This project is still under construction and therefore not every file might be in the 
proper location. Our apologies for the inconvenience. If the main.py file isn't working,
try to go back in the branch to get an older version.
* In case of questions and/or remarks, please contact us on jasperdenduijf@hotmail.com.
* We are not responsible for any damage done to your machine. Use this algorithm on your own risk.


