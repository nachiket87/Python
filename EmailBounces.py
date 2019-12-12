#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 23:09:40 2019

@author: nachiketpusalkar
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:52:28 2019

@author: nachiketpusalkar
"""


from exchangelib import DELEGATE, Account, Credentials
from bs4 import BeautifulSoup
import csv


username1 = input('Username: ')
password1 = input('Password: ')

credentials = Credentials(
    username=username1,  
    password=password1
)
account = Account(
    primary_smtp_address=username1, 
    credentials=credentials, 
    autodiscover=True, 
    access_type=DELEGATE
)



csvFile = open('bounces5.csv', 'w')
writer = csv.writer(csvFile)

for i in range(0, 500, 50):
    for item in account.inbox.all().order_by('-datetime_received')[i:i+50]:
        if item.subject != None and len(item.subject) >= 14:
            if item.subject[0:14] == 'Undeliverable:' or item.subject[0:17] == 'Delivery delayed:':
                soup = BeautifulSoup(item.body, 'lxml')
                try:
                    writer.writerow([soup.a['href'][7:]])
                    print(soup.a['href'][7:])
                except:
                    continue

         
    


csvFile.close()

