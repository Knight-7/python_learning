import re
import requests

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


def get_novel_text(name, url):
    response = requests.get(url, headers=HEADERS)
    response.encoding = 'utf8'
    if response.status_code == 200:
        pattern = re.compile("<div id='content'>.*?</div>")
        results = re.findall(pattern, response.text)
        for result in results:
            print(result)


def main():
    base_url = 'http://www.xbiquge.la/13/13959'
    get_novel_title(base_url)
    for item in get_novel_title(base_url):
        print(item['title'], item['link'])


if __name__ == '__main__':
    get_novel_text('123', 'http://www.xbiquge.la/13/13959/20171982.html')