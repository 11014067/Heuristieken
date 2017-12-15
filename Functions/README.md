# Functions 

This folder has different helper functions.
- Ask nicely
- Bounds
- Download data
- Plot grid
- Score function
- Switcher

## Ask nicely

This function asks the user what they want to do and how they want to connect the houses and betteries.
There is a short and a long version.

### Ask nicely short

This ask nicely will ask for:
- The neighborhood to be used
- The algorithm to use
- If necessary, the battery and houses sorting method

### Ask nicely long

This ask nicely will ask for:
- The neighborhood to be used
- If the batteries should be in the most house dense places
- If the batteries should have something else than the default amount of voltage and what amount it should be for each battery
- The algorithm to use
- If necessary, the battery and houses sorting method
- If the hillclimber should be used and for how many itterations

## Bounds

This function calculates the bounds of the chosen houses and batteries combination.

## Download data

This function downloads the data from the given CSV's and TXT's.

## Plot grid

This function visualises the linked houses and batteries.

## Score function

This function calculates the price and the cable length of the connections.

## Switcher

This function switches two houses from their battery so the battery with the most room left over will have even more room for houses that could not yet be linked to a battery.
This will usually make sure an unsolved combination of houses and batteries will be solved.
