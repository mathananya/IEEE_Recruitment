while True:         # until input is of correct format, keep asking user
    
    para = input('Enter paragraph:\n')              # asking for user paragraph input
    words = para.split()                            # creating a list of words in paragraph, separated by whitespace
    
    if len(words) > 100:                            # checking whether word count is over limit
        print('Enter less than 100 words.')         # tells user to follow input constraints
        continue                                    # goes back to start of while loop
    
    else:               # if input was of correct format,
        break           # then exits the while loop


palindromeExists = False    # starts with palindromeExists as false until found

for thisWord in words:                                  # iterates through all the words
    if thisWord.lower() == thisWord[::-1].lower():      # checks if reverse of word is same as word itself (lowercaps)
        palindromeExists = True                         # if word is a palindrome then set to True and print it
        print(thisWord)

if not palindromeExists:        # if palindrome was never found, prints 0
    print(0)


""" NOTE:- Could also have used for-else and break combination instead of setting the variable palindromeExists """
