from bs4 import BeautifulSoup
import requests
import sys

if __name__ == '__main__':
    print("inside main..")
    url='http://www.imdb.com/chart/top'
    response=requests.get(url)
    # print("response:::::",response)

    soup=BeautifulSoup(response.text)
    ##print("soup:::::",soup)

    tr=soup.findChildren("tr")
    tr=iter(tr)
    next(tr)
    # print("tr:::::",tr)

    for movie in tr:
        print("movie:::::", movie.find('td', {'class': 'titleColumn'}).find('a').contents[0])
        # title=movie.find('td',{'class':'titleColumn'}).find('a').contents[0]
        # year=movie.find('td',{'class':'titleColumn'}).find('span',{'class':'socindaryInfo'}).contents[0]
        # rating=movie.find('td',{'class':'ratingColumn imdbRating'}).find('strong').contents[0]
        # row=title+'-'+rating

    # print(row)