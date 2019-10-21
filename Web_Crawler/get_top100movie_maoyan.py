import re
import requests
import json

from urllib.request import urljoin
from time import sleep

BASE_URL = 'https://maoyan.com'


def get_url_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?href="(.*?)"'
                         '.*?data-src="(.*?)".*?title="(.*?)".*?star">'
                         '(.*?)</p>.*?"releasetime">(.*?)</p>.*?"integer">(.*?)</i>'
                         '.*?"fraction">(.*?)</i>.*?</dd>', re.S)
    results = re.findall(pattern, html)
    for result in results:
        yield{
            'index': result[0],
            'link': urljoin(BASE_URL, result[1]),
            'image': result[2],
            'title': result[3],
            'actor': result[4].strip()[3:],
            'time': result[5].strip()[5:],
            'score': result[6] + result[7]
        }


def write_to_json(content):
    with open('maoyantop100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_url_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_json(item)


if __name__ == '__main__':
    for i in range(10):
        main(i * 10)
        sleep(1)