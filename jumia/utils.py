"""
    name='utils',
    project='jumia'
    date='1/11/2020',
    author='Oshodi Kolapo',
"""
from bs4 import BeautifulSoup
import requests as req


def scrape_data(percent_range: int, product_type_url: str):
    products_list = []
    percents_list = []
    prices_list = []
    old_prices_list = []
    img_urls_list = []
    product_urls_list = []

    def only_percent(mdata: str):
        try:
            return int(mdata.split()[0].replace('%', ''))
        except ValueError:
            return 0
        except IndexError:
            return 0

    print("\nStarted Scraping Process")
    count = 1
    base_url = product_type_url
    url = base_url + str(count)
    while url and count < 11:
        reqs = req.get(url)
        content = reqs.content
        soup = BeautifulSoup(content, "html.parser", from_encoding="utf-8")
        print(f"                            Scraping : {url}")

        main = soup.find_all("a", {"class": "link"})
        for page_index in main:
            percent_off = ''
            try:
                percent_off = page_index.find("span", {"class": "sale-flag-percent"}).text
            except AttributeError:
                pass

            percent = only_percent(percent_off)
            if percent < -percent_range:
                product = page_index.find("span", {"class": "name"}).text.replace('\uff1a', ':').replace('\uff09',
                                                                                                         ')').replace(
                    '\uff0c', ',').replace('\uff08', '(')
                price = page_index.find("span", {"class": "price"}).text.replace('\u20a6', '').strip()
                old_price = page_index.find("span", {"class": "price -old"}).text.replace('\u20a6', '').strip()
                img_url = page_index.find("img", attrs={'width': '220'}).attrs['data-src']
                product_url = page_index.get('href')

                percent = int(-1 * percent)

                percents_list.append(percent)
                prices_list.append(price)
                products_list.append(product)
                old_prices_list.append(old_price)
                img_urls_list.append(img_url)
                product_urls_list.append(product_url)

        count += 1
        url = base_url + str(count)

    print("Finished Scraping Process ):")
    return percents_list, products_list, prices_list, old_prices_list, product_urls_list, img_urls_list
