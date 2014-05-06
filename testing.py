from bs4 import BeautifulSoup
import requests

'''
German Results
www.ran.de/datenbank/fussball/bundesliga/ergebnisse-und-tabelle

England Results
www.football.co.uk/match_reports/premier_league/index.shtml
'''

#Top Day Get
def get_data_bundesliga():
    home = soup.find_all('td', class_='team-name-home')
    away = soup.find_all('td', class_='team-name-away')
    result = soup.find_all('td', class_='match-result')

    for value in zip(home, result, away):
        print('Home: ' + value[0].string + ' ' + value[1].string + ' Away: ' + value[2].string)

        
def get_data_epl():
    home = soup.find_all('li', class_='home')
    away = soup.find_all('li', class_='away')
    result = soup.find_all('li', class_='v')

    for value in zip(home, result, away)[0:10]:
        print('Home: ' + value[0].string + ' ' + value[1].string + ' Away: ' + value[2].string)


while True:   
    url = raw_input("Please enter (1) for Bundesliga or (2) for EPL: ")
    
    league = ''
    

    if url == '1':
        url = 'www.ran.de/datenbank/fussball/bundesliga/ergebnisse-und-tabelle'
        league = 'Bundesliga'
        
    elif url == '2':
        url = 'www.football.co.uk/match_reports/premier_league/index.shtml'
        league = 'EPL'
        
    else:
        url = raw_input("Please try again. (1) Bundesliga or (2) EPL: ")
        
    r  = requests.get("http://" +url)

    data = r.text

    soup = BeautifulSoup(data)
    
    if league == 'Bundesliga':
        get_data_bundesliga()
        
    elif league == 'EPL':
        get_data_epl()
        
