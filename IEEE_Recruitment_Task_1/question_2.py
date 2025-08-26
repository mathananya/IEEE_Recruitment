while True:
    para = input('Enter paragraph:\n')
    words = para.split()
    if len(words) > 100:
        print('Enter less than 100 words.')
        continue
    else:
        break

palindromeExists = False

for thisWord in words:
    if thisWord.lower() == thisWord[::-1].lower():
        palindromeExists = True
        print(thisWord)

if not palindromeExists:
    print(0)
