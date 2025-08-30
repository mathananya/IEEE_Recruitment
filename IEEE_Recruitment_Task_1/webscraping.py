import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.bitsadmission.com/fd/BITSAT_cutOffs.html?yr=2024-2025')

soup = BeautifulSoup(response.content,'html.parser')

yeardata = soup.find('div',id='2024-2025')

campi = yeardata.find_all('table')      #iBelieveInLatin

for campus in range(len(campi)):
    campi[campus] = campi[campus].find_all('tr')
    for branch in range(len(campi[campus])):
        campi[campus][branch] = campi[campus][branch].find_all('span')
        for data in range(len(campi[campus][branch])):
            campi[campus][branch][data] = campi[campus][branch][data].get_text()


theActualList = campi[0]+campi[1]+campi[2]
l = []
for eachData in theActualList:
    try:
        if eachData[1] in ['B.E. Computer Science','B.E. Chemical','M.Sc. Biological Sciences','M.Sc. Economics']:
            l.append(tuple(eachData[0:3]))
    except:
        pass
    
print(l)

## NOW THE ACTUAL PROGRAM STARTS. IGNORE ABOVE IF BEHIND ON CLASSWORK.

d = dict()
for city in l:
    d[city] = 
