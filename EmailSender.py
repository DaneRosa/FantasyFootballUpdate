#
# Composes and sends the league email message
#
from email.header import Header
from email.mime.text import MIMEText
from getpass import getpass
from smtplib import SMTP_SSL
from EmailMessageBuilder import getMessageHTML
from StaticContent import LeagueInfo

login, password = 'rpossardt@gmail.com', getpass()
testEmail = 'rpossardt@gmail.com'
week = 5


# create message
msg = MIMEText(getMessageHTML(week, LeagueInfo.sectionTitlesBTB , LeagueInfo.leagueScoreboardURLBTB , LeagueInfo.leagueStandingsURLBTB), 'html')
msg['Subject'] = Header(LeagueInfo.sectionTitlesBTB[0] + ' Week ' + str(week), 'utf-8')
msg['From'] = login
#msg['To'] = ", ".join(leagueEmails)
msg['To'] = testEmail

msg1 = MIMEText(getMessageHTML(week, LeagueInfo.sectionTitlesTFF , LeagueInfo.leagueScoreboardURLTFF , LeagueInfo.leagueStandingsURLTFF), 'html')
msg1['Subject'] = Header(LeagueInfo.sectionTitlesTFF[0] + ' Week ' + str(week),'utf-8')
msg1['From'] = login
msg1['To'] = testEmail
# send it via gmail
s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
s.set_debuglevel(1)
try:
    s.login(login, password)
    s.sendmail(msg['From'], testEmail, msg.as_string())
    s.sendmail(msg1['From'], testEmail, msg1.as_string())
finally:
    s.quit()