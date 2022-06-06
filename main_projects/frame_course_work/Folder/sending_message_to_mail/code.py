# import the smtplib module. It should be included in Python by default
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login("maxomah123@gmail.com", "starrk090910")

msg = MIMEMultipart()

name = 'starrkroo@gmail.com'

# message = message_template.substitue(PERSON_NAME=name)

msg['From'] = 'maxomha123@gmail.com'
msg['To'] = name
msg['Subject'] = 'This is for testing'

msg.attach(MIMEText("hello", 'plain'))

s.send_message(msg)
