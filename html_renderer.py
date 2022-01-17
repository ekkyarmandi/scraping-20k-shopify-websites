# import selenium library
from selenium.webdriver import Chrome
from math import nan
from bs4 import BeautifulSoup
import json, re

# import custom functions library
import scraper

# open the browser
browser = Chrome("./driver/chromedriver.exe")

# read the urls file
websites = json.load(open("./data/urls.json"))

# iterate the html rendering process
i = 0
for url in websites:

    # specify destination ouput path
    dest_path = f"./data/from_html/{i:05d}.json"
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

        # save the output
        info = {
            "website": url,
            "language": language,
            "it_has_klaviyo": it_has_klaviyo,
            "social_media": social_media
        }
        json.dump(info,open(f"./data/from_html/{i:05d}.json","w"))
    i += 1