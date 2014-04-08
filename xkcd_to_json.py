#!/usr/bin/env python

import requests
import json
from BeautifulSoup import BeautifulSoup

XKCD_ARCHIVE = "http://xkcd.com/archive/"
XKCD_JSON_LINK = "http://xkcd.com/%i/info.0.json"

def main():
    comics = []
    for num in xrange(get_num_comics()):
        r = requests.get(XKCD_JSON_LINK % (num+1))
        if r.status_code == 200:
            r = r.json()
            comics.append({
                "title" : r['title'],
                "num" : r['num'],
                "transcript" : r['transcript'],
                "alt" : r['alt'],
                "url" : r['img']
                })
    print comics

def get_num_comics():
    r = requests.get(XKCD_ARCHIVE)
    soup = BeautifulSoup(r.text)
    return int(soup.find(id="middleContainer").findAll("a")[0]['href'][1:-1])

if __name__ == "__main__":
    main()
