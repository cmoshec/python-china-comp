from bs4 import BeautifulSoup
import requests
import re
import csv
import random
from time import sleep

#open here the file ChinaSearchList.csv, copy the names to the file , remove any spaces, and save. the best way is to prepare the list in a csv file in excel and to copy the list and paste to a mail in gmail the results of the search will be exported to ChinaList.csv
#all the letters in the name are converted to capitals as in the website. the string is also trimed
print('searching')


print('Searching...','\n')
pubNum=[]
with open('ChinaSearchList.csv','r') as csv_file_read:
    csv_reader=csv.reader(csv_file_read)
    for line in csv_reader:
         pubNum.append(line[0].upper().strip())
         print(line[0])
         
csv_file=open('ChinaList.csv','w')
csv_writer=csv.writer(csv_file)


url='https://www.chemsafetypro.com/Topics/Cosmetics/China_IECIC_Finder.html'
r = requests.get(url)
data = r.text

soup = BeautifulSoup(data,'html.parser')
tbody = soup.get_text()         

i=0
print('\n')

for pn in pubNum:


    x=pubNum[i]
    i=i+1
    if x in tbody:
       print(x,' found')
       found='found'
    else:
       print(x,' not found')
       found='not found'
    csv_writer.writerow([x,found])
    
print('\n','exported to ChinaList.csv')