
import requests
import pprint
from bs4 import BeautifulSoup as jb

website_url = 'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1'

def midsouthshooterssupply(website_url):



    proxies = {
        "http": '34.203.142.175:80',
        "https": '157.230.103.189:43450',
    }

    try:
        response_data = requests.get(website_url, proxies=proxies)
    except:
        response_data = requests.get(website_url)

    scrap_data = jb(response_data.text, 'html.parser')

    prices = scrap_data.find_all('span', class_ = 'price')
    titles = scrap_data.find_all('a', class_ = 'catalog-item-name')
    stocks = scrap_data.find_all('span', class_ = 'status')
    manufacturers = scrap_data.find_all('a', class_ = 'catalog-item-brand')

    scraped = []
    for (price, title, stock, manufacturer) in zip([price for price in prices], [title for title in titles], [stock for stock in stocks], [ manufacturer for manufacturer in manufacturers]):

        print(scraped.append({'price': price.text, 'title': title.text, 'stock': (True if stock.text == 'Out of Stock' else False), 'manufacturer': manufacturer.text}))

    pprint.pprint(scraped)


midsouthshooterssupply(website_url)


