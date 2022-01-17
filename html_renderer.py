# import selenium library
from selenium.webdriver import Chrome
from math import nan
import BeautifulSoup
import json, re

# import custom functions library
import crawler

# open the browser
browser = Chrome("./driver/chromedriver.exe")

# read the urls file
websites = json.load(open("./data/urls.json"))

# iterate the html rendering process
i = 0
for url in websites:
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
    social_media = crawler.find_all_social_media(html)

    # 