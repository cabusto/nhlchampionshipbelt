from flask_script import Manager
from bs4 import BeautifulSoup
import csv
import urllib
import certifi
import ssl
from app import app

manager = Manager(app)

@manager.command
@manager.option('-y', '--year', help='Year the cup was awarded. (2012-13 season would be 2013)')
def scrape(year=2015):
	#this.year = 2014
	url = "http://www.hockey-reference.com/leagues/NHL_" + str(year) + "_games.html";
	r  = urllib.request.urlopen(url, context=ssl.create_default_context(cafile=certifi.where()))

	print(r.getcode())
	data = r.read()
	r.close()

	table = BeautifulSoup(data, 'html.parser')
	rows = []

	for row in table.find_all('tr'):
		#line = row.find_all('th')
		#rows.append(line)
		rows.append([val.text for val in row.find_all('th')])
	
	with open('./app/static/data/' + str(year) + '.csv', 'w') as f:
		print("Writing to /app/static/data/{str(year)}.csv")
		writer = csv.writer(f, dialect='excel')
		writer.writerows(row for row in rows if row)
		
if __name__ == "__main__":
    manager.run({'scrape':scrape()})