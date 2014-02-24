from flask import render_template
from app import app
from Team import Team
from HReferenceParser import HReferenceParser
from Schedule import Schedule
from GameLog import GameLog
from Stats import Stats

@app.route('/')
def index():
	season = 2013
	defendingChamp = Team('CHI', 'Chicago Blackhawks')
	availableSeasons = {
		2013 : defendingChamp,
	}
	
	parser = HReferenceParser('app/static/data/2013.csv')
	games = parser.getGames()
	schedule = Schedule(games)
	gameLog = GameLog()
	stats = Stats()
	beltHolder = defendingChamp #availableSeasons[season]

	for g in schedule.games:
		beltGame = stats.analyzeGame(g, beltHolder)
		if beltGame:
			gameLog.addGame(beltGame)
			beltHolder = beltGame.getBeltHolderAfterGame()

	upcomingChampGame = schedule.getUpcomingChampionshipGame(beltHolder)
	upcomingChampGameIfHomeTeamWins = None
	upcomingChampGameIfAwayTeamWins = None
	if upcomingChampGame:
		upcomingChampGameIfHomeTeamWins = schedule.getUpcomingChampionshipGame(
			upcomingChampGame.getHomeTeam(), upcomingChampGame.getAwayTeam())
		upcomingChampGameIfAwayTeamWins = schedule.getUpcomingChampionshipGame(
			upcomingChampGame.getAwayTeam(), upcomingChampGame.getHomeTeam())

	data = {
		'id' : beltHolder.getID(),
		'name' : beltHolder.getName()
	}

	return render_template('index.html', 
		games = games, 
		availableSeasons = availableSeasons,
		beltHolder = beltHolder,
		isOngoingSeason = season,
		stats = stats,
		gameLog = gameLog,
		upcomingGame = upcomingChampGame,
		upcomingChampGameIfHomeTeamWins = upcomingChampGameIfHomeTeamWins,
		upcomingChampGameIfAwayTeamWins = upcomingChampGameIfAwayTeamWins
		)

