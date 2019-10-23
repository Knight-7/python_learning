import re
import requests
import os

from bs4 import BeautifulSoup

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.36'
    }


def main():
    url = 'http://www.xbiquge.la/13/13959/20185420.html'
    response = requests.get(url, headers=HEADERS)
    response.encoding = 'utf8'
    soup = BeautifulSoup(response.text, 'lxml')
    html_text = soup.prettify()
    pattern = re.compile('<br/>(.*?)<br/>|"content">(.*?)<br/>', re.S)
    results = pattern.findall(html_text)
    novel = results[0][1].strip() + '\n'
    for result in results[1:-2]:
        novel += result[0].strip() + '\n'
    return novel


if __name__ == '__main__':
    print(main())
    'http://www.xbiquge.la/7/7931/'