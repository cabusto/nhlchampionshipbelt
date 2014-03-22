from flask.ext.script import Manager
from bs4 import BeautifulSoup
import csv
import urllib2
from app import app

manager = Manager(app)

@manager.command
@manager.option('-y', '--year', help='Year the cup was awarded. (2012-13 season would be 2013)')
def scrape(year=2014):
	#this.year = 2014
	r  = urllib2.urlopen("http://www.hockey-reference.com/leagues/NHL_" + str(year) + "_games.html")
	data = r.read()
	r.close()

	soup = BeautifulSoup(data)

	table = soup.find('table')
	rows = []

	for row in table.find_all('tr'):
		rows.append([val.text.encode('utf8') for val in row.find_all('td')])
	
	with open('./app/static/data/' + str(year) + '.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(row for row in rows if row)
		
if __name__ == "__main__":
    manager.run()