#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:13:39 2019

@author: nachiketpusalkar
"""

#git changed something

from bs4 import BeautifulSoup
import requests
import csv


source = requests.get('https://wowwiki.fandom.com/wiki/Warcraft_III_hero_units').text

soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())
total_list = []
y = []
z= []
spells = []

for content in soup.find_all('article', class_= 'WikiaMainContent'):

    listofcontents = content.find('div', class_= 'mw-content-ltr mw-content-text')


    for heros in listofcontents.find_all('li'):
        total_list.append(heros.text)
        
        #print(total_list[0][:-1])
        for x in heros.find_all('a'):
            y.append(x.get('href'))
            
for i in y:
    if i[0] == '/':
        z.append(i)

z = [z for z in z if z[6:8] != 'Wa']
z = [z for z in z if z[6:9] != 'Ran']
z = z[0:15]




for links in z:
    sources = 'https://wowwiki.fandom.com/' + links
   
    source2 = requests.get(sources).text

    soup = BeautifulSoup(source2, 'lxml')

    for content2 in soup.find_all('h3', class_ = ''):
        spells.append(content2.span.text)
        
#print(spells[0])


for j in range(0, len(spells)):
    if spells[j][0] == ' ':
        spells[j] = spells[j][1:]
        
    
        
spells2 = [spells[i:i+4] for i in range(0, len(spells), 4)]








csv_file = open('wc3.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Heroes', 'Spell 1', 'Spell 2', 'Spell 3', 'Ultimate'])

total_list = total_list[0:15]


i = 0
total_list.remove(total_list[-2])

for names in total_list:
    names = names.split('\n')
    names = names[0] 
    csv_writer.writerow([names, spells2[i][0], spells2[i][1], spells2[i][2], spells2[i][3]])
    i += 1

    







csv_file.close()
