import re
import requests
import os
import json

from bs4 import BeautifulSoup

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.36'
    }


def main():
    url = 'http://www.xbiquge.la/15/15409/'
    response = requests.get(url, headers=HEADERS)
    response.encoding = 'utf8'
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        box_con = soup.find(class_='box_con')
        ps = box_con.find_all('p')
        inf = []
        for i in range(len(ps)):
            if i == 0 or i == 2 or i == 5:
                inf.append(ps[i].string)
            elif i == 3:
                inf.append({'title': ps[i].a.string, 'link': ps[i].a['href']})
        return inf


if __name__ == '__main__':
    main()