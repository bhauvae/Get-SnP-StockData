import requests
import bs4 as bs


def get_tickers():
    resp = requests.get("http://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find_all("table")[0]  # Grab the first table

    tickers = []
    for row in table.findAll("tr")[1:]:
        ticker = row.findAll("td")[0].text.strip("\n")
        tickers.append(ticker)

    return tickers
