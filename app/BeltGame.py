class BeltGame:
	# game object
	game = 0
	# Team object
	beltHolder = 0
	winStreak = 0
	accumulatedWins = 0

	def __init__(self, game, beltHolder):
		self.game = game
		self.beltHolder = beltHolder

	def setWinStreak(self, winStreak):
		self.winStreak = winStreak

	def setAccumulatedWins(self, accumulatedWins):
		self.accumulatedWins = accumulatedWins

	def getGame(self):
		return self.game

	def getBeltHolderBeforeGame(self):
		return self.beltHolder

	def getBeltHolderAfterGame(self):
		return self.game.getWinner()

	def getWinStreak(self):
		return self.winStreak

	def getAccumulatedWins(self):
		return self.accumulatedWins

