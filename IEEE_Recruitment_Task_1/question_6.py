### THE FOLLOWING CODE IS WEBSCRAPING THE CUTOFF DATA FROM THE WEBSITE TO CREATE INITIAL LISTS
### SKIP TO LINE 45 FOR CODE RELATED TO QUESTION AFTER THE LIST HAS BEEN CREATED

import requests                     # imports requests library for making HTTP requests and handling responses
from bs4 import BeautifulSoup       # imports BeautifulSoup to scrape data from raw HTML (no JavaScript)


response = requests.get('https://www.bitsadmission.com/fd/BITSAT_cutOffs.html?yr=2024-2025')    # sends GET request to server and stores response object

soup = BeautifulSoup(response.content,'html.parser')    # creates HTML parse tree from unformatted HTML 

yeardata = soup.find('div',id='2024-2025')              # finds and stores 2024-2025 division from HTML

campi = yeardata.find_all('table')                      # creates list of all campus-wise tables present in 2024-2025 division HTML


# First, it will go through all branch-wise table rows in each campus' table and create a list of them and replace them in the campi list
for campus in range(len(campi)):
    campi[campus] = campi[campus].find_all('tr')
    
    # Then replace all the CSS+HTML with just the HTML text in the nested lists of data
    for branch in range(len(campi[campus])):
        campi[campus][branch] = campi[campus][branch].find_all('span')

        # Then extract just the text and replace each individual data stored in the lists of table data
        for data in range(len(campi[campus][branch])):
            campi[campus][branch][data] = campi[campus][branch][data].get_text()


theActualList = campi[0]+campi[1]+campi[2]      # flatten the campi list from 3-dimensional to 2-dimensional
l = []                                          # this will be the list of censored data actually asked for in the question


# sadly, now removing any branches from the scraped data that were not asked for in the original question, and formatting it
for eachData in theActualList:
    try:
        if eachData[1] in ['B.E. Computer Science','B.E. Chemical','M.Sc. Biological Sciences','M.Sc. Economics']:
            l.append(tuple(eachData[0:3]))
    except:
        pass

print(l,'\n')       # prints the list which was in the question


### CONVERSION OF LIST TO DICTIONARY AS FOLLOWS --

d = dict()                      # creates a dictionary

for i in l:                     # iterates through list elements
    if i[0] not in d:           # if campus wasn't already in dictionary
        d[i[0]] = {i[1]:i[2]}   # add campus to dictionary with its value being a nested dictionary {branch:marks} from the list element

    else:                       # else campus must already be in the dictionary
        d[i[0]][i[1]] = i[2]    # so just add the item {branch:marks} to the value which is a nested dictionary

print(d)                        # prints the dictionary
