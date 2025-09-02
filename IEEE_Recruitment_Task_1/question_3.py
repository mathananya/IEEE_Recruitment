from numpy import *     # imports numpy module

def x5matrix():             # creating a function since this matrix is needed for question_4.py, and will be called there
    matrix = random.randint(1,100,size=(5,5))       # creates a 2-D 5x5 matrix with random integers between 1 and 100
    return matrix                                   # returns the new matrix to calling variable

if __name__ == '__main__':  # necessary to stop extra code from running when importing x5matrix() to question_4.py

    matrix = x5matrix()                                 # calls x5matrix() function and assigns returned value to variable
    print('MATRIX:\n',matrix,'\n')                      # prints matrix
    print('Maximum number = ', amax(matrix))            # prints maximum value of matrix
    print('Minimum number = ', amin(matrix))            # prints minimum value of matrix
    print('Mean of matrix = ', mean(matrix),'\n')       # prints mean value of matrix

    normalisedMatrix = (matrix-amin(matrix))/(amax(matrix)-amin(matrix))        # normalises each value of matrix between 0 and 1 range

    print('FLATTENED NORMALISED MATRIX:\n',normalisedMatrix.reshape(-1)) # could have also used .flatten() over here, turns 2-D matrix to 1-D
