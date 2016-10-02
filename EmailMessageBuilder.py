from ESPNScraper import getWeeklyTeamAndScoreDictionary, getTeamStandingsEast, getTeamStandingsWest, getWestDivisionPFDict, getEastDivisionPFDict

def getMessageHTML(week):
	weeklyTeamScoresDict = getWeeklyTeamAndScoreDictionary(week)
	weeklyTeamScoresDictKeys = list(weeklyTeamScoresDict.keys())
	weeklyTeamScoresDictKeys.sort()
	teamStandingsEast = getTeamStandingsEast()
	teamStandingsWest = getTeamStandingsWest()
	teamPFEast = getEastDivisionPFDict()
	teamPFWest = getWestDivisionPFDict()
	teamPFEastKeys = list(teamPFEast.keys())
	teamPFWestKeys = list(teamPFWest.keys())
	teamPFEastKeys.sort()
	teamPFWestKeys.sort()
	lowestPF = teamPFEastKeys[0]
	highestPF = teamPFEastKeys[3]
	lowestPFTeamName = teamPFEast[teamPFEastKeys[0]]
	highestPFTeamName = teamPFEast[teamPFEastKeys[3]]
	if(teamPFEastKeys[0] > teamPFWestKeys[0]):
		lowestPFTeamName = teamPFWest[teamPFWestKeys[0]]
		lowestPF = teamPFWestKeys[0]
	if(teamPFEastKeys[3] < teamPFWestKeys[3]):
		highestPFTeamName = teamPFWest[teamPFWestKeys[3]]
		highestPF = teamPFWestKeys[3]
	return """
	<HTML>
<!-- Change this style tag to inline eventually -->

<body>
<table align="center" style="width: 500px;table-layout:fixed;border-spacing:0;font:20px Arial, sans-serif;">
<tbody>
	<tr>
		<th width="100%" style="background-color: lightgreen; font-size:50px;">
			
				Tolland Fantasy Buttball Weekly Results
					
		</th>
	</tr>
	
	<!-- Most points scored rows:-->
	<tr>
		<td style="float:left;"><strong>Most Points Scored:</strong><div style="font-size:10px">(This week)</div></td>
	</tr>
	<tr>
		<td style="float:left;" width="10%"></td>
		<td style="float:left;" width="50%">""" + weeklyTeamScoresDict[weeklyTeamScoresDictKeys[7]] + """</td>
		<td style="float:left;"><div style="width:90px;height:90px;border-radius:45px;font-size:32px;color:#000;line-height:90px;text-align:center;background:lightgreen">""" + str(weeklyTeamScoresDictKeys[7]) + """</div></td>
	</tr>
	<tr style="background-color: white;height:5px;"><td></td></tr>
	
	<!--Least points scored rows: -->
	<tr style="background-color:lightgreen;margin-top:10px">
		<td style="float:left;"><strong>Least Points Scored: </strong><div style="font-size:10px">(This week)</div></td>
	</tr>
	<tr style="background-color:lightgreen">
		<td style="float:left;" width="10%"></td>
		<td style="float:left;" width="50%">""" + weeklyTeamScoresDict[weeklyTeamScoresDictKeys[0]] + """</td>
		<td style="float:left;"><div style="width:70px;height:70px;border-radius:35px;font-size:28px;color:#000;line-height:70px;text-align:center;background:#fff">""" + str(weeklyTeamScoresDictKeys[0]) + """</div></td>
	</tr>
	<tr style="background-color: lightgreen;height:5px;"><td></td></tr>
	
	<!-- league standings -->
	<tr>
		<td style="float:left;"><strong>League Standings:</strong></td>
	</tr>
	<tr>
		<td style="float:left;" width="10%"></td>
		<td style="float:left;">East</td>
	</tr>
	<tr style="font-size:15px">
		<td style="float:left;" width="15%"></td>
		<td style="float:left;">1. """ + teamStandingsEast[0] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td style="float:left;" width="15%"></td>
		<td style="float:left;">2. """ + teamStandingsEast[1] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td style="float:left;" width="15%"></td>
		<td style="float:left;">3. """ + teamStandingsEast[2] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td style="float:left;" width="15%"></td>
		<td style="float:left;">4. """ + teamStandingsEast[3] + """</td>
	</tr>
	<tr>
		<td style="float:left;" width="10%"></td>
		<td style="float:left;">West</td>
	</tr>
	<tr style="font-size:15px">
		<td style="float:left;" width="15%"></td>
		<td style="float:left;">1. """ + teamStandingsWest[0] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td style="float:left;" width="15%"></td>
		<td style="float:left;">2. """ + teamStandingsWest[1] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td style="float:left;" width="15%"></td>
		<td style="float:left;">3. """ + teamStandingsWest[2] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td style="float:left;" width="15%"></td>
		<td style="float:left;">4. """ + teamStandingsWest[3] + """</td>
	</tr>
	<tr style="background-color: white;height:5px;"><td></td></tr>

	<!--Most points scored so far -->
	<tr style="background-color:lightgreen;">
		<td style="float:left;"><strong>Overall Scoring Leader:</strong></td>
	</tr>
	<tr style="background-color:lightgreen">
		<td style="float:left;" width="10%"></td>
		<td style="float:left;" width="50%">""" + highestPFTeamName + """</td>
		<td style="float:left;"><div style="width:110px;height:110px;border-radius:55px;font-size:34px;color:#000;line-height:110px;text-align:center;background:#fff">"""+ str(highestPF) +"""</div></td>
	</tr>
	<tr style="background-color: lightgreen;height:5px;"><td></td></tr>

	<!--Least points scored so far -->
	<tr>
		<td style="float:left;"><strong>Overall Scoring Loser:</strong></td>
	</tr>
	<tr>
		<td style="float:left;" width="10%"></td>
		<td style="float:left;" width="50%">"""+ lowestPFTeamName +"""</td>
		<td style="float:left;"><div style="width:90px;height:90px;border-radius:45px;font-size:30px;color:#000;line-height:90px;text-align:center;background:lightgreen">"""+ str(lowestPF) +"""</div></td>
	</tr>
	<tr style="background-color: white;height:5px;"><td></td></tr>
	
	<!-- Most points scored against? :( -->

	<!--Bottom row -->
	<tr style="background-color:lightgreen; font-size: 12px;">
		<td style="float:left;">Copyright Ryan Possardt</td>
	</tr>
</tbody>
</table>
</body>
</HTML>
"""

