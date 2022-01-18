import re, os

# regex patterns
MONSTER_REGEX = "(?P<facebook__profile>(?:https?:)?\/\/(?:www\.)?(?:facebook|fb)\.com\/(?P<facebook__profile__profile>(?![A-z]+\.php)(?!marketplace|gaming|watch|me|messages|help|search|groups)[A-z0-9_\-\.]+)\/?)|(?P<facebook__profile_by_id>(?:https?:)?\/\/(?:www\.)facebook.com/(?:profile.php\?id=)?(?P<facebook__profile_by_id__id>[0-9]+))|(?P<instagram__profile>(?:https?:)?\/\/(?:www\.)?(?:instagram\.com|instagr\.am)\/(?P<instagram__profile__username>[A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?))|(?P<linkedin__company>(?:https?:)?\/\/(?:[\w]+\.)?linkedin\.com\/(?P<linkedin__company__company_type>(company)|(school))\/(?P<linkedin__company__company_permalink>[A-z0-9-À-ÿ\.]+)\/?)|(?P<linkedin__post>(?:https?:)?\/\/(?:[\w]+\.)?linkedin\.com\/feed\/update\/urn:li:activity:(?P<linkedin__post__activity_id>[0-9]+)\/?)|(?P<linkedin__profile>(?:https?:)?\/\/(?:[\w]+\.)?linkedin\.com\/in\/(?P<linkedin__profile__permalink>[\w\-\_À-ÿ%]+)\/?)|(?P<linkedin__profile_pub>(?:https?:)?\/\/(?:[\w]+\.)?linkedin\.com\/pub\/(?P<linkedin__profile_pub__permalink_pub>[A-z0-9_-]+)(?:\/[A-z0-9]+){3}\/?)|(?P<telegram__profile>(?:https?:)?\/\/(?:t(?:elegram)?\.me|telegram\.org)\/(?P<telegram__profile__username>[a-z0-9\_]{5,32})\/?)|(?P<twitter__status>(?:https?:)?\/\/(?:[A-z]+\.)?twitter\.com\/@?(?P<twitter__status__username>[A-z0-9_]+)\/status\/(?P<twitter__status__tweet_id>[0-9]+)\/?)|(?P<twitter__user>(?:https?:)?\/\/(?:[A-z]+\.)?twitter\.com\/@?(?!home|share|privacy|tos)(?P<twitter__user__username>[A-z0-9_]+)\/?)"

def find_all_social_media(html):
    '''
    Regular expression functions to look for social media accounts, facebook and instagram
    :param html: str -> requests.text or browser.page_source
    :return social_media: list -> list of social media urls
    '''
    social_media = []
    results = re.findall(MONSTER_REGEX,html)
    try:
        for sos in results:
            acc = [s.strip("/") for s in sos if "http" in s]
            acc = list(dict.fromkeys(acc))
            social_media.extend(acc)
    except:
        pass
    return list(dict.fromkeys(social_media))

def find_collections(ref,page):
    '''
    Collecting urls from a tags with <url_route> inside href attributes with /collections or /products on the route
    :param ref: str -> referer url
    :param page: BeautifulSoup object -> converted html text
    :return urls: list -> all collected urls
    '''
    try: ref = page.find("link",{"rel":"canonical"})['href']
    except: pass
    urls = []
    for a in page.find_all("a"):
        try:
            url = a['href']
            if "/collections" in url or "/products" in url:
                if ref not in url:
                    urls.append(ref.strip("/") + url)
                else:
                    urls.append(url)
        except: pass
    return list(dict.fromkeys(urls))

# system functions
def check_folder(path):
    '''
    Creating a new folder if the path is not exists
    :param path: str -> folder path
    '''
    if not os.path.exists(path):
        os.mkdir(path)