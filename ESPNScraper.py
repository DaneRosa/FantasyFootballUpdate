#
#ESPN web Fantasy Football Scraper
#  Takes the information from a league and returns it as different data structures
#
from bs4 import BeautifulSoup
from urllib.request import urlopen



def getSoup(url):
	http = urlopen(url)
	soup = BeautifulSoup(http.read(), "html.parser")
	return soup

def getTeamNameAndRecordString(team, wins, losses):
	return team + ' (' + wins + '-' + losses + ')'


def addTeamAndAttributeToDict(score, teamName, dictionary):
	if score in dictionary:
		newTeamNames = dictionary[score] + '<strong> and </strong>' + teamName
		dictionary.update({score : newTeamNames})
	else:
		dictionary.update({score : teamName})

def getWeeklyTeamAndScoreDictionary(weekNumber, scoreboardURL):
	scoreboardURL += str(weekNumber)
	soup = getSoup(scoreboardURL)
	weeklyTeamScoresDict = {}
	leagueSize = 0
	for i in range(1,13):
		tableRowId = 'teamscrg_' + str(i) + '_activeteamrow'
		if soup.find("tr", id=tableRowId) is None:
			print('why can\'t you name these divs tr s nicely ESPN?')
		else:
			leagueSize+=1
			teamScore = soup.find("tr", id=tableRowId).find("td",class_="score").string
			teamName = soup.find("tr",id=tableRowId).find("td",class_="team").find("div",class_="name").find("a").string
			addTeamAndAttributeToDict(float(teamScore), teamName, weeklyTeamScoresDict)
	print("HEY THIS IS THE LEAGUE SIZE " + str(leagueSize))
	return (weeklyTeamScoresDict, leagueSize)


def getTeamStandingsEast(leagueStandingsURL,leagueSize):
	eastDivisionStandings = []
	soup = getSoup(leagueStandingsURL)
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
	#TODO: if league size > 8, we need to also add the teams that are missing.
	if int(leagueSize) == 10 or int(leagueSize) == 12:
		#Do the thing
		TeamFiveName = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("a").string
		TeamFiveWins = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
		TeamFiveLosses = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
		eastDivisionStandings.append(getTeamNameAndRecordString(TeamFiveName,TeamFiveWins,TeamFiveLosses))
	return eastDivisionStandings

def getTeamStandingsWest(leagueStandingsURL,leagueSize):
	westDivisionStandings = []
	soup = getSoup(leagueStandingsURL)
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
	if int(leagueSize) == 10 or int(leagueSize) == 12:
		#Do the thing
		TeamFiveName = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("a").string
		TeamFiveWins = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
		TeamFiveLosses = soup.find("tr",class_="tableBody").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
		westDivisionStandings.append(getTeamNameAndRecordString(TeamFiveName,TeamFiveWins,TeamFiveLosses))
	return westDivisionStandings

def getLeaguePFDict(leagueStandingsURL,leagueSize):
	teamAndPointsForDict = {}
	soup = getSoup(leagueStandingsURL)
	
	#East division:
	teamOneEastName = soup.find("tr",class_="bodyCopy").find("td").find("a").string
	teamTwoEastName = soup.find("tr",class_="bodyCopy").findNext("tr").find("td").find("a").string
	teamThreeEastName = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").find("a").string
	teamFourEastName = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").find("a").string

	teamOneEastPF = soup.find("tr",class_="bodyCopy").find("td").findNext("td").string
	teamTwoEastPF = soup.find("tr",class_="bodyCopy").findNext("tr").find("td").findNext("td").string
	teamThreeEastPF = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").findNext("td").string
	teamFourEastPF = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
	
	#West division:
	teamOneWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").find("td").find("a").string
	teamTwoWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").find("td").find("a").string
	teamThreeWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").find("a").string
	teamFourWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").find("a").string

	teamOneWestPF = soup.find("table", id="xstandTbl_div1").find("tr",class_="bodyCopy").find("td").findNext("td").string
	teamTwoWestPF = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").find("td").findNext("td").string
	teamThreeWestPF = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").findNext("td").string
	teamFourWestPF = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
	
	if int(leagueSize) == 10 or int(leagueSize) == 12:
		teamFiveEastName = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
		teamFiveEastPF = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
		addTeamAndAttributeToDict(float(teamFiveEastPF),teamFiveEastName,teamAndPointsForDict)

		teamFiveWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").find("a").string
		teamFiveWestPF = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
		addTeamAndAttributeToDict(float(teamFiveWestPF),teamFiveWestName,teamAndPointsForDict)
	#addTeamAndAttributeToDict(score, teamname, dictionary)
	# East:
	addTeamAndAttributeToDict(float(teamOneEastPF), teamOneEastName, teamAndPointsForDict)
	addTeamAndAttributeToDict(float(teamTwoEastPF), teamTwoEastName, teamAndPointsForDict)
	addTeamAndAttributeToDict(float(teamThreeEastPF), teamThreeEastName, teamAndPointsForDict)
	addTeamAndAttributeToDict(float(teamFourEastPF), teamFourEastName, teamAndPointsForDict)
	# West:
	addTeamAndAttributeToDict(float(teamOneWestPF), teamOneWestName, teamAndPointsForDict)
	addTeamAndAttributeToDict(float(teamTwoWestPF), teamTwoWestName, teamAndPointsForDict)
	addTeamAndAttributeToDict(float(teamThreeWestPF), teamThreeWestName, teamAndPointsForDict)
	addTeamAndAttributeToDict(float(teamFourWestPF), teamOneEastName, teamAndPointsForDict)
	return teamAndPointsForDict

def getLeaguePADict(leagueStandingsURL,leagueSize):
	teamAndPointsAgainstDict = {}
	soup = getSoup(leagueStandingsURL)
	
	#East division:
	teamOneEastName = soup.find("tr",class_="bodyCopy").find("td").find("a").string
	teamTwoEastName = soup.find("tr",class_="bodyCopy").findNext("tr").find("td").find("a").string
	teamThreeEastName = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").find("a").string
	teamFourEastName = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").find("a").string

	teamOneEastPA = soup.find("tr",class_="bodyCopy").find("td").findNext("td").findNext("td").string
	teamTwoEastPA = soup.find("tr",class_="bodyCopy").findNext("tr").find("td").findNext("td").findNext("td").string
	teamThreeEastPA = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
	teamFourEastPA = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
	
	#West division:
	teamOneWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").find("td").find("a").string
	teamTwoWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").find("td").find("a").string
	teamThreeWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").find("a").string
	teamFourWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").find("a").string

	teamOneWestPA = soup.find("table", id="xstandTbl_div1").find("tr",class_="bodyCopy").find("td").findNext("td").findNext("td").string
	teamTwoWestPA = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").find("td").findNext("td").findNext("td").string
	teamThreeWestPA = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
	teamFourWestPA = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
	
	if int(leagueSize) == 10 or int(leagueSize) == 12:
		teamFiveEastName = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").string
		teamFiveEastPA = soup.find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
		addTeamAndAttributeToDict(float(teamFiveEastPF),teamFiveEastName,teamAndPointsAgainstDict)

		teamFiveWestName = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").find("a").string
		teamFiveWestPA = soup.find("table",id="xstandTbl_div1").find("tr",class_="bodyCopy").findNext("tr").findNext("tr").findNext("tr").findNext("tr").find("td").findNext("td").findNext("td").string
		addTeamAndAttributeToDict(float(teamFiveWestPF),teamFiveWestName,teamAndPointsAgainstDict)
	#addTeamAndAttributeToDict(score, teamname, dictionary)
	# East:
	addTeamAndAttributeToDict(float(teamOneEastPA), teamOneEastName, teamAndPointsAgainstDict)
	addTeamAndAttributeToDict(float(teamTwoEastPA), teamTwoEastName, teamAndPointsAgainstDict)
	addTeamAndAttributeToDict(float(teamThreeEastPA), teamThreeEastName, teamAndPointsAgainstDict)
	addTeamAndAttributeToDict(float(teamFourEastPA), teamFourEastName, teamAndPointsAgainstDict)
	# West:
	addTeamAndAttributeToDict(float(teamOneWestPA), teamOneWestName, teamAndPointsAgainstDict)
	addTeamAndAttributeToDict(float(teamTwoWestPA), teamTwoWestName, teamAndPointsAgainstDict)
	addTeamAndAttributeToDict(float(teamThreeWestPA), teamThreeWestName, teamAndPointsAgainstDict)
	addTeamAndAttributeToDict(float(teamFourWestPA), teamOneEastName, teamAndPointsAgainstDict)
	return teamAndPointsAgainstDict

def getBenchWeeklyScoreDict(leagueID):
	weeklyBenchScoreDict = {}
	matchupURL = 'http://games.espn.com/ffl/boxscorequick?leagueId=' + str(leagueID) + '&teamId=1&scoringPeriodId=6&seasonId=2016&view=scoringperiod&version=quick'
	soup = getSoup(matchupURL)
	soup.find("div",id="tmInactivePts_1").string
	a = soup.find("div",id="teamInfos").find('a', {"href" : True}).findNext("a")
	for i in range(1,5):
		matchupURL = 'http://games.espn.com/ffl/boxscorequick?leagueId=' + str(leagueID) + '&teamId=' + str(i) + '&scoringPeriodId=6&seasonId=2016&view=scoringperiod&version=quick'
		soup = getSoup(matchupURL)
		leftTeamName = soup.find("div",id="teamInfos").find("div",class_="bodyCopy").find("b").string
		rightTeamName = soup.find("div",id="teamInfos").find("div",class_="bodyCopy").findNext("div",class_="bodyCopy").find("b").string
		leftTeamBenchPoints = soup.find("div", id="tmInactivePts_" + str(i))
		rightTeamNumber = soup.find("div",id="teamInfos").find('a', {"href" : True}).findNext("a")['href'][-1]
		rightTeamBenchPoints = soup.find("div", id="tmInactivePts_" + rightTeamNumber)
		addTeamAndAttributeToDict(float(leftTeamBenchPoints.string),leftTeamName,weeklyBenchScoreDict)
		addTeamAndAttributeToDict(float(rightTeamBenchPoints.string),rightTeamName,weeklyBenchScoreDict)
	return weeklyBenchScoreDict
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

print(getBenchWeeklyScoreDict(1940569))