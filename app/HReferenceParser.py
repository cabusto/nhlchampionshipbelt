import fileinput
from Game import Game
from Team import Team
from datetime import date

class HReferenceParser:
	mode = 1
	csvPath = ""

	teams = {
        'Anaheim Ducks' : 'ANA',
        'Boston Bruins' : 'BOS',
        'Buffalo Sabres' : 'BUF',
        'Calgary Flames' : 'CGY',
        'Carolina Hurricanes' : 'CAR',
        'Chicago Blackhawks' : 'CHI', 
        'Colorado Avalanche' : 'COL',
        'Columbus Blue Jackets' : 'CBJ',
        'Dallas Stars' : 'DAL',
        'Detroit Red Wings' : 'DET',
        'Edmonton Oilers' : 'EDM',
        'Florida Panthers' : 'FLA',
        'Los Angeles Kings' : 'LAK',
        'Minnesota Wild' : 'MIN',
        'Montreal Canadiens' : 'MON',
        'Nashville Predators' : 'NSH',
        'New Jersey Devils' : 'NJD',
        'New York Islanders' : 'NYI',
        'New York Rangers' : 'NYR',
        'Ottawa Senators' : 'OTT',
        'Philadelphia Flyers' : 'PHI',
        'Phoenix Coyotes' : 'PHX',
        'Pittsburgh Penguins' : 'PIT',
        'San Jose Sharks' : 'SJS',
        'St. Louis Blues' : 'STL',
        'Tampa Bay Lightning' : 'TB',
        'Toronto Maple Leafs' : 'TOR',
        'Vancouver Canucks' : 'VAN',
        'Washington Capitals' : 'WSH',
        'Winnipeg Jets' : 'WPG',
				'Atlanta Thrashers' : 'ATL',
	}

	def __init__(self, filepath, mode = 1):
		self.csvPath = filepath
		self.mode = mode

	def setCSVPath(self, path):
		self.csvPath = path

	def setMode(self, mode):
		self.mode = mode

	def loadData(self):
		a = []
		if (not fileinput.input(self.csvPath)):
			return a

		for line in fileinput.input(self.csvPath):
			a.append(line)

		return a

	def getTeam(self, teamName):
		id = self.getTeamId(teamName)
		return Team(id, teamName)

	def getTeamId(self, teamName):
		return self.teams[teamName]


	def getGames(self):
		data = self.loadData();
		games = []

		for row in data:
			items = row.split(',')
			gamedate = items[0]
			awayTeamStr = self.getTeam(items[1])
			if (len(items[2]) > 0):
				awayTeamScore = items[2]
			else:
				awayTeamScore = 0
			
			homeTeamStr = self.getTeam(items[3])
						
			if (len(items[4]) > 0):
				homeTeamScore = items[4]
			else:
				homeTeamScore = 0
								
			g = Game(gamedate, awayTeamStr, awayTeamScore, homeTeamStr, homeTeamScore)
			if (gamedate < str(date.today()) and not g.wasPlayed()):
				# if here, means game was postponed or cancelled. it screws up the upcoming games
				# if one of the teams in the postponed games was involved
				pass
			else:
				games.append(g)
					
				
		return games
