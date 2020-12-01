import random 
import os 
import smtplib

email_address = os.environ.get('EMAIL_USER') 

password = os.environ.get('EMAIL_PASS') 

l = { os.environ.get('CATAN_USER'): os.environ.get('EMAIL_PASS'),\
      'prakashsingh.mony@gmail.com': 'Catanuni@777',\
      'aldrin.bombay@gmail.com': 'Atos@123',\
      'harsh.s.goyal@gmail.com': 'Harsh@123'\
    }

emails = [i for i in l.keys()]
subject = 'Catan Login'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(email_address, password)

    for i in emails:
        x, y = random.choice(list(l.items()))
        body = f'username: {x}\npassword: {y}\n\n Good Luck! Have Fun!'
        msg = f'Subject: {subject}\n\n{body}'
        del l[x]
        smtp.sendmail(email_address, i, msg)
