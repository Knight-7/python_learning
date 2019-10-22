import re
import requests
import os

from bs4 import BeautifulSoup

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.36'
    }


def get_str(sentence):
    p = 0
    start = 0
    for s in sentence:
        if s != '\n' and s != ' ' and start == 0:
            start = p
        if start != 0 and s == '\n':
            return sentence[start: p + 1]
        p += 1


def main():
    url = 'http://www.xbiquge.la/13/13959/20185420.html'
    response = requests.get(url, headers=HEADERS)
    response.encoding = 'utf8'
    soup = BeautifulSoup(response.text, 'lxml')
    html_text = soup.prettify()
    pattern = re.compile('<br/>(.*?)<br/>|"content">(.*?)<br/>', re.S)
    results = pattern.findall(html_text)
    novel = get_str(results[0][1])
    for result in results[1:-2]:
        novel += get_str(result[0])
    return novel


if __name__ == '__main__':
    path = '/home/knight/课程文件/Python/爬虫/圣墟/'
    with open(path + '123' + '.txt', 'a') as f:
        f.write(main())