from bs4 import BeautifulSoup as bs
import requests, json
import handler

def getSoup(URL):
    page = requests.get(URL)
    if page.status_code == 200:
        content = page.content

    return bs(content, 'html.parser')

def getMatches(soup):
    boxTable = soup.find_all("div", class_="brkts-matchlist")

    for box in boxTable:
        title = box.findChildren()[0].text
        try:
            timer = box.findChildren()[1].find("span", class_="timer-object").text
        except:
            timer = box.findChildren()[3].find("span", class_="timer-object").text
        
        print(title + " on " + timer)

        matches = box.find_all("div", class_="brkts-matchlist-match")
        for match in matches:
            op1 = match.find_all("div", class_="brkts-matchlist-cell")[0].attrs["aria-label"]
            op2 = match.find_all("div", class_="brkts-matchlist-cell")[2].attrs["aria-label"]
            print(op1 + " vs " + op2)

        print()
        next

def getWinner(soup):
    boxTable = soup.find_all("div", class_="brkts-matchlist")

    for box in boxTable:
        matches = box.find_all("div", class_="brkts-matchlist-slot-winner")
        if(len(matches) != 0):
            title = box.findChildren()[0].text
            try:
                timer = box.findChildren()[1].find("span", class_="timer-object").text
            except:
                timer = box.findChildren()[3].find("span", class_="timer-object").text
            print(title + " on " + timer)

            for match in matches:
                print(str(matches.index(match) + 1))
                print(str(match.attrs["aria-label"]))
                
            print()

        next

# Testing Dictionaries for firestore
def testDictionary():
    thisdict = {
        "id": "playday1",
        "match1": {
            "team1": "test1",
            "team2": "test2",
            "winner": "test1"
        }
    }
    # print('{}'.format(thisdict.get('playday')))
    handler.enterDictToDb(thisdict)

if __name__ == "__main__":
    URL = "" # Liquipedia URL for R6
    soup = getSoup(URL)
    getWinner(soup)
    # getMatches(soup)
    testDictionary()
