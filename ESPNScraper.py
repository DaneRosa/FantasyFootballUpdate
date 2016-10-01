#ESPN web Fantasy Football Scraper
#Takes the information from a league and returns it as different data structures
from bs4 import BeautifulSoup
from urllib.request import urlopen



def getSoup(url):
	http = urlopen(url)
	soup = BeautifulSoup(http.read(), "html.parser")
	return soup


def getWeeklyTeamAndScoreDictionary(weekNumber):
	scoreboardUrl = "http://games.espn.com/ffl/scoreboard?leagueId=1940569&matchupPeriodId=" + str(weekNumber)
	soup = getSoup(scoreboardUrl)
	weeklyTeamScoresDict = {}
	for i in range(1,9):
		tableRowId = 'teamscrg_' + str(i) + '_activeteamrow'
		teamScore = soup.find("tr", id=tableRowId).find("td",class_="score").string
		teamName = soup.find("tr",id=tableRowId).find("td",class_="team").find("div",class_="name").find("a").string
		weeklyTeamScoresDict.update({float(teamScore) : teamName})
	return weeklyTeamScoresDict

#scoresDict = getWeeklyTeamAndScoreDictionary(1)
#print(scoresDict)

def getTeamNameAndRecordString(team, wins, losses):
	return team + ' (' + wins + '-' + losses + ')'

def getTeamStandingsEast():
	eastDivisionStandings = []
	leagueStandingsUrl = "http://games.espn.com/ffl/standings?leagueId=1940569&seasonId=2016"
	soup = getSoup(leagueStandingsUrl)
	TeamOneName = soup.find("tr",class_="tableBody").find("a").string
	TeamOneWins = soup.find("tr",class_="tableBody").find("td").findNext("td").string
	TeamOneLosses = soup.find("tr",class_="tableBody").find("td").findNext("td").findNext("td").string
	eastDivisionStandings.append(getTeamNameAndRecordString(TeamOneName, TeamOneWins, TeamOneLosses))
	TeamTwoName = soup.find("tr",class_="tableBody").findNext("tr").find("a").string
	TeamTwoWins = soup.find("tr",class_="tableBody").findNext("tr").find("td").findNext("td").string
	TeamTwoLosses = soup.find("tr",class_="tableBody").findNext("tr").find("td").findNext("td").findNext("td").string
	eastDivisionStandings.append(getTeamNameAndRecordString(TeamTwoName,TeamTwoWins,TeamTwoLosses))
	TeamThreeName = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").find("a").string
	TeamThreeWins = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").find("td").findNext("td").string
	TeamThreeLosses = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
	eastDivisionStandings.append(getTeamNameAndRecordString(TeamThreeName,TeamThreeWins,TeamThreeLosses))
	TeamFourName = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").find("a").string
	TeamFourWins = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
	TeamFourLosses = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
	eastDivisionStandings.append(getTeamNameAndRecordString(TeamFourName,TeamFourWins,TeamFourLosses))
	return eastDivisionStandings

def getTeamStandingsWest():
	westDivisionStandings = []
	leagueStandingsUrl = "http://games.espn.com/ffl/standings?leagueId=1940569&seasonId=2016"
	soup = getSoup(leagueStandingsUrl)
	TeamOneName = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").find("a").string
	TeamOneWins = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").find("td").findNext("td").string
	TeamOneLosses = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").find("td").findNext("td").findNext("td").string
	westDivisionStandings.append(getTeamNameAndRecordString(TeamOneName,TeamOneWins,TeamOneLosses))
	TeamTwoName = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").findNext("tr").find("a").string
	TeamTwoWins = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").findNext("tr").find("td").findNext("td").string
	TeamTwoLosses = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").findNext("tr").find("td").findNext("td").findNext("td").string
	westDivisionStandings.append(getTeamNameAndRecordString(TeamTwoName,TeamTwoWins,TeamTwoLosses))
	TeamThreeName = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").findNext("tr").findNext("tr").find("a").string
	TeamThreeWins = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").findNext("tr").findNext("tr").find("td").findNext("td").string
	TeamThreeLosses = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
	westDivisionStandings.append(getTeamNameAndRecordString(TeamThreeName,TeamThreeWins,TeamThreeLosses))
	TeamFourName = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").find("a").string
	TeamFourWins = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
	TeamFourLosses = soup.find("table",class_="tableBody").findNext("table").find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
	westDivisionStandings.append(getTeamNameAndRecordString(TeamFourName,TeamFourWins,TeamFourLosses))
	return westDivisionStandings

#DEBUGGING
#print(getTeamStandingsEast())
#print(getTeamStandingsWest())
#scoreList = list(getWeeklyTeamAndScoreDictionary(3).keys())
#scoreList.sort()
#print(scoreList)
