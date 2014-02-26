class TeamStats:
	#team object
	team = 0
	winsAsChallenger = 0
	winsAsDefender = 0
	lossesAsChallenger = 0
	lossesAsDefender = 0

	def __init__(self, team):
		self.team = team
		self.winsAsChallenger = 0
		self.winsAsDefender = 0
		self.lossesAsDefender = 0
		self.lossesAsChallenger = 0

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

	def countGames(self):
		return self.countWins() + self.countLosses()

	def countWins(self):
		return self.winsAsChallenger + self.winsAsDefender

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

		return round(self.countWins() / self.countLosses * 100, 2);

	def getTeam(self):
		return self.team