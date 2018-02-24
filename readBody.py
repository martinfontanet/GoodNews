import urllib.request
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


url = "https://www.indiatoday.in/education-today/gk-current-affairs/story/picassos-masterpiece-sold-auction-new-york-977763-2017-05-18"
html = urllib.request.urlopen(url)
#file = open('file.html', 'w')
#file.write(html)
#file.close()
#with open(html) as fp:
#soup =  BeautifulSoup(fp)
soup = BeautifulSoup(html)
soup.a.clear()

def is_short_string(string):
    return len(string) > 10
body = soup.find_all('p')
file = open('body.html', 'w')
file.write(str(body))
file.close()
