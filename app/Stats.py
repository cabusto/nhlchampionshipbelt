from TeamStats import TeamStats
from BeltGame import BeltGame
from operator import itemgetter, attrgetter

class Stats:
	# TeamStats Object
	stats = {}

	def __init__(self):
		self.stats = {}

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
		if (not team.getID() in self.stats):
			t = TeamStats(team)
			self.stats[team.getID()] = t

		#print self.stats[team.getID()]
		#sorted(self.stats, key=attrgetter('winPercentage'))
		return self.stats[team.getID()]

	def getSortedStats(self):
		# sort by win Pct
		# sorted(stats)
		sortedList = []
		for s,t in self.stats.items():
			sortedList.append(t)
			
		sortedList = sorted(sortedList, key=attrgetter('totalWins'), reverse=True)
		return sortedList