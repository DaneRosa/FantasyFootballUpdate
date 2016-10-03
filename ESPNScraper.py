#ESPN web Fantasy Football Scraper
#Takes the information from a league and returns it as different data structures
from bs4 import BeautifulSoup
from urllib.request import urlopen



def getSoup(url):
	http = urlopen(url)
	soup = BeautifulSoup(http.read(), "html.parser")
	return soup

def addTeamAndPFToDict(score, teamName, dictionary):
	if score in dictionary:
		newTeamNames = dictionary[score] + '<strong> and </strong>' + teamName
		dictionary.update({score : newTeamNames})
	else:
		dictionary.update({score : teamName})

def getWeeklyTeamAndScoreDictionary(weekNumber):
	scoreboardUrl = "http://games.espn.com/ffl/scoreboard?leagueId=1940569&matchupPeriodId=" + str(weekNumber)
	soup = getSoup(scoreboardUrl)
	weeklyTeamScoresDict = {}
	for i in range(1,9):
		tableRowId = 'teamscrg_' + str(i) + '_activeteamrow'
		teamScore = soup.find("tr", id=tableRowId).find("td",class_="score").string
		teamName = soup.find("tr",id=tableRowId).find("td",class_="team").find("div",class_="name").find("a").string
		addTeamAndPFToDict(float(teamScore), teamName, weeklyTeamScoresDict)
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

def getLeaguePFDict():
	teamAndPointsForDict = {}
	leagueStandingsUrl = "http://games.espn.com/ffl/standings?leagueId=1940569&seasonId=2016"
	soup = getSoup(leagueStandingsUrl)
	
	#East division:
	teamOneEastName = soup.find("tr",class_="bodyCopy").find("td").find("a").string
	teamOneEastPF = soup.find("tr",class_="bodyCopy").find("td").findNext("td").string
	teamTwoEastName = soup.find("tr",class_="bodyCopy").findNext("tr").find("td").find("a").string
	teamTwoEastPF = soup.find("tr",class_="bodyCopy").findNext("tr").find("td").findNext("td").string
	teamThreeEastName = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").find("a").string
	teamThreeEastPF = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").findNext("td").string
	teamFourEastName = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").find("a").string
	teamFourEastPF = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
	
	#West division:
	teamOneWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").find("td").find("a").string
	teamOneWestPF = soup.find("table", id="xstandTbl_div1").find("tr",class_="bodyCopy").find("td").findNext("td").string
	teamTwoWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").find("td").find("a").string
	teamTwoWestPF = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").find("td").findNext("td").string
	teamThreeWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").find("a").string
	teamThreeWestPF = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").findNext("td").string
	teamFourWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").find("a").string
	teamFourWestPF = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
	
	#addTeamAndPFToDict(score, teamname, dictionary)
	# East:
	addTeamAndPFToDict(float(teamOneEastPF), teamOneEastName, teamAndPointsForDict)
	addTeamAndPFToDict(float(teamTwoEastPF), teamTwoEastName, teamAndPointsForDict)
	addTeamAndPFToDict(float(teamThreeEastPF), teamThreeEastName, teamAndPointsForDict)
	addTeamAndPFToDict(float(teamFourEastPF), teamFourEastName, teamAndPointsForDict)
	# West:
	addTeamAndPFToDict(float(teamOneWestPF), teamOneWestName, teamAndPointsForDict)
	addTeamAndPFToDict(float(teamTwoWestPF), teamTwoWestName, teamAndPointsForDict)
	addTeamAndPFToDict(float(teamThreeWestPF), teamThreeWestName, teamAndPointsForDict)
	addTeamAndPFToDict(float(teamFourWestPF), teamOneEastName, teamAndPointsForDict)
	
	return teamAndPointsForDict

def getWestDivisionPFDict():
	teamAndPointsForDict = {}
	leagueStandingsUrl = "http://games.espn.com/ffl/standings?leagueId=1940569&seasonId=2016"
	soup = getSoup(leagueStandingsUrl)
	TeamOneName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").find("td").find("a").string
	TeamOnePF = soup.find("table", id="xstandTbl_div1").find("tr",class_="bodyCopy").find("td").findNext("td").string
	teamAndPointsForDict.update({float(TeamOnePF) : TeamOneName})
	TeamTwoName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").find("td").find("a").string
	TeamTwoPF = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").find("td").findNext("td").string
	teamAndPointsForDict.update({float(TeamTwoPF) : TeamTwoName})
	TeamThreeName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").find("a").string
	TeamThreePF = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").findNext("td").string
	teamAndPointsForDict.update({float(TeamThreePF) : TeamThreeName})
	TeamFourName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").find("a").string
	TeamFourPF = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
	teamAndPointsForDict.update({float(TeamFourPF) : TeamFourName})
	return teamAndPointsForDict

#DEBUGGING
#print(getTeamStandingsEast())
#print(getTeamStandingsWest())
#scoreList = list(getWeeklyTeamAndScoreDictionary(3).keys())
#scoreList.sort()
#print(scoreList)
#soup = getSoup("http://games.espn.com/ffl/standings?leagueId=1940569&seasonId=2016")
#print(soup.find("tr",class_="bodyCopy").findNext("tr").find("td").find("a").string)
#print(soup.find("tr",class_="bodyCopy").findNext("tr").find("td").findNext("td").string)
#print(getWestDivisionPFDict())
