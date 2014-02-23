import fileinput

class HReferenceParser:
	MODE_TEAMS = 1
	MODE_FRACHISES = 2

	def __init__(self):
		self.csvPath = ""
		self.mode = self.MODE_TEAMS
	
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
        'Vancouver Canucks ' : 'VAN',
        'Washington Capitals' : 'WSH',
        'Winnipeg Jets' : 'WPG',
	}

	

	def setCSVPath(self, path):
		self.csvPath = path

	def setMode(self, mode):
		self.mode = mode;

	def loadData(self):
		if (!fileinput.input(csvPath)) {
            return
        }
        
        a =[]
        for line in fileinput.input(self.csvPath):
        	a.append(line)
        
        return a;

    def getGames(self):
    	data = self.loadData();
    	games = []

    	for row in data:
    		date, awayTeamStr, awayTeamScore, homeTeamStr, homeTeamScore = row
    		g = new Game(date, awayTeamStr, awayTeamScore, homeTeamStr, homeTeamScore)
    		games.append(g)
        
        return games;
