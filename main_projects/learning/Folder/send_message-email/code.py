import smtplib
from email.mime.text import MIMEText
msg = MIMEText('Message text')
# me == email отправителя
# you == email получателя
msg['Subject'] = 'Test message'
msg['From'] = me
msg['To'] = you
s = smtplib.SMTP('')
s.sendmail(me, [you], mesg.as_string())
s.quit()
