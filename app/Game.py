class Game:
	date = ""
	homeTeam = 0
	awayTeam = 0
	homeTeamScore = 0
	awayTeamScore = 0

	def __init__(self, date, awayTeam, awayTeamScore, homeTeam, homeTeamScore):
		self.date = date
		self.awayTeam = awayTeam
		self.awayTeamScore = awayTeamScore
		self.homeTeam = homeTeam
		self.homeTeamScore = homeTeamScore

	def wasPlayed(self):
		return self.homeTeamScore > 0 and self.awayTeamScore > 0

	def getDate(self):
		return self.date

	def getHomeTeam(self):
		return self.homeTeam

	def getAwayTeam(self):
		return self.awayTeam

	def getHomeTeamScore(self):
		return self.homeTeamScore

	def getAwayTeamScore(self):
		return self.awayTeamScore

	def getScore(self):
		return '%s : %s' %(self.homeTeamScore, self.awayTeamScore)
		
	def getWinner(self):
		if (self.homeTeamScore > self.awayTeamScore):
			return self.homeTeam
		else:
			return self.awayTeam

	def getLoser(self):
		if (self.homeTeamScore > self.awayTeamScore):
			return self.awayTeam
		else:
			return self.homeTeam 
