import requests
import re
import os

from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urljoin


class Web_Crawler_novel():
    """自定义的一个从笔趣阁爬取小说的类"""

    def __init__(self, title, url, path):
        self._title = title
        self._url = url
        self._novel_path = os.path.join(path, self._title)
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/52.0.2743.116 Safari/537.36'
        }

    def get_novel_title(self):
        response = requests.get(self._url, headers=self._headers)
        response.encoding = 'utf8'
        if response.status_code == 200:
            pattern = re.compile("<dd>.*?'(.*?)' >(.*?)</a>.*?</dd>", re.S)
            results = re.findall(pattern, response.text)
            for result in results:
                yield {
                    'title': result[1],
                    'link': urljoin(self._url, result[0])
                }


    def get_novel_image(self):
        response = requests.get(self._url, headers=self._headers)
        response.encoding = 'utf8'
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            img_src = soup.find_all('img', attrs={'alt': self._title})[0]['src']
            img_content = requests.get(img_src, headers=self._headers)
            if img_content.status_code == 200:
                self.write_to_local(self._title, img_content.content, 2)

    def get_novel_text(self, url):
        response = requests.get(url, headers=self._headers)
        response.encoding = 'utf8'
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            html_text = soup.prettify()
            pattern = re.compile('<br/>(.*?)<br/>|"content">(.*?)<br/>', re.S)
            results = pattern.findall(html_text)
            novel = results[0][1].strip() + '\n'
            for result in results[1:-2]:
                novel += result[0].strip() + '\n'
            return novel

    def write_to_local(self, chapter_title, content, type = 1):
        try:
            chapter_path = os.path.join(self._novel_path, chapter_title)
            if type == 1:
                with open(chapter_path + '.txt', 'a', encoding='utf8') as f:
                    f.write(content)
            elif type == 2:
                with open(chapter_path + '.jpg', 'wb') as f:
                    f.write(content)
        except FileNotFoundError:
            print('目录不存在')
        except FileExistsError:
            print('目录已经存在')

    def make_dir(self):
        try:
            os.mkdir(self._novel_path)
            return 1
        except FileExistsError:
            print('目录已存在，无法创建')
            return 0
        except FileNotFoundError:
            print('没有找到目录')
            return 0

    def download(self):
        if self.make_dir():
            self.get_novel_image()
            for item in self.get_novel_title():
                print(f'正在下载----{item["title"]}')
                novel = self.get_novel_text(item['link'])
                self.write_to_local(item['title'], novel)
                sleep(0.2)


if __name__ == '__main__':
    douluodalu = Web_Crawler_novel(*input('请依次输入要爬虫的小说的名称、网址和保存地址：').split())
    douluodalu.download()
    # 斗罗大陆 http://www.xbiquge.la/1/1710/ C:\Users\ouyuj\Desktop\tmp\课程文件\python文件\爬虫