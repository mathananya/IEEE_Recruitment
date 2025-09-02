from numpy import *                     # imports all numpy functions
import matplotlib.pyplot as plt         # imports matplotlib functions under alias

xmatrix = random.normal(loc=0,scale=1,size=(1000,2))    # generates matrix of 1000 pairs of randomised normalised integers
print(xmatrix)                                          # prints matrix

plt.scatter(xmatrix[:,0],xmatrix[:,1],s=0.7)            # creates scatter plot of all points in matrix using values as x,y coordinates
plt.title("Randomly generated normal distribution")     # adds title to graph
plt.xlabel("X-Values")                                  # adds label to x-axis
plt.ylabel("Y-Values")                                  # adds label to y-axis

plt.show()          # displays scatter plot of normalised randomised points
