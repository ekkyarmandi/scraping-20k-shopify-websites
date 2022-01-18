# import selenium library
from itertools import product
from selenium.webdriver import Chrome
from math import nan
from bs4 import BeautifulSoup
from random import choice
import json, os

# import custom functions library
import scraper

# open the browser
browser = Chrome("./driver/chromedriver.exe")

# read the urls file
websites = json.load(open("./data/urls.json"))

# specify destination folder
dest_folder = "./data/from_html/"
scraper.check_folder(dest_folder)

# iterate the html rendering process
i = 0
for url in websites:

    # specify destination ouput path
    dest_path = dest_folder + f"{i:05d}.json"
    if not os.path.exists(dest_path):
        browser.get(url)
        html = browser.page_source
        page = BeautifulSoup(html,"html.parser")

        # look for "klaviyo" strings
        if "https://static.klaviyo.com/onsite/js" in html:
            it_has_klaviyo = True
        else:
            it_has_klaviyo = False

        # website language
        try: language = page.find("html")['lang']
        except: language = nan

        # collecting social media accounts
        social_media = scraper.find_all_social_media(html)

        # look for collections urls
        it_has_learnq = nan
        learnq_strings = [
            "learnq.push(['track', 'Added to Cart', item])",
            "learnq.push(['track', 'Add To Cart', item])"
        ]
        collections = scraper.find_collections(url,page)
        it_has_collections = len(collections) > 0
        if it_has_collections:
            product_urls = [u for u in collections if "/products" in u] # filtering the product urls only
            if len(product_urls) > 0:
                product_url = choice(product_urls)
                browser.get(product_url)
                html = browser.page_source
                if any([True if f in html else False for f in learnq_strings]):
                    it_has_learnq = True
                else:
                    it_has_learnq = False

        # save the output
        info = {
            "website": url,
            "language": language,
            "it_has_klaviyo": it_has_klaviyo,
            "it_has_collections": it_has_collections,
            "it_has_learnq": it_has_learnq,
            "social_media": social_media
        }
        json.dump(info,open(dest_path,"w"))
    i += 1