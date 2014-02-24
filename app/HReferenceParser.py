import fileinput
from Game import Game
from Team import Team

class HReferenceParser:
    mode = 1
    csvPath = ""

    teams = {
        'Anaheim Ducks' : 'ANA',
        'Boston Bruins' : 'BOS',
        'Buffalo Sabres' : 'BUF',
        'Calgary Flames' : 'CAL',
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
            date = items[0]
            awayTeamStr = self.getTeam(items[1])
            awayTeamScore = items[2]
            homeTeamStr = self.getTeam(items[3])
            homeTeamScore = items[4]
            g = Game(date, awayTeamStr, awayTeamScore, homeTeamStr, homeTeamScore)
            games.append(g)
        
        return games
