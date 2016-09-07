import urllib
from bs4 import BeautifulSoup

url_base_daily = 'http://www.astrology.com/horoscope/daily/'
url_base_weekly = 'http://www.astrology.com/horoscope/weekly-overview/'
print1 = 'Daily Horoscope -'
print2 = 'Weekly Horoscope -'

def dailyHoroscope():
    global resp
    resp = raw_input('\nPlease enter your sun-sign: ')
    url = url_base_daily + resp.lower() + '.html'
    html_read = urllib.urlopen(url)
    soup = BeautifulSoup(html_read,'html.parser')

    try:
        forDate = soup.find('span',{'class':'page-horoscope-date-font'}).text
        dailyPrediction = soup.find('div',{'class':'page-horoscope-text'}).text
        print
        print '\n', print1, forDate
        print '-' * (len(print1) + len(forDate) + 1)
        print
        print dailyPrediction
    except:
        print 'Please enter a valid sun-sign'
        dailyHoroscope()


dailyHoroscope()

def weeklyHoroscope():
    url = url_base_weekly + resp.lower() + '.html'
    html_read = urllib.urlopen(url)
    soup = BeautifulSoup(html_read,'html.parser')

    forDate = soup.find('span',{'class':'page-horoscope-date-font'}).text
    weeklyPrediction = soup.find('div',{'class':'page-horoscope-text'}).text
    print '\n\n', print2, forDate
    print '-' * (len(print2) + len(forDate) + 1) + '\n'
    print weeklyPrediction + '\n'
    
weeklyHoroscope()
