class Schedule:
	# Game object
	games = []

	def __init__(self, games):
		self.setGames(games)

	def setGames(self, games):
		# some sort of sorting
		self.games = games

	def getUpcomingChampionshipGame(self, beltHolder, butNotAgainstTeam = None):
		for g in self.games:
			if g.wasPlayed():
				continue
			if (butNotAgainstTeam and butNotAgainstTeam.isPlayingIn(g)):
				continue
			if beltHolder.isPlayingIn(g):
				return g

		return None
