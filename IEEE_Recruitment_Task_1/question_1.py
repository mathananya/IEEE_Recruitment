
n = int(input('Enter an integer: '))    # taking integer input for number of lines

for i in range(1,n+1):      # for each line from 1 to n to be printed,
    print(' '*(n-i)+'*'*i)  # print the number of spaces and stars using line index to calculate
