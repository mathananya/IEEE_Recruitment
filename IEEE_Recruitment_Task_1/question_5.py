from numpy import *
import matplotlib.pyplot as plt

xmatrix = random.normal(loc=0,scale=1,size=(1000,2))
print(xmatrix)

plt.scatter(xmatrix[:,0],xmatrix[:,1],s=0.7)
plt.title("Randomly generated normal distribution")
plt.xlabel("X-Values")
plt.ylabel("Y-Values")

plt.show()
