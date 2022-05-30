import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

msg = EmailMessage()
msg['subject'] = 'python notification'
msg['from'] = EMAIL_ADDRESS
msg['To'] = 'seungiri841@gmail.com'
msg.set_content('from sunil')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    smtp.send_message(msg)