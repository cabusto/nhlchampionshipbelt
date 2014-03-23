from flask import render_template, redirect, url_for
from app import app
from Team import Team
from HReferenceParser import HReferenceParser
from Schedule import Schedule
from GameLog import GameLog
from Stats import Stats
from BeltGame import BeltGame

season = 2014
availableSeasons = {
		2006 : Team('CAR', 'Carolina Hurricanes'),									
		2007 : Team('ANA', 'Anaheim Ducks'),
		2008 : Team('DET', 'Detroit Red Wings'),									
		2009 : Team('PIT', 'Pittsburgh Penguins'),
		2010 : Team('CHI', 'Chicago Blackhawks'),									
		2011 : Team('BOS', 'Boston Bruins'),
		2012 : Team('LAK', 'Los Angeles Kings'),									
		2013 : Team('CHI', 'Chicago Blackhawks'),
	}

@app.route('/<season>')
@app.route('/')
def index(season=2014):
	season = int(season)
	champ = season - 1
	# render current season
	if (not (champ in availableSeasons)):
		# render season not available
		print 'no data for ' + str(season)
		return redirect(url_for('index'))
		
	
	#data = season
	parser = HReferenceParser('app/static/data/' + str(season) + '.csv')
	games = parser.getGames()
	schedule = Schedule(games)
	gameLog = GameLog()

	stats = Stats()
	beltHolder = availableSeasons[champ]
	defendingChamp = beltHolder
	beltGame = None

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
		games = gameLog.getGames(), 
		availableSeasons = availableSeasons,
    defendingChamp = defendingChamp,
		beltHolder = beltHolder,
		isOngoingSeason = season,
		stats = stats,
		gameLog = gameLog,
		upcomingChampGame = upcomingChampGame,
		upcomingChampGameIfHomeTeamWins = upcomingChampGameIfHomeTeamWins,
		upcomingChampGameIfAwayTeamWins = upcomingChampGameIfAwayTeamWins,
    sortedStats = stats.getSortedStats(),
		currentSeason = season,
		)

