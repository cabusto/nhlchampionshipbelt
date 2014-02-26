class GameLog:
	# BeltGames
	belt_games = []
	win_streak = 0
	accumulated_wins_by_team = {}

	def __init__(self):
		self.win_streak = 0
		self.belt_games = []
		#self.clearGames()
		accumulated_wins_by_team = {}
		accumulated_wins_by_team.clear()

	def addGame(self, beltGame):
		old_holder = beltGame.getBeltHolderBeforeGame()
		new_holder = beltGame.getBeltHolderAfterGame()

		if (old_holder.isSame(new_holder)):
			self.win_streak += 1
		else:
			self.win_streak = 0

		beltGame.setWinStreak(self.win_streak)

		winner_name = new_holder.getName()
		if (winner_name in self.accumulated_wins_by_team):
			self.accumulated_wins_by_team[winner_name] += 1
			beltGame.setAccumulatedWins(self.accumulated_wins_by_team[winner_name])
		else:
			self.accumulated_wins_by_team[winner_name] = 0

		self.belt_games.append(beltGame)

	def getGames(self):
		return self.belt_games

	def clearGames(self):
		if (len(self.belt_games) > 0):
			self.belt_games[:] = []
