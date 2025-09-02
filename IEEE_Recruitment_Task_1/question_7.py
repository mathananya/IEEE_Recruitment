# creating 2 lists
list1 = [3, 4, 5, 1, 4, 6, 1, 7, 7]
list2 =[5, 8, 2, 9, 9, 4, 6, 3]

finalList = list(set(list1) & set(list2))   # taking intersection of unique elements by sets and converting back to a list
print(finalList)    # displaying output list
