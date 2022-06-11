import random
import numpy as np
import pylab

# n is the # of steps 
n = 1000
# initial values and x and y are the cordinates 
x =  np.zeros(n)
y =  np.zeros(n)

direction =["EAST","WEST", "NORTH", "SOUTH"]

for i in range(1,n):
    step = np.random.choice(direction)

    if step == "EAST":
        x[i] = x[i-1] +1
        y[i] = y[i-1]

    elif step == "WEST":
        x[i] = x[i-1] -1
        y[i] = y[i-1]
    elif step == "NORTH":
        x[i] = x[i-1] +1
        y[i] = y[i-1]

    elif step == "SOUTH":
        x[i] = x[i-1] -1
        y[i] = y[i-1]

pylab.plot.title("Random walk in 2D")
pylab.plot(x,y)
pylab.show()