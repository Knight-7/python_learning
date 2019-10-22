import re
import requests
import os

from time import sleep
from bs4 import BeautifulSoup
from urllib.request import urljoin

HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.36'
    }


def get_novel_title(book_url):
    response = requests.get(book_url, headers=HEADERS)
    response.encoding = 'utf8'
    if response.status_code == 200:
        pattern = re.compile("<dd>.*?'(.*?)' >(.*?)</a>.*?</dd>", re.S)
        results = re.findall(pattern, response.text)
        for result in results:
            yield{
                'title': result[1],
                'link': urljoin(book_url, result[0])
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


def get_novel_text(url):
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


def write_to_local(title, content):
    path_file = '/home/knight/课程文件/Python/爬虫/圣墟/'
    with open(path_file + title + '.txt', 'a') as f:
        f.write(content)


def main():
    base_url = 'http://www.xbiquge.la/13/13959'
    get_novel_title(base_url)
    for item in get_novel_title(base_url):
        print(f'正在下载----{item["title"]}')
        novel = get_novel_text(item['link'])
        write_to_local(item['title'], novel)
        sleep(0.2)


if __name__ == '__main__':
    path = '/home/knight/课程文件/Python/爬虫'
    os.mkdir(path + '/圣墟')
    main()