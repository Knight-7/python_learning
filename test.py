import  re
from urllib.request import urljoin


def main():
    with open('html.txt', 'r') as f:
        html = f.read()
    pattern = re.compile('<li.*?href="(.*?)"\ssinger="(.*?)">(.*?)</a>', re.S)
    results = re.findall(pattern, html)
    base_url = 'https://www.netmusic.com'
    for result in results:
        full_url = urljoin(base_url, result[0])
        print(f'歌手：{result[1]}, 歌曲：{result[2]}, 下载链接：{full_url}')


if __name__ == '__main__':
    main()