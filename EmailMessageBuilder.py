#
# Builds the message HTML, and fills in information gathered from webscraper.
#
from ESPNScraper import getWeeklyTeamAndScoreDictionary, getTeamStandingsEast, getTeamStandingsWest, getLeaguePFDict, getLeaguePADict,getBenchWeeklyScoreDict
#inputsArray = [leagueName, mostPointsScoredTitle, LeastPointsScoredTite, mostPFTitle, LeastPFTitle]
def getMessageHTML(week, inputsArray,leagueScoreboardURL,leagueStandingsURL,leagueID):
	results = getWeeklyTeamAndScoreDictionary(week,leagueScoreboardURL)
	weeklyTeamScoresDict = results[0]
	leagueSize = int(results[1])
	weeklyTeamScoresDictKeys = list(weeklyTeamScoresDict.keys())
	weeklyTeamScoresDictKeys.sort()

	teamStandingsEast = getTeamStandingsEast(leagueStandingsURL,leagueSize)
	teamStandingsWest = getTeamStandingsWest(leagueStandingsURL,leagueSize)
	
	#Points For
	leaguePFDict = getLeaguePFDict(leagueStandingsURL,leagueSize)
	leaguePFDictKeys = list(leaguePFDict.keys())
	leaguePFDictKeys.sort()
	lowestPF = leaguePFDictKeys[0]
	lowestPFTeamName = leaguePFDict[lowestPF]
	highestPF = leaguePFDictKeys[-1]
	highestPFTeamName = leaguePFDict[highestPF]

	#Points Against
	leaguePADict = getLeaguePADict(leagueStandingsURL, leagueSize)
	leaguePADictKeys = list(leaguePADict.keys())
	leaguePADictKeys.sort()
	mostPA = leaguePADictKeys[-1]
	mostPATeamName = leaguePADict[mostPA]

	#Points left on bench
	leagueBenchScoreDict = getBenchWeeklyScoreDict(leagueID)
	leagueBenchScoreDictKeys = list(leagueBenchScoreDict.keys())
	leagueBenchScoreDictKeys.sort()
	mostPointsOnBench = leagueBenchScoreDictKeys[-1]
	mostPointsOnBenchTeamName = leagueBenchScoreDict[mostPointsOnBench]


	# Need fix for categories where numbers are now >1000
	#Use array of strings we will join later.
	emailMessageList = []
	emailMessageList.append("""
	<HTML>
<body style="min-width:100%;margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-left:0;padding-right:0;font-family:Arial, sans-serif;">
<table align="center" style="width:500px;table-layout:fixed;border-spacing:0;font:20px Arial, sans-serif;">
	<col style="width:5%">
	<col style="width:30%">
	<col style="width:20%">
<tbody>
	<tr>
		<th colspan="3" width="100%" style="background-color: lightgreen; font-size:50px;">""")
	emailMessageList.append(inputsArray[0] + """ Week """)
	emailMessageList.append(str(week) + """ Results			
		</th>
	</tr>
	""")

	emailMessageList.append("""<!--Most points scored so far -->
	<tr>
		<td colspan="3"><strong>""" + inputsArray[1] + """</strong><div style="font-size:10px">(Overall)</div></td>
	</tr>
	<tr>
		<td></td>
		<td>""" + highestPFTeamName + """</td>
		<td><div style="width:110px;height:110px;border-radius:55px;font-size:28px;color:#000;line-height:110px;text-align:center;background:lightgreen">""" + str(highestPF) + """</div></td>
	</tr>
	<tr style="height:5px;"><td colspan="3"></td></tr>""")
	
	emailMessageList.append("""<!-- Most points scored(this week) rows:-->
	<tr style="background:lightgreen;">
		<td colspan="3"><strong>""" + inputsArray[2] +"""</strong><div style="font-size:10px">(This week)</div></td>
	</tr>
	<tr style="background:lightgreen;">
		<td></td>
		<td>""" + weeklyTeamScoresDict[weeklyTeamScoresDictKeys[-1]] + """</td>
		<td><div style="width:100px;height:100px;border-radius:50px;font-size:32px;color:#000;line-height:100px;text-align:center;background:#fff">""" + str(weeklyTeamScoresDictKeys[-1]) + """</div></td>
	</tr>
	<tr style="background-color: lightgreen;height:5px;"><td colspan="3"></td></tr>""")

	emailMessageList.append("""<!-- league standings -->
	<tr>
		<td colspan="3"><strong>League Standings:</strong></td>
	</tr>
	<tr>
		<td></td>
		<td style="font-size:18px;text-decoration:underline;">East</td>
	</tr>""")

	#League Standings: 
	for i in range(0,int((leagueSize/2))):
		emailMessageList.append( 
		"""<tr style="font-size:15px">
			<td></td>
			<td colspan="2">""" + str(i + 1) + """. """ + teamStandingsEast[i] + """</td>
		</tr>""")
	
	emailMessageList.append("""
	<tr>
		<td></td>
		<td style="font-size:18px;text-decoration:underline;">West</td>
	</tr>""")
	for i in range(0,int((leagueSize/2))):
		emailMessageList.append( 
		"""<tr style="font-size:15px">
			<td></td>
			<td colspan="2">""" + str(i + 1) + """. """ + teamStandingsWest[i] + """</td>
		</tr>
	<tr style="background-color: white;height:5px;"><td></td></tr>""")

	emailMessageList.append(""" <!--Most Points Left on Bench -->
	<tr style="background:lightgreen;margin-top:10px;">
		<td colspan="3"><strong>""" + inputsArray[3]+ """</strong><div style="font-size:10px">(This week)</div></td>
	</tr>
	<tr style="background:lightgreen;">	
		<td></td>
		<td>""" + mostPointsOnBenchTeamName + """</td>
		<td><div style="width:70px;height:70px;border-radius:35px;font-size:28px;color:#000;line-height:70px;text-align:center;background:#fff">""" + str(mostPointsOnBench) + """</div></td>
	</tr>
	<tr style="background:lightgreen;height:5px;"><td colspan="3"></td></tr>
		""")

	emailMessageList.append("""<!--Least points scored(this week) rows: -->
	<tr style="margin-top:10px">
		<td colspan="3"><strong>""" + inputsArray[4] + """</strong><div style="font-size:10px">(This week)</div></td>
	</tr>
	<tr>
		<td></td>
		<td>""" + weeklyTeamScoresDict[weeklyTeamScoresDictKeys[0]] + """</td>
		<td><div style="width:80px;height:80px;border-radius:40px;font-size:30px;color:#000;line-height:80px;text-align:center;background:lightgreen">""" + str(weeklyTeamScoresDictKeys[0]) + """</div></td>
	</tr>
	<tr style="height:5px;"><td colspan="3"></td></tr>
	""")
	
	emailMessageList.append("""<!--Least points scored so far -->
	<tr style="background:lightgreen;">
		<td colspan="3"><strong>""" + inputsArray[5] + """</strong><div style="font-size:10px">(Overall)</div></td>
	</tr>
	<tr style="background:lightgreen;">
		<td></td>
		<td>""" + lowestPFTeamName + """</td>
		<td><div style="width:90px;height:90px;border-radius:45px;font-size:26px;color:#000;line-height:90px;text-align:center;background:#fff">""" + str(lowestPF) + """</div></td>
	</tr>
	<tr style="background-color:lightgreen;height:5px;"><td colspan="3"></td></tr>
	""")
	
	emailMessageList.append("""	<!-- Most points scored against :( -->
	<tr>
		<td colspan="3"><strong>""" + inputsArray[6] + """</strong><div style="font-size:10px">(Overall)</div></td>
	</tr>
	<tr>
		<td></td>
		<td>""" + mostPATeamName + """</td>
		<td><div style="width:100px;height:100px;border-radius:50px;font-size:26px;color:#000;line-height:100px;text-align:center;background:lightgreen">""" + str(mostPA) + """</div></td>
	</tr>
	<tr style="height:5px;"><td colspan="3"></td></tr>
	""")


	emailMessageList.append("""<!--Bottom row -->
	<tr style="background-color:lightgreen; font-size: 12px;">
		<td colspan="3">Ryan Possardt</td>
	</tr>

	</tbody>
</table>
</body>
</HTML>
""")
	return "".join(emailMessageList)

