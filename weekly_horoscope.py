import urllib
from bs4 import BeautifulSoup

url_base = 'http://www.astrology.com/horoscope/weekly-overview/'

def weeklyHoroscope():
    resp = raw_input('Please enter your sun-sign: ')
    url = url_base + resp.lower() + '.html'
    html_read = urllib.urlopen(url)
    soup = BeautifulSoup(html_read,'html.parser')

    try:
        forDate = soup.find('span',{'class':'page-horoscope-date-font'}).text
        weeklyPrediction = soup.find('div',{'class':'page-horoscope-text'}).text

        print forDate
        print
        print weeklyPrediction
    except:
        print "Please enter a valid sun-sign"
        weeklyHoroscope()


weeklyHoroscope()
