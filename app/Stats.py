from TeamStats import TeamStats
from BeltGame import BeltGame

class Stats:
	# TeamStats Object
	stats = {}

	def __init__(self):
		pass

	def analyzeGame(self, game, currentBeltHolder):
		self.assertTeamStats(game.getHomeTeam())
		self.assertTeamStats(game.getAwayTeam())

		if (not currentBeltHolder.isPlayingIn(game)):
			return False

		if (not game.wasPlayed()):
			return False

		winner = game.getWinner()
		self.assertTeamStats(winner).recordGame(True, currentBeltHolder.isSame(winner))

		loser = game.getLoser()
		self.assertTeamStats(loser).recordGame(False, currentBeltHolder.isSame(loser))

		return BeltGame(game, currentBeltHolder)

	def assertTeamStats(self, team):
		if (not team in self.stats):
			t = TeamStats(team)
			self.stats[team.getName()] = t

		return self.stats[team.getName()]

	def getSortedStats(self):
		# sort by win Pct
		# sorted(stats)
		pass

