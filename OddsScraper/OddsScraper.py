# http://www.oddschecker.com/football/other/sweden/allsvenskan
# //*[@id="fixtures"]/div/table/tbody/tr

from __future__ import print_function
from bs4 import BeautifulSoup
import lxml
import httplib2
import io, os, stat, time


def main():
    fileName = "tmp"

    content = getData("http://www.oddschecker.com/football/other/sweden/allsvenskan", fileName)



    soup = BeautifulSoup(content, 'lxml')
    rows = soup.find_all('tr','match-on')

    for row in rows:
        colums = row.find_all('td')
        for colum in colums:
            print(colum.text, end = '\t')
        print('')



def getData(url, fileName):
    try:
        age = time.time() - os.stat(fileName)[stat.ST_MTIME]
        if age > 600:
            print("Cached file is old, downloading new")
            raise NotImplementedError

        file = io.open(fileName)
        content = file.read()
        file.close()
        if len(content) < 23:
            print("No cache file fond, downloading")
            raise EOFError
        print("Using cached file")
    except:
        resp, contentNoDecode = httplib2.Http().request(url)
        content = unicode(contentNoDecode, 'utf-8')
        file = io.open(fileName, mode = 'w+')
        file.write(content)
        file.close()
    return content



if __name__=="__main__":
   main()