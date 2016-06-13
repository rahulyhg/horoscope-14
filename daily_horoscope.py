import urllib
from bs4 import BeautifulSoup

url_base = 'http://www.astrology.com/horoscope/daily/'

def dailyHoroscope():
    resp = raw_input('Please enter your sun-sign: ')
    url = url_base + resp.lower() + '.html'
    html_read = urllib.urlopen(url)
    soup = BeautifulSoup(html_read,'html.parser')

    try:
        forDate = soup.find('span',{'class':'page-horoscope-date-font'}).text
        dailyPrediction = soup.find('div',{'class':'page-horoscope-text'}).text

        print "Date:",forDate
        print
        print dailyPrediction
    except:
        print "Please enter a valid sun-sign"
        dailyHoroscope()


dailyHoroscope()
