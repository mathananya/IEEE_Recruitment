from question_3 import x5matrix     # imports x5matrix() from question_3.py which generates random 5x5 matrix
import numpy                        # imports numpy module

matrix = x5matrix()                 # calls x5matrix() function and stores random matrix in variable

x3matrix = matrix[1:4,1:4]          # slices 2nd to 4th elements from 2nd to 4th rows (central 3x3 matrix)

dotproduct = numpy.dot(x3matrix[0],x3matrix[:,-1])       # dot product of first row and last element of all rows, i.e. the last column

print(x3matrix)                         # displays 3x3 matrix,
print("Dot product = ",dotproduct)      # and dot product on screen
