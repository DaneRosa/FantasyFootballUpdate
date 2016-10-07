#
# Builds the message HTML, and fills in information gathered from webscraper.
#
from ESPNScraper import getWeeklyTeamAndScoreDictionary, getTeamStandingsEast, getTeamStandingsWest, getLeaguePFDict
#inputsArray = [leagueName, mostPointsScoredTitle, LeastPointsScoredTite, mostPFTitle, LeastPFTitle]
def getMessageHTML(week, inputsArray,leagueScoreboardURL,leagueStandingsURL):
	results = getWeeklyTeamAndScoreDictionary(week,leagueScoreboardURL)
	weeklyTeamScoresDict = results[0]
	leagueSize = int(results[1])
	weeklyTeamScoresDictKeys = list(weeklyTeamScoresDict.keys())
	weeklyTeamScoresDictKeys.sort()

	teamStandingsEast = getTeamStandingsEast(leagueStandingsURL,leagueSize)
	teamStandingsWest = getTeamStandingsWest(leagueStandingsURL,leagueSize)
	leaguePFDict = getLeaguePFDict(leagueStandingsURL,leagueSize)
	leaguePFDictKeys = list(leaguePFDict.keys())
	leaguePFDictKeys.sort()

	lowestPF = leaguePFDictKeys[0]
	lowestPFTeamName = leaguePFDict[lowestPF]

	highestPF = leaguePFDictKeys[-1]
	highestPFTeamName = leaguePFDict[highestPF]

	#Use array of strings we will join later.
	emailMessageList = []
	indexCounter = 0
	emailMessageList.append("""
	<HTML>
<body style="min-width:100%;margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-left:0;padding-right:0;font-family:Arial, sans-serif;">
<table align="center" style="width:500px;table-layout:fixed;border-spacing:0;font:20px Arial, sans-serif;">
	<col style="width:5%">
	<col style="width:20%">
	<col style="width:20%">
<tbody>
	<tr>
		<th colspan="3" width="100%" style="background-color: lightgreen; font-size:50px;">""")
	emailMessageList.append(inputsArray[0] + """ week """)
	emailMessageList.append(str(week) + """ Results			
		</th>
	</tr>
	""")
	emailMessageList.append("""<!-- Most points scored rows:-->
	<tr>
		<td colspan="3"><strong>""" + inputsArray[1] +"""</strong><div style="font-size:10px">(This week)</div></td>
	</tr>
	<tr>
		<td></td>
		<td>""")
	emailMessageList.append(weeklyTeamScoresDict[weeklyTeamScoresDictKeys[-1]] + """</td>
		<td><div style="width:100px;height:100px;border-radius:50px;font-size:32px;color:#000;line-height:100px;text-align:center;background:lightgreen">""" + str(weeklyTeamScoresDictKeys[-1]) + """</div></td>
	</tr>
	<tr style="background-color: white;height:5px;"><td></td></tr>
	
	<!--Least points scored rows: -->
	<tr style="background-color:lightgreen;margin-top:10px">
		<td colspan="3"><strong>""" + inputsArray[2] + """</strong><div style="font-size:10px">(This week)</div></td>
	</tr>
	<tr style="background-color:lightgreen">
		<td></td>
		<td>""" + weeklyTeamScoresDict[weeklyTeamScoresDictKeys[0]] + """</td>
		<td><div style="width:70px;height:70px;border-radius:35px;font-size:28px;color:#000;line-height:70px;text-align:center;background:#fff">""" + str(weeklyTeamScoresDictKeys[0]) + """</div></td>
	</tr>
	<tr style="background-color: lightgreen;height:5px;"><td colspan="3"></td></tr>
	""")

	emailMessageList.append("""<!-- league standings -->
	<tr>
		<td colspan="3"><strong>League Standings:</strong></td>
	</tr>
	<tr>
		<td></td>
		<td style="font-size:18px;text-decoration:underline;">East</td>
	</tr>""")
	print("HEY THIS IS THE LEAGUE SIZE:" + str(leagueSize))
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
		</tr>""")
	emailMessageList.append("""<tr style="background-color: white;height:5px;"><td></td></tr>

	<!--Most points scored so far -->
	<tr style="background-color:lightgreen;">
		<td colspan="3"><strong>""" + inputsArray[3] + """</strong><div style="font-size:10px">(Overall)</div></td>
	</tr>
	<tr style="background-color:lightgreen">
		<td></td>
		<td>""")
	emailMessageList.append(highestPFTeamName + """</td>
		<td><div style="width:110px;height:110px;border-radius:55px;font-size:34px;color:#000;line-height:110px;text-align:center;background:#fff">""" + str(highestPF) + """</div></td>
	</tr>
	<tr style="background-color: lightgreen;height:5px;"><td colspan="3"></td></tr>""")
	emailMessageList.append("""<!--Least points scored so far -->
	<tr>
		<td colspan="3"><strong>""" + inputsArray[4] + """</strong><div style="font-size:10px">(Overall)</div></td>
	</tr>
	<tr>
		<td></td>
		<td>""" + lowestPFTeamName + """</td>
		<td><div style="width:90px;height:90px;border-radius:45px;font-size:30px;color:#000;line-height:90px;text-align:center;background:lightgreen">""" + str(lowestPF) + """</div></td>
	</tr>
	""")
	emailMessageList.append("""<tr style="background-color: white;height:5px;"><td colspan="3"></td></tr>
	
	<!-- Most points scored against? :( -->

	<!--Bottom row -->
	<tr style="background-color:lightgreen; font-size: 12px;">
		<td colspan="3">Ryan Possardt</td>
	</tr>

	</tbody>
</table>
</body>
</HTML>
""")
	return "".join(emailMessageList)

