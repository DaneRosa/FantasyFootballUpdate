#Composes and sends the league email message
from email.header import Header
from email.mime.text import MIMEText
from getpass import getpass
from smtplib import SMTP_SSL
from EmailMessageBuilder import getMessageHTML

#right now using random created account
#  will use personal email in future..
login, password = 'rpossardt@gmail.com', getpass()
to = 'ryan.possardt@uconn.edu'
recipients = [to]

# create message
#msg = MIMEText(getDealString('https://meh.com'), 'plain', 'utf-8')
msg = MIMEText(getMessageHTML(1), 'html')





msg['Subject'] = Header('Last Test?', 'utf-8')
msg['From'] = login
msg['To'] = ", ".join(recipients)

# send it via gmail
s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
s.set_debuglevel(1)
try:
    s.login(login, password)
    s.sendmail(msg['From'], recipients, msg.as_string())
finally:
    s.quit()