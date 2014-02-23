import Game

class Team:
	id = ""
	name = ""
	alternativeNames = []

	def __init__(self, id, name):
		self.id = id
		self.name = name

	def getID(self):
		return self.id;

	def getName(self):
		return self.name
	
	def getAlternativeNames(self):
		return self.alternativeNames

	def isSame(self, team):
		return self.getID() == team.getID()

	def isPlayingIn(self, game):
		if (self.isSame(game.getHomeTeam())):
			return True

		if (self.isSame(game.getAwayTeam())):
			return True

		return False

