#
# Composes and sends the league email message
#
from email.header import Header
from email.mime.text import MIMEText
from getpass import getpass
from smtplib import SMTP_SSL
from EmailMessageBuilder import getMessageHTML

login, password = 'rpossardt@gmail.com', getpass()
testEmail = 'rpossardt@gmail.com'
leagueEmailsBTB = []
leagueEmailsTFF = []

sectionTitlesBTB = ['Busby Tight Buttholes','Local Faggot: ', 'Huge Faggot: ','Gay Faggot: ','National Faggot: ']
sectionTitlesTFF = ['Tolland Fantasy Buttball', 'Most Points Scored: ','Least Points Scored: ','League Scoring Leader: ','League Scoring Loser: ']
week = 3
# create message
msg = MIMEText(getMessageHTML(week, sectionTitlesBTB,'http://games.espn.com/ffl/scoreboard?leagueId=1140963&scoringPeriodId=', 'http://games.espn.com/ffl/standings?leagueId=1140963&seasonId=2016'), 'html')
msg['Subject'] = Header(sectionTitlesBTB[0] + ' Week ' + str(week), 'utf-8')
msg['From'] = login
#msg['To'] = ", ".join(leagueEmails)
msg['To'] = testEmail

msg1 = MIMEText(getMessageHTML(week, sectionTitlesTFF,'http://games.espn.com/ffl/scoreboard?leagueId=1940569&scoringPeriodId=','http://games.espn.com/ffl/standings?leagueId=1940569&seasonId=2016'), 'html')
msg1['Subject'] = Header(sectionTitlesTFF[0] + ' Week ' + str(week),'utf-8')
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