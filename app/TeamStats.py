class TeamStats:
	#team object
	#team = None
	#winsAsChallenger = 0
	#winsAsDefender = 0
	#lossesAsChallenger = 0
	#lossesAsDefender = 0
	#winPercentage = 0

	def __init__(self, team, totalWins = 0):
		self.team = team
		self.totalWins = totalWins
		self.winsAsChallenger = 0
		self.winsAsDefender = 0
		self.lossesAsDefender = 0
		self.lossesAsChallenger = 0
		self.winPercentage = 0.0
    
	def recordGame(self, hasWon, wasBeltHolder):
		if (hasWon):
			if (wasBeltHolder):
				self.winsAsDefender += 1
			else:
				self.winsAsChallenger += 1
		else:
			if (wasBeltHolder):
				self.lossesAsDefender += 1
			else:
				self.lossesAsChallenger += 1
				
		self.calcWinPercentage()
		self.countWins()

	def countGames(self):
		return self.countWins() + self.countLosses()

	def countWins(self):
		self.totalWins = self.winsAsChallenger + self.winsAsDefender
		return self.totalWins

	def countWinsAsChallenger(self):
		return self.winsAsChallenger

	def countWinsAsDefender(self):
		return self.winsAsDefender

	def countLosses(self):
		return self.lossesAsChallenger + self.lossesAsDefender

	def countLossesAsChallenger(self):
		return self.lossesAsChallenger

	def countLossesAsDefender(self):
		return self.lossesAsDefender

	def calcWinPercentage(self):
		num_games = self.countGames()
		if (num_games == 0):
			return 0.0

		return round(self.countWins() *1.0 / self.countGames() *1.0 * 100.0, 2);

	def getTeam(self):
		return self.team