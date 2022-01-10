# Import sqrt and pow functions for calculations
from math import sqrt
from math import pow

class distanceandmidpointcalculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(x1, y1, x2, y2):
        # Calculate the distance between 2 points
        dx = pow(x2 - x1, 2)
        dy = pow(y2 - y1, 2)
        distance = sqrt(dx + dy)

        # Log calculated distance
        print("Distance between (" + x1 + "," + y1 + ") and (" + x1 + "," + y1 + ") is " + distance)

        # Return the distance between the points
        return distance

    def midpoint(x1, y1, x2, y2):
        # Calculate midpoint location
        midx = (x1 + x2)/2
        midy = (y1 + y2)/2

        # Add points to array point
        # This is done for formatting as one return
        point = [midx, midy]

        # Log calculated midpoint
        print("Midpoint between (" + x1 + "," + y1 + ") and (" + x1 + "," + y1 + ") is (" + point[0] + "," + point[1] + ")")

        # Return point array
        return point