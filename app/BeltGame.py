class BeltGame:
	# game object
	game = None
	# Team object
	beltHolder = None
	winStreak = 0
	accumulatedWins = 0

	def __init__(self, game, beltHolder):
		self.winStreak = 0
		self.accumulatedWins = 0
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

