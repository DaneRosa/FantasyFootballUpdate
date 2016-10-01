from ESPNScraper import getWeeklyTeamAndScoreDictionary, getTeamStandingsEast, getTeamStandingsWest

def getMessageHTML(week):
	weeklyTeamScoresDict = getWeeklyTeamAndScoreDictionary(week)
	weeklyTeamScoresDictKeys = list(weeklyTeamScoresDict.keys())
	weeklyTeamScoresDictKeys.sort()
	teamStandingsEast = getTeamStandingsEast()
	teamStandingsWest = getTeamStandingsWest()
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
		<td style="float:left;"><div style="border-radius:50%;	width: 90px;height: 90px;padding: 8px;background: lightgreen;border: 0px solid #666;color: #666;text-align: center;font: 32px Arial, sans-serif;">""" + str(weeklyTeamScoresDictKeys[7]) + """</div></td>
	</tr>
	<tr style="background-color: white;height:5px;"><td></td></tr>
	
	<!--Least points scored rows: -->
	<tr style="background-color:lightgreen;margin-top:10px">
		<td style="float:left;"><strong>Least Points Scored: </strong><div style="font-size:10px">(This week)</div></td>
	</tr>
	<tr style="background-color:lightgreen">
		<td style="float:left;" width="10%"></td>
		<td style="float:left;" width="50%">""" + weeklyTeamScoresDict[weeklyTeamScoresDictKeys[0]] + """</td>
		<td style="float:left;"><div style="border-radius:50%;	width: 70px;height: 70px;padding: 8px;background: white;border: 0px solid #666;color: #666;text-align: center;font: 32px Arial, sans-serif;">""" + str(weeklyTeamScoresDictKeys[0]) + """</div></td>
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
		<td style="float:left;" width="50%">TeamName</td>
		<td style="float:left;"><div style="border-radius:50%;	width: 70px;height: 70px;padding: 8px;background: white;border: 0px solid #666;color: #666;text-align: center;vertical-align:center;font: 32px Arial, sans-serif;">500</div></td>
	</tr>
	<tr style="background-color: lightgreen;height:5px;"><td></td></tr>

	<!--Least points scored so far -->
	<tr>
		<td style="float:left;"><strong>Overall Scoring Loser:</strong></td>
	</tr>
	<tr>
		<td style="float:left;" width="10%"></td>
		<td style="float:left;" width="50%">TeamName</td>
		<td style="float:left;"><div style="border-radius:50%;	width: 70px;height: 70px;padding: 8px;background: lightgreen;border: 0px solid #666;color: #666;text-align: center;font: 32px Arial, sans-serif;">100</div></td>
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
