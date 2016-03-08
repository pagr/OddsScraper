# http://www.oddschecker.com/football/other/sweden/allsvenskan
# //*[@id="fixtures"]/div/table/tbody/tr

from __future__ import print_function
from bs4 import BeautifulSoup
import lxml
import httplib2
import io
import os
import stat
import time
import fractions


class Match:
    def __init__(self, teamA, oddsA, teamB, oddsB, oddsDraw, url):
        self.teamA = teamA
        self.oddsA = parseFraction(oddsA.replace("(","").replace(")",""))
        self.teamB = teamB
        self.oddsB = parseFraction(oddsB.replace("(","").replace(")",""))
        self.oddsDraw = parseFraction(oddsDraw.replace("(","").replace(")",""))
        self.url = url

def main():

    domain = 'http://www.oddschecker.com/'
    cacheFile = "tmp"

    content = getData(domain + "football/other/sweden/allsvenskan", cacheFile)



    soup = BeautifulSoup(content, 'lxml')
    rows = soup.find_all('tr','match-on')

    for row in rows:
        colums = row.find_all('td')
        url = row.find('a','button')
        odds = row.find_all('span', 'odds')
        teams = row.find_all('span', 'fixtures-bet-name')

        Match(teams[0].text, odds[0].text, teams[2].text, odds[2].text, odds[1].text, url.attrs['href'])
        

def parseFraction(txt):
    return float(fractions.Fraction(txt))

def getData(url, cacheFile):
    try:
        age = time.time() - os.stat(cacheFile)[stat.ST_MTIME]
        if age > 600:
            print("Cached file is old, downloading new")
            raise NotImplementedError

        file = io.open(cacheFile)
        content = file.read()
        file.close()
        if len(content) < 23:
            print("No cache file fond, downloading")
            raise EOFError
        print("Using cached file")
    except:
        resp, contentNoDecode = httplib2.Http().request(url)
        content = unicode(contentNoDecode, 'utf-8')
        file = io.open(cacheFile, mode = 'w+')
        file.write(content)
        file.close()
    return content


    
if __name__ == "__main__":
   main()