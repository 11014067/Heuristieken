# Algorithms folder

## Sorting

The sorting algotithm sorts the houses and batteries on x-coordinate, y-coordinate, voltage or random.
After sorting it go and try to link the houses to the first battery they fit on.

## Distance

The distance algorithm looks at the distance from each house to each battery. 
It sorts the batteries on x-coordinate, y-coordinate, voltage or random after which each battery gets the first house of there list that fits and is not linked yet.
In this way all the batteries will have one house linked to them before the first battery in the list gets linked to a second house.

## Free batteries

This algorithm looks at the grid of houses as if it has a lot of overlapping matrices. It puts the batteries in (if posible non-overlaying) matrices with the most houses insite of them.

## Non-itterative

The non-itterative algorithm also looks at the difference between each house and each battery.
But unlike the distance algorithm it does not itteratively pass through the batteries.
The non-itterative algorithm looks at the shortest distance between any house and any battery and tries to link those two. 
This way, unlike the distance algorithm, a battery in an area with a lot of houses will fill up a lot quicker.

## Hillclimber

The hillclimber gets a solved list of connected houses and batteries but tries to switch two houses between two batteries to see if that lowers the cost of the neighborhood.
It switches two houses as many times as wanted.
