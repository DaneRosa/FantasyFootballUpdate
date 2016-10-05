#
# Builds the message HTML, and fills in information gathered from webscraper.
#
from ESPNScraper import getWeeklyTeamAndScoreDictionary, getTeamStandingsEast, getTeamStandingsWest, getLeaguePFDict

def getMessageHTML(week):
	weeklyTeamScoresDict = getWeeklyTeamAndScoreDictionary(week)
	weeklyTeamScoresDictKeys = list(weeklyTeamScoresDict.keys())
	weeklyTeamScoresDictKeys.sort()
	teamStandingsEast = getTeamStandingsEast()
	teamStandingsWest = getTeamStandingsWest()
	leaguePFDict = getLeaguePFDict()
	leaguePFDictKeys = list(leaguePFDict.keys())
	leaguePFDictKeys.sort()

	lowestPF = leaguePFDictKeys[0]
	lowestPFTeamName = leaguePFDict[lowestPF]

	highestPF = leaguePFDictKeys[-1]
	highestPFTeamName = leaguePFDict[highestPF]

	return """
	<HTML>
<!-- Change this style tag to inline eventually -->

<body style="min-width:100%;margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-left:0;padding-right:0;font-family:Arial, sans-serif;">
<table align="center" style="width:500px;table-layout:fixed;border-spacing:0;font:20px Arial, sans-serif;">
	<col style="width:5%">
	<col style="width:20%">
	<col style="width:20%">
<tbody>
	<tr>
		<th colspan="3" width="100%" style="background-color: lightgreen; font-size:50px;">
			
				Tolland Fantasy Buttball Week """ + str(week) + """ Results
					
		</th>
	</tr>
	
	<!-- Most points scored rows:-->
	<tr>
		<td colspan="3"><strong>Most Points Scored:</strong><div style="font-size:10px">(This week)</div></td>
	</tr>
	<tr>
		<td></td>
		<td>""" + weeklyTeamScoresDict[weeklyTeamScoresDictKeys[-1]] + """</td>
		<td><div style="width:100px;height:100px;border-radius:50px;font-size:32px;color:#000;line-height:100px;text-align:center;background:lightgreen">""" + str(weeklyTeamScoresDictKeys[-1]) + """</div></td>
	</tr>
	<tr style="background-color: white;height:5px;"><td></td></tr>
	
	<!--Least points scored rows: -->
	<tr style="background-color:lightgreen;margin-top:10px">
		<td colspan="3"><strong>Least Points Scored: </strong><div style="font-size:10px">(This week)</div></td>
	</tr>
	<tr style="background-color:lightgreen">
		<td></td>
		<td>""" + weeklyTeamScoresDict[weeklyTeamScoresDictKeys[0]] + """</td>
		<td><div style="width:70px;height:70px;border-radius:35px;font-size:28px;color:#000;line-height:70px;text-align:center;background:#fff">""" + str(weeklyTeamScoresDictKeys[0]) + """</div></td>
	</tr>
	<tr style="background-color: lightgreen;height:5px;"><td colspan="3"></td></tr>
	
	<!-- league standings -->
	<tr>
		<td colspan="3"><strong>League Standings:</strong></td>
	</tr>
	<tr>
		<td></td>
		<td style="font-size:18px;text-decoration:underline;">East</td>
	</tr>
	<tr style="font-size:15px">
		<td></td>
		<td colspan="2">1. """ + teamStandingsEast[0] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td></td>
		<td colspan="2">2. """ + teamStandingsEast[1] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td></td>
		<td colspan="2">3. """ + teamStandingsEast[2] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td></td>
		<td colspan="2">4. """ + teamStandingsEast[3] + """</td>
	</tr>
	<tr>
		<td></td>
		<td style="font-size:18px;text-decoration:underline;">West</td>
	</tr>
	<tr style="font-size:15px">
		<td></td>
		<td colspan="2">1. """ + teamStandingsWest[0] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td></td>
		<td colspan="2">2. """ + teamStandingsWest[1] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td></td>
		<td colspan="2">3. """ + teamStandingsWest[2] + """</td>
	</tr>
	</tr>
	<tr style="font-size:15px">
		<td></td>
		<td colspan="2">4. """ + teamStandingsWest[3] + """</td>
	</tr>
	<tr style="background-color: white;height:5px;"><td></td></tr>

	<!--Most points scored so far -->
	<tr style="background-color:lightgreen;">
		<td colspan="3"><strong>League Scoring Leader:</strong><div style="font-size:10px">(Overall)</div></td>
	</tr>
	<tr style="background-color:lightgreen">
		<td></td>
		<td>""" + highestPFTeamName + """</td>
		<td><div style="width:110px;height:110px;border-radius:55px;font-size:34px;color:#000;line-height:110px;text-align:center;background:#fff">""" + str(highestPF) + """</div></td>
	</tr>
	<tr style="background-color: lightgreen;height:5px;"><td colspan="3"></td></tr>

	<!--Least points scored so far -->
	<tr>
		<td colspan="3"><strong>League Scoring Loser:</strong><div style="font-size:10px">(Overall)</div></td>
	</tr>
	<tr>
		<td></td>
		<td>""" + lowestPFTeamName + """</td>
		<td><div style="width:90px;height:90px;border-radius:45px;font-size:30px;color:#000;line-height:90px;text-align:center;background:lightgreen">""" + str(lowestPF) + """</div></td>
	</tr>
	<tr style="background-color: white;height:5px;"><td colspan="3"></td></tr>
	
	<!-- Most points scored against? :( -->

	<!--Bottom row -->
	<tr style="background-color:lightgreen; font-size: 12px;">
		<td colspan="3">Ryan Possardt</td>
	</tr>

</tbody>
</table>
</body>
</HTML>
"""

