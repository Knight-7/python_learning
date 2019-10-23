import re
import requests
import os

from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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


def get_novel_text(url):
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


def write_to_local(chapter_title, content, novel_path):
    try:
        chapter_path = os.path.join(novel_path, chapter_title)
        with open(chapter_path + '.txt', 'a', encoding='utf8') as f:
            f.write(content)
    except FileNotFoundError:
        print('目录不存在')
    except FileExistsError:
        print('目录已经存在')


def main(base_url, path):
    for item in get_novel_title(base_url):
        print(f'正在下载----{item["title"]}')
        novel = get_novel_text(item['link'])
        write_to_local(item['title'], novel, path)
        sleep(0.2)


if __name__ == '__main__':
    try:
        title, url, path = input('请依次输入要爬虫的小说的名称、网址和保存地址：').split()
        novel_path = os.path.join(path, title)
        os.mkdir(novel_path)
        main(url, novel_path)
    except FileNotFoundError:
        print('目录不存在')
    except FileExistsError:
        print('目录已经存在了')