from bs4 import BeautifulSoup

import urllib2

l = []
year = 2014
#r  = urllib2.urlopen("http://www.hockey-reference.com/leagues/NHL_" + str(year) + "_games.html")
r = urllib2.urlopen("http://www.nhlchampionshipbelt.com")
data = r.read()
r.close()

soup = BeautifulSoup(data)
#print soup.prettify()

print len(soup.table.tbody.tr)
i = 1
for link in soup.table.tbody.children:
    print "----------"
    print link
    i = i + 1
    
print i
    
    
    
    