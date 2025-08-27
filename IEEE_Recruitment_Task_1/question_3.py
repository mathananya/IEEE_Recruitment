from numpy import *

matrix = random.randint(1,100,size=(5,5))
print('MATRIX:\n',matrix,'\n')
print('Maximum number = ', amax(matrix))
print('Minimum number = ', amin(matrix))
print('Mean of matrix = ', mean(matrix),'\n')

normalisedMatrix = (matrix-amin(matrix))/(amax(matrix)-amin(matrix))

print('FLATTENED NORMALISED MATRIX:\n',normalisedMatrix.reshape(-1)) #could have also used .flatten() over here
