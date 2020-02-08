"""
    name='iphone-scrape',
    project='stellar'
    date='1/17/2020',
    author='Oshodi Kolapo',
"""
from datetime import datetime

from time import sleep
from bs4 import BeautifulSoup
import requests as req
import csv

dataToCsv = []

startTime = datetime.now()


def only_percent(data: str):
    try:
        return int(data.split()[0].replace('%', ''))
    except ValueError:
        return 0
    except IndexError:
        return 0


def scrape_data():
    count = 1
    base_url = 'https://www.jumia.com.ng/health-beauty/?page='
    # base_url = 'https://www.jumia.com.ng/ios-phones/?page='
    url = base_url + str(count)
    while url and count < 26:
        reqs = req.get(url)
        content = reqs.content
        soup = BeautifulSoup(content, "lxml", from_encoding="utf-8")
        print(f"                            Scraping : {url}")

        main = soup.find_all("a", {"class": "link"})
        for index in main:
            percent_off = ''
            try:
                percent_off = index.find("span", {"class": "sale-flag-percent"}).text
            except AttributeError:
                pass

            percent = only_percent(percent_off)
            if percent < -70:
                product = index.find("span", {"class": "name"}).text.replace('\uff1a', ':').replace('\uff09', ')')
                price = index.find("span", {"class": "price"}).text.replace('\u20a6', '').strip()
                old_price = index.find("span", {"class": "price -old"}).text.replace('\u20a6', '').strip()
                img_url = index.img['data-src']
                link = index.get('href')

                # print(f"{percent} , {product} , {price}, {old_price}")

                dataToCsv.append(
                    [percent, product, price, old_price, img_url, link])

        count += 1
        url = base_url + str(count)
        print("SUCCESS")


scrape_data()
total_time = datetime.now() - startTime
print(total_time)
