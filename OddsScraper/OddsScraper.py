# http://www.oddschecker.com/football/other/sweden/allsvenskan
# //*[@id="fixtures"]/div/table/tbody/tr


from bs4 import BeautifulSoup
import lxml
import httplib2

resp, content = httplib2.Http().request("http://www.oddschecker.com/football/other/sweden/allsvenskan")
soup = BeautifulSoup(content, 'lxml')
rows = soup.find_all('tr','match-on')


print rows



