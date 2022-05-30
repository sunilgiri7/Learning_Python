# rcsobrdxoyvaqgux


# import webbrowser


# webbrowser.open('https://google.com')

# from turtle import pd
# import pandas as pd
# print(pd.datetime.now())
# from email.policy import SMTP
import os
import smtplib

from flask import session

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
     subject = 'python notification'
     body = 'sunil'
     
     msg = f'Subject: {subject}\n\n{body}'

     smtp.sendmail(EMAIL_ADDRESS, 'seungiri841@gmail.com',msg)
