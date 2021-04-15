import requests, lxml, re
from bs4 import BeautifulSoup

URL_BASE = 'https://siege.gg'
URL_QUERY = '/competitions?type%5B%5D=Pro' # hard-link to Pro League Competition
url = URL_BASE + URL_QUERY

page = requests.get(url)
soup = BeautifulSoup(page.text, "lxml")

# find competition-links
competitions = soup.find_all('a', {"href" : re.compile('/competitions//*')})
for comp in competitions:
    print(comp['href'] + " : " + comp.find('h3').text.strip())

    URL_QUERY = comp['href']

    # get team standings-data from competition page
    url = URL_BASE + URL_QUERY
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    rows = soup.find_all('tbody')[0].find_all('tr')
    for row in rows:
        try:
            cols=row.find_all('td')
            place = cols[0].text.strip()
            name = cols[1].text.strip()
            pts = cols[2].text.strip()
            wol = cols[3].text.strip()
            rd = cols[4].text.strip()
            print(place + " - " + name + " - " + pts + " - " + wol + " - " + rd)
        except IndexError:
            print("no data yet") # needs improvement
            continue
    print("\n")

        #cols=[x.text.strip() for x in cols]
        #print (cols[1])