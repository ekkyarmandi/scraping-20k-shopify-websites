import json, os, sys

def collect_urls(path):
    '''
    Collecting website urls only from data/urls/ and then save it as data/websites.json
    '''
    data = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith("json"):
                data.extend(json.load(open(root+file)))
    websites = []
    for d in data:
        url = d['website']
        if "www" not in url:
            url = "https://www." + url + "/"
        else:
            url = "http://" + url + "/"
        websites.append(url)
    json.dump(websites,open("./data/urls.json","w"))
    print("urls.json created")

if __name__ == '__main__':

    args = sys.argv[1]

    if args == "collect_urls":
        collect_urls("./data/urls/")